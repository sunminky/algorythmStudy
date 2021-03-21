# https://www.acmicpc.net/problem/9372

import sys

if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        n_country, n_flight = map(int, sys.stdin.readline().split())

        for _ in range(n_flight):
            src, dst = map(int, sys.stdin.readline().split())

        print(n_country - 1)