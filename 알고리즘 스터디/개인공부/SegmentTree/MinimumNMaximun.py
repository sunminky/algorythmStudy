# https://www.acmicpc.net/problem/2357

import sys
from math import ceil, log2

functions = {False: min, True: max}
init_value = {False: 1000000000, True: 0}


def inflate_tree(n_number, nums, flag):
    height = ceil(log2(n_number))
    tree = [init_value[flag]] * (2 << height)
    end_layer = 1 << height

    for i in range(n_number):
        tree[end_layer + i] = nums[i]

    end_layer >>= 1
    while end_layer:
        for i in range(end_layer):
            tree[end_layer + i] = functions[flag](tree[(end_layer + i) * 2], tree[(end_layer + i) * 2 + 1])
        end_layer >>= 1

    return tree


def query(tree, query_start, query_end, nth_node, portion_start, portion_end, flag):
    # 구간을 벗어나는 경우
    if query_start > portion_end or query_end < portion_start:
        return init_value[flag]

    # 구간에 속하는 경우
    if query_start <= portion_start and portion_end <= query_end:
        return tree[nth_node]

    # 구간에 걸쳐있는 경우
    middle = (portion_start + portion_end) // 2
    return functions[flag](query(tree, query_start, query_end, nth_node * 2, portion_start, middle, flag),
                           query(tree, query_start, query_end, nth_node * 2 + 1, middle + 1, portion_end, flag))


if __name__ == '__main__':
    n_number, n_query = map(int, sys.stdin.readline().split())
    nums = [int(sys.stdin.readline()) for _ in range(n_number)]
    min_tree = inflate_tree(n_number, nums, False)
    max_tree = inflate_tree(n_number, nums, True)
    tree_end = 1 << ceil(log2(n_number))

    for _ in range(n_query):
        start, end = map(int, sys.stdin.readline().split())
        print(query(min_tree, start, end, 1, 1, tree_end, False), query(max_tree, start, end, 1, 1, tree_end, True))
