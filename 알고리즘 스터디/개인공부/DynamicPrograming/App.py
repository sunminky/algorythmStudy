#https://www.acmicpc.net/problem/7579

import sys

if __name__ == '__main__':
    N, mem_limit = tuple(map(int, sys.stdin.readline().split()))
    mem = tuple(map(int, sys.stdin.readline().split()))
    cost = tuple(map(int, sys.stdin.readline().split()))
    sum_cost = sum(cost)
    knapsack = [-1 for _ in range(sum_cost+1)]
    answer = sum_cost

    knapsack[0] = 0  #아무것도 안챙김

    for i in range(N):
        prev_knapsack = knapsack.copy()

        for j in range(sum_cost+1):
            if prev_knapsack[j] != -1:
                knapsack[j + cost[i]] = max(knapsack[j + cost[i]], prev_knapsack[j] + mem[i])

    for i in range(sum_cost + 1):
        if knapsack[i] != -1 and knapsack[i] >= mem_limit:
            answer = i
            break

    print(answer)