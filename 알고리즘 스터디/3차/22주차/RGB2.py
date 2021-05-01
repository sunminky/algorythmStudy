# https://www.acmicpc.net/problem/17404

import sys

if __name__ == '__main__':
    cost = [tuple(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))]
    answer = 10000000

    for i in range(3):
        estimate = [cost[0][i] + cost[1][j] for j in range(3)]
        estimate[i] = 2001

        for j in range(2, len(cost)):
            estimate = [
                cost[j][0] + min(estimate[1], estimate[2]),
                cost[j][1] + min(estimate[0], estimate[2]),
                cost[j][2] + min(estimate[0], estimate[1])
            ]

        estimate[i] = 10000000
        answer = min(answer, min(estimate))

    print(answer)
