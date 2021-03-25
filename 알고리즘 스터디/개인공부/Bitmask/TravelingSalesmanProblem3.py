# https://www.acmicpc.net/problem/16991

import sys
from math import sqrt

if __name__ == '__main__':
    n_city = int(sys.stdin.readline())
    location = [tuple(map(int, sys.stdin.readline().split()))for _ in range(n_city)]
    path = [[0 for _ in range(n_city)] for _ in range(n_city)]  # 도시 간의 거리 저장
    cost = [[-1 for _ in range(1 << n_city)] for _ in range(n_city)]        # 여행 비용 저장
    
    # 도시간의 거리 계산
    for row in range(n_city):
        for col in range(n_city):
            path[row][col] = sqrt((location[row][0] - location[col][0]) ** 2 + (location[row][1] - location[col][1]) ** 2)

    print(location)
    print(path)
