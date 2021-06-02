# https://www.acmicpc.net/problem/1572
# https://www.acmicpc.net/problem/9426
import sys


def inflate_tree():
    # height = 17     # ceil(log2(65536 + 1))
    tree = [0] * 262144     # (2 << height)

    return tree


def update(tree, nth_node, value):
    nth_node += 131072    # 1 << height
    # Bottom-Up
    while nth_node:
        tree[nth_node] += value
        nth_node >>= 1


def search(tree, limit):
    query_start = 0
    query_end = 131071  # (1 << height) - 1
    nth_node = 1
    remain = limit

    # Top-Down
    while query_start < query_end:
        middle = (query_start + query_end) >> 1

        if tree[nth_node * 2] < remain:
            remain -= tree[nth_node * 2]
            query_start = middle + 1
            nth_node = nth_node * 2 + 1
        else:
            query_end = middle
            nth_node <<= 1

    return query_start


if __name__ == '__main__':
    n_number, width = map(int, sys.stdin.readline().split())
    numbers = tuple(int(sys.stdin.readline()) for _ in range(n_number))
    tree = inflate_tree()
    answer = 0

    for i in range(width - 1):
        update(tree, numbers[i], 1)

    for i in range(n_number - width + 1):
        update(tree, numbers[i + width - 1], 1)
        answer += search(tree, (width + 1) >> 1)
        update(tree, numbers[i], -1)

    print(answer)
