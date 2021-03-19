# https://www.acmicpc.net/problem/2098

import sys

N = int(sys.stdin.readline())


def tsp(visited, current):
    global cost
    global path

    if visited == all_visited:
        if path[current][0] != 0:
            cost[current][visited] = path[current][0]   #현재위치에서 0번으로 돌아가는 비용
        else:
            cost[current][visited] = 17000001   #0번으로 돌아갈 수 없으면 값을 무한으로 세팅

        return cost[current][visited]

    # 예전에 비용을 계산 한 적이 있었다면 그대로 반환
    elif cost[current][visited] != -1:
        return cost[current][visited]

    else:
        cost[current][visited] = 17000001
        #방문 안한 노드 탐색
        for city in range(N):
            if visited & (1 << city):
                continue
            if path[current][city] == 0:
                continue

            cost[current][visited] = min(cost[current][visited], tsp(visited | (1 << city), city) + path[current][city])

    return cost[current][visited]


if __name__ == '__main__':
    global cost
    global all_visited
    global path

    path = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    cost = [[-1 for _ in range(1 << N)] for _ in range(N)]
    all_visited = (1 << N) - 1

    print(tsp(1, 0))
