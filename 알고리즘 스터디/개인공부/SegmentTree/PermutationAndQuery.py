# https://www.acmicpc.net/problem/13537
# https://www.acmicpc.net/problem/13544
# 머지소트트리, 세그먼트 트리로도 해보기

import sys
from math import ceil, log2
from bisect import bisect_right


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
    sys.stdin.readline()    # 노드의 개수, 필요없음
    nodes = [*map(int, sys.stdin.readline().split())]
    n_query = int(sys.stdin.readline())
    tree = infalte_tree(nodes)
    tree_len = 1 << ceil(log2(len(nodes)))

    for _ in range(n_query):
        # 문제 조건에 맞게 인덱스 변경
        src, dst, target = map(int, sys.stdin.readline().split())
        cnt = 0

        for portion in search(tree, tree_len, src, dst):
            cnt += len(portion) - bisect_right(portion, target)

        print(cnt)
