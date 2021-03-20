# https://www.acmicpc.net/problem/9372

import sys

if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        n_country, n_flight = map(int, sys.stdin.readline().split())
        path = [[] for _ in range(n_country)]
        visited = [False for _ in range(n_country)]

        for _ in range(n_flight):
            src, dst = map(int, sys.stdin.readline().split())
            path[src-1].append(dst-1)
            path[dst-1].append(src-1)

        print(n_country - 1)