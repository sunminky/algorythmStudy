# https://www.acmicpc.net/problem/12837
import sys
from math import ceil, log2


def inflate_tree(numbers):
    tree_height = ceil(log2(numbers))
    end_layer = 1 << tree_height
    tree = [0] * (2 << tree_height)

    return tree, end_layer


def search(tree, query_start, query_end, nth_node, portion_start, portion_end):
    # 구간을 벗어난 경우
    if portion_end < query_start or query_end < portion_start:
        return 0
    # 구간에 속하는 경우
    if query_start <= portion_start and portion_end <= query_end:
        return tree[nth_node]
    # 구간에 걸쳐있는 경우
    middle = (portion_start + portion_end) // 2
    return search(tree, query_start, query_end, nth_node * 2, portion_start, middle) \
           + search(tree, query_start, query_end, nth_node * 2 + 1, middle + 1, portion_end)


def update(tree, nth_node, value):
    while nth_node:
        tree[nth_node] += value
        nth_node >>= 1


if __name__ == '__main__':
    life, n_query = map(int, sys.stdin.readline().split())
    tree, end_layer = inflate_tree(life)

    for _ in range(n_query):
        action, date, currency = map(int, sys.stdin.readline().split())

        if action == 1:
            update(tree, end_layer + date - 1, currency)
        else:
            print(search(tree, date, currency, 1, 1, end_layer))
