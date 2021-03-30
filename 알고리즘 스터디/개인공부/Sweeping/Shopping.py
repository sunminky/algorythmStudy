# https://www.acmicpc.net/problem/10332

import sys

if __name__ == '__main__':
    n_city, n_restrict = map(int, sys.stdin.readline().split())
    preprocess = []

    for _ in range(n_restrict):
        map(int, sys.stdin.readline().split())
