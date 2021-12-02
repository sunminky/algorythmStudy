# https://www.acmicpc.net/problem/10868

import sys

INF = 1000000000
n_number, n_query = map(int, sys.stdin.readline().split())
number = [int(sys.stdin.readline()) for _ in range(n_number)]
tree1 = [INF] * (n_number + 1)
tree2 = [INF] * (n_number + 1)


def update1(tree, nth_node, value):
    while nth_node <= n_number:
        tree[nth_node] = min(tree[nth_node], value)
        nth_node += nth_node & -nth_node


def update2(tree, nth_node, value):
    while nth_node > 0:
        tree[nth_node] = min(tree[nth_node], value)
        nth_node -= nth_node & -nth_node


def query(tree1, tree2, numbers, start, end):
    result = INF

    prev = start
    cur = prev + (prev & -prev)
    while cur <= end:
        result = min(result, tree2[prev])
        prev = cur
        cur += (cur & -cur)

    result = min(result, numbers[prev - 1])

    prev = end
    cur = prev - (prev & -prev)
    while cur >= start:
        result = min(result, tree1[prev])
        prev = cur
        cur -= (cur & -cur)

    return result


if __name__ == '__main__':
    for seq, num in enumerate(number):
        update1(tree1, seq + 1, num)
        update2(tree2, seq + 1, num)

    for _ in range(n_query):
        src, dst = map(int, sys.stdin.readline().split())
        print(query(tree1, tree2, number, src, dst))
