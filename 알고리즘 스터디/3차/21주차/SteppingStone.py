# https://www.acmicpc.net/problem/2602

import sys

target = sys.stdin.readline().rstrip()
bridge = [sys.stdin.readline().rstrip() for _ in range(2)]
cost = [[[-1 for _ in range(len(bridge[0]))] for _ in range(2)] for _ in range(len(target))]


def search(start, char_idx, bridge_idx):    # 탐색 시작지점, 타켓문자열 인덱스, 현재 다리 인덱스
    # 기저조건
    # 탐색이 불가능 한 경우
    if start >= len(bridge[bridge_idx]):
        return 0

    # 이미 계산한 값 인 경우
    if cost[char_idx][bridge_idx][start] != -1:
        return cost[char_idx][bridge_idx][start]

    opposite = 1 if bridge_idx == 0 else 0  # 반대편 다리 지정
    result = 0

    for i in range(start, len(bridge[bridge_idx])):
        # 현재 타겟 인덱스와 일치하는 문자 찾음
        if bridge[bridge_idx][i] == target[char_idx]:
            # 맨 끝 문자를 찾은 경우 1만 더해줌 
            if char_idx == len(target) - 1:
                result += 1
            # i + 1 ~ 다리 끝 까지 target[char_idx + 1] 와 일치하는 문자를 찾음
            else:
                result += search(i + 1, char_idx + 1, opposite)
                cost[char_idx][bridge_idx][start] = result

    return result


if __name__ == '__main__':
    answer = 0

    # 천사다리 탐색
    answer += search(0, 0, 0)

    # 비용 memoization 초기화
    cost = [[[-1 for _ in range(len(bridge[0]))] for _ in range(2)] for _ in range(len(target))]

    # 악마다리 탐색
    answer += search(0, 0, 1)

    print(answer)
