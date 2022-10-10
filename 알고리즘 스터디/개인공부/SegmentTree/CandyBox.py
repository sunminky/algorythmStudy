# https://www.acmicpc.net/problem/2243
import sys
from math import ceil, log2


tree_len = 1 << ceil(log2(1000000))


def update(tree, sugar_content, n_candy):
    idx = tree_len + sugar_content - 1

    while idx:
        tree[idx] += n_candy
        idx >>= 1


def find(tree, nth_node, rank):
    # 바닥에 닿음
    if nth_node >= tree_len:
        print(nth_node - tree_len + 1)
        tree[nth_node] -= 1

        return nth_node >> 1
    else:
        portion1 = tree[nth_node * 2]

        if portion1 >= rank:
            idx = find(tree, nth_node * 2, rank)
        else:
            idx = find(tree, nth_node * 2 + 1, rank - portion1)

        tree[idx] -= 1

        return idx >> 1


if __name__ == '__main__':
    tree = [0] * (tree_len << 1)

    for _ in range(int(sys.stdin.readline())):
        op, *args = map(int, sys.stdin.readline().split())

        # 1인 경우 : 빼기
        if op == 1:
            rank = args[0]
            find(tree, 1, rank)
        # 2인 경우 : 추가하기
        else:
            sugar_content, n_candy = args
            update(tree, sugar_content, n_candy)
