# https://www.acmicpc.net/problem/7578
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
    line_a = sys.stdin.readline().split()
    line_b = sys.stdin.readline().split()
    seq_dict = dict(zip(line_b, range(1, n_node + 1)))
    tree = [0] * (n_node + 1)

    for machine in reversed(line_a):
        answer += query(tree, seq_dict[machine])
        update(tree, seq_dict[machine])

    print(answer)
