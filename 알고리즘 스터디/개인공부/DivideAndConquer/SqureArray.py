# https://www.acmicpc.net/problem/10830

import sys
from math import log2, ceil, floor


def matrix_mul(arr1, arr2, N) -> list:
    memo = [[0 for _ in range(N)] for _ in range(N)]

    for r1 in range(N):
        for c1 in range(N):
            for c2 in range(N):
                memo[r1][c1] = (memo[r1][c1] + arr1[r1][c2] * arr2[c2][c1]) % 1000

    return memo


if __name__ == '__main__':
    N, expoential = map(int, sys.stdin.readline().split())
    arr = [list(map(lambda x: int(x)%1000, sys.stdin.readline().split())) for _ in range(N)]
    memo = [None for _ in range(40)]   #log2(100000000000)
    memo[0] = arr.copy()

    #memo[i] = 행렬의 2 ** i 제곱
    for i in range(1, ceil(log2(expoential) + 1)):
        memo[i] = matrix_mul(memo[i-1], memo[i-1], N)

    answer = None

    while expoential > 0:
        tmp = floor(log2(expoential))

        if answer is None:
            answer = memo[tmp]
        else:
            #행렬 곱
            answer = matrix_mul(answer, memo[tmp], N)

        expoential -= 2 ** tmp

    for _ans in answer:
        print(" ".join(map(str, _ans)))