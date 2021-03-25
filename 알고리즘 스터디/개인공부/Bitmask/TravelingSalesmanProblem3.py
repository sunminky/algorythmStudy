# https://www.acmicpc.net/problem/16991

import sys
from math import sqrt


n_city = int(sys.stdin.readline())
location = [tuple(map(int, sys.stdin.readline().split()))for _ in range(n_city)]
path = [[0 for _ in range(n_city)] for _ in range(n_city)]  # 도시 간의 거리 저장
cost = [[-1 for _ in range(1 << n_city)] for _ in range(n_city)]        # 여행 비용 저장
all_visited = (1 << n_city) - 1


def tsp(visited, cur_loc):
    #모든 도시를 다 방문함
    if visited == all_visited:
        cost[cur_loc][visited] = path[cur_loc][0]   # 현재도시에서 0번도시로 가는 값

    else:
        #아직 비용이 계산 되지 않았다면
        if cost[cur_loc][visited] == -1:
            cost[cur_loc][visited] = 16001  # 가질수 있는 최대값으로 세팅
            for city in range(n_city):
                # 이미 방문한 도시면 패스
                if visited & (1 << city):
                    continue
                cost[cur_loc][visited] = min(cost[cur_loc][visited], tsp(visited | (1 << city), city) + path[cur_loc][city])

    return cost[cur_loc][visited]



if __name__ == '__main__':
    # 도시간의 거리 계산
    for row in range(n_city):
        for col in range(n_city):
            path[row][col] = sqrt((location[row][0] - location[col][0]) ** 2 + (location[row][1] - location[col][1]) ** 2)

    print(f"{tsp(1, 0):.7f}")
