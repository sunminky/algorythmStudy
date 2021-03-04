#https://www.acmicpc.net/problem/2096

import sys

if __name__ == '__main__':
    height = int(sys.stdin.readline())
    field = tuple(map(int, sys.stdin.readline().split()))
    max_cost = field
    min_cost = field

    for _ in range(1, height):
        field = tuple(map(int, sys.stdin.readline().split()))
        new_max_cost = [0 for _ in range(len(max_cost))]
        new_min_cost = [0 for _ in range(len(min_cost))]

        for i in range(len(field)):
            new_max_cost[i] = max(max_cost[max(0, i-1):min(len(max_cost), i+2)]) + field[i]
            new_min_cost[i] = min(min_cost[max(0, i-1):min(len(min_cost), i+2)]) + field[i]

        max_cost = new_max_cost
        min_cost = new_min_cost

    print(max(max_cost), min(min_cost))