# https://www.acmicpc.net/problem/7469
# 머지소트트리, 세그먼트 트리로도 해보기

import sys
from math import ceil, log2
from bisect import bisect_left


# 머지소트 트리 생성
def infalte_tree(nodes):
    height = ceil(log2(len(nodes)))
    tree = [list() for _ in range(2 << height)]
    end_layer = 1 << height

    for seq, num in enumerate(nodes):
        tree[end_layer + seq] = [num]

    end_layer >>= 1
    while end_layer:
        for i in range(end_layer):
            # 병합정렬
            arr1_idx = arr2_idx = 0

            while arr1_idx < len(tree[(end_layer + i) * 2]) and arr2_idx < len(tree[(end_layer + i) * 2 + 1]):
                if tree[(end_layer + i) * 2][arr1_idx] < tree[(end_layer + i) * 2 + 1][arr2_idx]:
                    tree[(end_layer + i)].append(tree[(end_layer + i) * 2][arr1_idx])
                    arr1_idx += 1
                else:
                    tree[(end_layer + i)].append(tree[(end_layer + i) * 2 + 1][arr2_idx])
                    arr2_idx += 1

            # 남은 원소 넣어주기
            if arr1_idx != len(tree[(end_layer + i) * 2]):
                for e in range(arr1_idx, len(tree[(end_layer + i) * 2])):
                    tree[(end_layer + i)].append(tree[(end_layer + i) * 2][e])

            # 남은 원소 넣어주기
            if arr2_idx != len(tree[(end_layer + i) * 2 + 1]):
                for e in range(arr2_idx, len(tree[(end_layer + i) * 2 + 1])):
                    tree[(end_layer + i)].append(tree[(end_layer + i) * 2 + 1][e])

        end_layer >>= 1

    return tree


# query_start ~ query_end 내 정렬 된 구간 반환
def search(tree, tree_len, query_start, query_end):
    result = []

    # bottom-up 방식
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
    n_node, n_query = map(int, sys.stdin.readline().split())
    nodes = [*map(int, sys.stdin.readline().split())]
    tree = infalte_tree(nodes)
    tree_len = 1 << ceil(log2(len(nodes)))

    for _ in range(n_query):
        src, dst, nth_node = map(int, sys.stdin.readline().split())

        max_val = 1000000001
        min_val = -1000000001

        # 이분탐색 시작
        while min_val < max_val:
            middle = (max_val + min_val) >> 1
            cnt = 0

            # middle 보다 작은 숫자 카운트
            for portion in search(tree, tree_len, src, dst):
                cnt += bisect_left(portion, middle)

            # middle이 너무 큼
            if cnt >= nth_node:
                max_val = middle

            # middle 이 너무 작음
            else:
                min_val = middle + 1

        print(max_val - 1)  # 이분 탐색이 정답 + 1에 묶여서 더이상 진행되지 않았기 때문에 1을 빼줘야 함
