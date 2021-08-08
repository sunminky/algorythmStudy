# https://www.acmicpc.net/problem/16432
import sys


def dig(cake, answer, cur_idx, prev_idx, prev_cake) -> bool:
    # 기저조건
    if cur_idx == prev_idx:
        if prev_cake != cake[prev_idx][1]:
            return True
        return False

    for cakes in cake[cur_idx][1:]:
        if cakes == prev_cake:
            continue
        if dig(cake, answer, cur_idx + 1, prev_idx, cakes):
            answer.append(cakes)
            return True

    return False


if __name__ == '__main__':
    cake = [tuple(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))]
    prev_single = len(cake)
    answer = []
    success = True

    cake.append((1, -2))

    for i in range(len(cake) - 2, -1, -1):
        # 떡이 하나밖에 없음
        if cake[i][0] == 1 or i == 0:
            # 현재위치 ~ 이전 하나밖에 없는 위치까지 도달가능한지 체크
            success = dig(cake, answer, i, prev_single, -1)
            prev_single = i
            if not success:
                break

    if success:
        for e in reversed(answer):
            print(e)
    else:
        print(-1)
