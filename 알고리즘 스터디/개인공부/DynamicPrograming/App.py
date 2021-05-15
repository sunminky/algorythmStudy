# https://www.acmicpc.net/problem/7579
import sys

if __name__ == '__main__':
    N, mem_limit = tuple(map(int, sys.stdin.readline().split()))
    mem = tuple(map(int, sys.stdin.readline().split()))
    cost = tuple(map(int, sys.stdin.readline().split()))
    knapsack = {0: 0}   # 아무것도 안챙긴 경우가 기본값
    answer = sum_cost = sum(cost)

    for i in range(N):
        prev_knapsack = knapsack.copy()

        for key in prev_knapsack:
            knapsack[key + cost[i]] = max(knapsack.get(key + cost[i], 0), prev_knapsack[key] + mem[i])

    for key in knapsack:
        if knapsack[key] >= mem_limit:
            answer = min(answer, key)

    print(answer)
