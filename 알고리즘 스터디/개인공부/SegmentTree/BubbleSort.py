# https://www.acmicpc.net/problem/1517
# 펜윅트리

import sys


def update(tree, nth_node):
    while nth_node < len(tree):
        tree[nth_node] += 1
        nth_node += (nth_node & -nth_node)


def query(tree, nth_node):
    result = 0

    while nth_node:
        result += tree[nth_node]
        nth_node -= (nth_node & -nth_node)

    return result


if __name__ == '__main__':
    answer = 0
    n_node = int(sys.stdin.readline())
    node = sorted(zip(map(int, sys.stdin.readline().split()), range(1, n_node + 1)), key=lambda x: (x[0], x[1]),
                  reverse=True)
    tree = [0] * (n_node + 1)

    for _, pos in node:
        answer += query(tree, pos - 1)
        update(tree, pos)

    print(answer)
