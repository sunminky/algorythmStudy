# https://www.acmicpc.net/problem/2668
import sys

if __name__ == '__main__':
    number = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
    qualified = [False] * (len(number) + 1)     # 집합에 속하는지 체크

    for i in range(len(number)):
        visited = [False] * (len(number) + 1)
        stack = []  # 방문한 노드 저장
        cur_idx = i + 1

        # 자기 자신으로 돌아오기전 qualified만나거나 이미 방문했던 곳 만나면 false
        while not visited[cur_idx] and not qualified[cur_idx]:
            visited[cur_idx] = True
            stack.append(cur_idx)
            cur_idx = number[cur_idx - 1]

            # 다시 자기자신으로 돌아온 경우
            if cur_idx == i + 1:
                break
        # 집합에 속하지 못함
        else:
            continue

        # 집합에 속한다면 방문했던 노드들 집합에 넣어주기
        for e in stack:
            qualified[e] = True

    print(sum(qualified))   # 집합에 속하는 원소들의 개수
    for i in range(1, len(qualified)):
        if qualified[i]:
            print(i)
