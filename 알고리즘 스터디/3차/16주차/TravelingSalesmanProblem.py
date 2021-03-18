# https://www.acmicpc.net/problem/2098

import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    path = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    print(path)