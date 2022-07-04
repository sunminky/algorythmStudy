# https://www.acmicpc.net/problem/7469
# 머지소트트리

import sys
from math import log2, ceil
from collections import deque
from bisect import bisect_left


# 머지소트 트리 생성
def inflate_tree(n_element, elements):
    height = ceil(log2(n_element))
    tree = [list()] * (2 << height)
    end_node = 1 << height

    for i in range(n_element):
        tree[end_node + i] = [elements[i]]

    end_node >>= 1
    while end_node:
        for i in range(end_node):
            tree[end_node + i] = list()

            # 머지소트 시작
            queue1 = deque(tree[(end_node + i) * 2])
            queue2 = deque(tree[(end_node + i) * 2 + 1])

            while queue1 and queue2:
                if queue1[0] > queue2[0]:
                    tree[end_node + i].append(queue2.popleft())
                else:
                    tree[end_node + i].append(queue1.popleft())

            while queue1:
                tree[end_node + i].append(queue1.popleft())

            while queue2:
                tree[end_node + i].append(queue2.popleft())

        end_node >>= 1

    return tree


def query(tree, tree_len, query_start, query_end):
    # bottom-up 방식
    result = []

    node_start = tree_len + query_start - 1
    node_end = tree_len + query_end

    while node_start < node_end:
        if node_start & 1:
            result.append(tree[node_start])
            node_start += 1

        if node_end & 1:
            result.append(tree[node_end - 1])
            node_end -= 1

        node_start >>= 1
        node_end >>= 1

    return result


if __name__ == '__main__':
    n_element, n_query = map(int, sys.stdin.readline().split())
    elements = tuple(map(int, sys.stdin.readline().split()))
    tree = inflate_tree(n_element, elements)
    end_length = 1 << ceil(log2(n_element))

    for _ in range(n_query):
        start, end, kth = map(int, sys.stdin.readline().split())
        data = query(tree, end_length, start, end)
        start, end = -1000000001, 1000000001

        while start < end:
            middle = (start + end) // 2
            cnt = 0

            for e in data:
                cnt += bisect_left(e, middle)

            if cnt >= kth:
                end = middle
            else:
                start = middle + 1

        print(start - 1)
