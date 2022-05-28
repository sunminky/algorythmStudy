# https://www.acmicpc.net/problem/10868

import sys
from math import ceil, log2


def inflate_tree(n_number, nums):
    height = ceil(log2(n_number))
    tree = [1000000000] * (2 << height)
    end_layer = 1 << height

    for i in range(n_number):
        tree[end_layer + i] = nums[i]

    end_layer >>= 1
    while end_layer:
        for i in range(end_layer):
            tree[end_layer + i] = min(tree[(end_layer + i) * 2], tree[(end_layer + i) * 2 + 1])

        end_layer >>= 1

    return tree


def query(tree, query_start, query_end, nth_node, portion_start, portion_end):
    # 구간을 벗어나는 경우
    if query_start > portion_end or query_end < portion_start:
        return 1000000000

    # 구간에 속하는 경우
    if query_start <= portion_start and portion_end <= query_end:
        return tree[nth_node]

    # 구간에 걸치는 경우
    middle = (portion_start + portion_end) // 2
    return min(query(tree, query_start, query_end, nth_node * 2, portion_start, middle),
               query(tree, query_start, query_end, nth_node * 2 + 1, middle + 1, portion_end))


if __name__ == '__main__':
    n_number, n_query = map(int, sys.stdin.readline().split())
    nums = [int(sys.stdin.readline()) for _ in range(n_number)]
    tree = inflate_tree(n_number, nums)
    end_layer = 1 << ceil(log2(n_number))

    for _ in range(n_query):
        start, end = map(int, sys.stdin.readline().split())
        print(query(tree, start, end, 1, 1, end_layer))
