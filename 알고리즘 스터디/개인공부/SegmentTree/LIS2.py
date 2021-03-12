#https://www.acmicpc.net/problem/12015
#세그먼트 트리로도 구현 가능

import sys
from math import ceil, log2


# 구간별 lis 최대 길이 저장 트리
def updateTree(tree, idx, value):
    while idx != 0:
        tree[idx] = max(tree[idx], value)
        idx >>= 1


def search(tree, query_end, nth_node, node_start, node_end) -> int:   #트리, 원하는 구간 끝, 노드 번호, 노드 구간 시작, 노드 구간 끝
    #구간이 포함되지 않는 경우
    if query_end <= node_start:
        return 0
    #구간이 포함되는 경우
    if node_end < query_end:
        return tree[nth_node]
    #구간이 경계에 걸쳐있는 경우
    middle = (node_start + node_end) // 2
    return max(search(tree, query_end, nth_node * 2, node_start, middle),
               search(tree, query_end, nth_node * 2 + 1, middle+1, node_end))


if __name__ == '__main__':
    n_number = int(sys.stdin.readline())
    numbers = sorted([[num, i] for i, num in enumerate(map(int, sys.stdin.readline().split()))], key=lambda x: x[0])
    height = ceil(log2(n_number))
    tree = [0 for _ in range(2 << height)]
    end_width = 1 << height

    prev_num = -1
    for n in numbers:
        value = search(tree, n[1] + 1, 1, 1, end_width)

        #이전과 같은 숫자가 아닌 경우
        if prev_num != n[0]:
            value += 1

        updateTree(tree, end_width + n[1], value)
        prev_num = n[0]

    print(tree[1])
