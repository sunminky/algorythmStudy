# https://www.acmicpc.net/problem/2533

import sys

if __name__ == '__main__':
    n_node = int(sys.stdin.readline())
    tree = [[] for _ in range(n_node)]

    for _ in range(n_node - 1):
        src, dst = map(int, sys.stdin.readline().split())

        tree[src - 1].append(dst - 1)
        tree[dst - 1].append(src - 1)

    print(tree)
