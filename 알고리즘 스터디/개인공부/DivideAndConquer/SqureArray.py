# https://www.acmicpc.net/problem/10830

import sys

if __name__ == '__main__':
    N, expoential = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    b = arr.copy()

    for _ in range(1, expoential):
        prev_arr = b.copy()
        b = [[0 for _ in range(N)] for _ in range(N)]
        for r1 in range(N):
            for c1 in range(N):
                for c2 in range(N):
                    b[r1][c1] = (b[r1][c1] + arr[r1][c2] * prev_arr[c2][c1]) % 1000

    for _b in b:
        print(" ".join(map(str, _b)))