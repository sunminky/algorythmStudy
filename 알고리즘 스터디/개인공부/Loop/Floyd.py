#https://www.acmicpc.net/problem/11404

import sys

if __name__ == '__main__':
    n_city = int(sys.stdin.readline())
    n_bus = int(sys.stdin.readline())
    costs = [[0 if i == j else 10000001 for j in range(n_city)] for i in range(n_city)]

    for _ in range(n_bus):
        src, dst, cost = tuple(map(int, sys.stdin.readline().split()))
        costs[src-1][dst-1] = min(costs[src-1][dst-1], cost)

    #플루이드 와샬
    for passby in range(n_city):    #거치는 노드
        for row in range(n_city):
            for col in range(n_city):
                costs[row][col] = min(costs[row][passby] + costs[passby][col], costs[row][col])

    for i in range(n_city):
        for j in range(n_city):
            if costs[i][j] == 10000001:
                print(0, end=" ")
            else:
                print(costs[i][j], end=" ")
        print()