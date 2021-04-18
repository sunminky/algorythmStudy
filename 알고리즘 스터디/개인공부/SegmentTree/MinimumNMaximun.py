# https://www.acmicpc.net/problem/2357

import sys
from math import ceil, log2


def inflate_tree(number, flag):
    func_collection = [min, max]
    height = ceil(log2(len(number)))
    tree = [None] * (2 << height)
    end_layer = 1 << height

    for i in range(len(number)):
        tree[end_layer + i] = number[i]

    end_layer >>= 1
    while end_layer:
        for i in range(end_layer):
            if tree[(end_layer + i) * 2 + 1] is None:
                tree[end_layer + i] = tree[(end_layer + i) * 2]
            else:
                tree[end_layer + i] = func_collection[flag](tree[(end_layer + i) * 2], tree[(end_layer + i) * 2 + 1])

        end_layer >>= 1

    return tree


def search(tree, query_start, query_end, nth_node, portion_start, portion_end, flag):
    # 구간을 벗어나는 경우
    if portion_end < query_start or query_end < portion_start:
        return None
    # 구간에 속하는 경우
    if query_start <= portion_start and portion_end <= query_end:
        return tree[nth_node]
    # 구간의 경계에 걸치는 경우
    middle = (portion_start + portion_end) // 2
    val1 = search(tree, query_start, query_end, nth_node * 2, portion_start, middle, flag)
    val2 = search(tree, query_start, query_end, nth_node * 2 + 1, middle + 1, portion_end, flag)

    if val1 is None:
        return val2
    if val2 is None:
        return val1
    if val1 > val2:
        if flag == 0:
            return val2
        else:
            return val1
    elif val2 > val1:
        if flag == 0:
            return val1
        else:
            return val2
    # val1 == val2
    else:
        return val1


if __name__ == '__main__':
    n_node, n_query = map(int, sys.stdin.readline().split())
    nodes = [int(sys.stdin.readline()) for _ in range(n_node)]
    end_layer = 1 << ceil(log2(len(nodes)))
    min_tree = inflate_tree(nodes, 0)   # 최소값 저장 트리
    max_tree = inflate_tree(nodes, 1)   # 최대값 저장 트리

    for _ in range(n_query):
        src, dst = map(int, sys.stdin.readline().split())
        print(search(min_tree, src, dst, 1, 1, end_layer, 0), search(max_tree, src, dst, 1, 1, end_layer, 1))
