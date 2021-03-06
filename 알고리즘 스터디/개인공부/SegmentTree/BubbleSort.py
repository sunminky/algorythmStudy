# https://www.acmicpc.net/problem/1517
# 시간초과

import sys
from math import log2
from math import ceil

tree = None
number = None
N = int(sys.stdin.readline())


# 최대값 세그먼트 트리
def infalteTree(numbers):
    global tree
    global number

    number = list(map(int, sys.stdin.readline().split()))
    height = ceil(log2(len(number)))
    tree = [0 for _ in range(2 << height)]
    end_layer = 1 << height

    for i in range(len(number)):
        tree[end_layer + i] = number[i]

    end_layer >>= 1

    while end_layer != 0:
        for i in range(end_layer):
            tree[end_layer + i] = min(tree[(end_layer + i) << 1], tree[((end_layer + i) << 1) + 1])
        end_layer >>= 1


def search(portion_end, node_start, node_end, nth_node):  # 원하는 구간의 끝, 트리의 처음, 트리의 끝, 트리에 있는 노드번호
    global number
    global tree

    #구간을 벗어나는 경우
    if portion_end <= node_start:
        return 0
    #구간에 속하는 경우
    if node_end < portion_end:
        if number[portion_end-1] < tree[nth_node]:
            return node_end - node_start + 1
        if node_start == node_end:
            return 0
    #구간의 경계인 경우
    middle = (node_start + node_end) // 2
    return search(portion_end, node_start, middle, nth_node<<1) + search(portion_end, middle+1, node_end, (nth_node<<1)+1)


if __name__ == '__main__':
    infalteTree(number)
    swap_cnt = 0
    end_node = 1 << ceil(log2(N))

    for i in range(N):
        swap_cnt += search(i+1, 1, end_node, 1)

    print(swap_cnt)