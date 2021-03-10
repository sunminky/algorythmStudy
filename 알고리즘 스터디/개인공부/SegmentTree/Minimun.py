#https://www.acmicpc.net/problem/10868

import sys
from math import ceil, log2


# 최소값 세그먼트 트리
def inflateTree(numbers):
    global tree

    height = ceil(log2(len(numbers)))
    tree = [1000000001 for _ in range(2 << height)]
    end_node = 1 << height

    for i in range(len(number)):
        tree[end_node + i] = number[i]

    end_node >>= 1
    while end_node != 0:
        for i in range(end_node):
            tree[end_node + i] = min(tree[(end_node + i) << 1], tree[((end_node + i) << 1) + 1])
        end_node >>= 1

    return 1 << height


def search(portion_start, portion_end, nth_node, node_start, node_end): #원하는 구간 시작점, 끝점, 현재 노드 번호, 구간에 포함되는 노드 시작점, 끝점
    global tree

    #구간에 속하지 않는 경우
    if portion_start > node_end or portion_end < node_start:
        return 1000000001
    #구간에 속하는 경우
    if portion_start <= node_start and node_end <= portion_end:
        return tree[nth_node]
    #구간의 경계에 걸치는 경우
    middle = (node_start + node_end) // 2
    return min(
        search(portion_start, portion_end, nth_node * 2, node_start, middle),
        search(portion_start, portion_end, nth_node * 2 + 1, middle + 1, node_end))


if __name__ == '__main__':
    n_number, n_query = map(int, sys.stdin.readline().split())
    number = [int(sys.stdin.readline()) for _ in range(n_number)]

    end_width = inflateTree(number)

    for _ in range(n_query):
        src, dst = map(int, sys.stdin.readline().split())
        print(search(src, dst, 1, 1, end_width))
