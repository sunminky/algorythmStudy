# https://www.acmicpc.net/problem/17404

import sys

if __name__ == '__main__':
    cost = [tuple(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))]
    answer = 10000000

    for i in range(3):
        estimate = [[0] * 3 for _ in range(len(cost))]

        for j in range(3):
            estimate[1][j] = cost[0][i] + cost[1][j]

        estimate[1][i] = 2001

        for j in range(2, len(cost)):
            estimate[j][0] = cost[j][0] + min(estimate[j-1][1], estimate[j-1][2])
            estimate[j][1] = cost[j][1] + min(estimate[j - 1][0], estimate[j - 1][2])
            estimate[j][2] = cost[j][2] + min(estimate[j - 1][0], estimate[j - 1][1])

        estimate[-1][i] = 10000000
        answer = min(answer, min(estimate[-1]))

    print(answer)
