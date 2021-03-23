# https://www.acmicpc.net/problem/6549
# https://www.acmicpc.net/problem/1725
# https://www.acmicpc.net/blog/view/12

import sys
from math import log2, ceil


# 구간별 최소 높이의 인덱스를 저장하는 트리
def inflate_tree(block):
    height = ceil(log2(len(block)))
    tree = [-1 for _ in range(2 << height)]
    end_node = 1 << height

    for i in range(len(block)):
        tree[end_node + i] = i

    end_node >>= 1
    while end_node != 0:
        for i in range(end_node):
            if tree[(end_node + i) * 2] == -1:
                tree[(end_node + i)] = tree[(end_node + i) * 2 + 1]
            elif tree[(end_node + i) * 2 + 1] == -1:
                tree[(end_node + i)] = tree[(end_node + i) * 2]
            else:
                if block[tree[(end_node + i) * 2]] > block[tree[(end_node + i) * 2 + 1]]:
                    tree[(end_node + i)] = tree[(end_node + i) * 2 + 1]
                else:
                    tree[(end_node + i)] = tree[(end_node + i) * 2]

        end_node >>= 1

    return tree


def search(tree, block, query_start, query_end, nth_node, portion_start, portion_end):
    # 범위를 벗어나는 경우
    if portion_end < query_start or query_end < portion_start:
        return -1
    # 범위 내에 있는 경우
    elif query_start <= portion_start and portion_end <= query_end:
        return tree[nth_node]
    # 구간의 경계에 걸친 경우
    else:
        middle = (portion_start + portion_end) // 2
        idx1 = search(tree, block, query_start, query_end, nth_node << 1, portion_start, middle)
        idx2 = search(tree, block, query_start, query_end, (nth_node << 1) + 1, middle + 1, portion_end)

        # 구간을 벗어난 경우 처리
        if idx1 == -1:
            return idx2
        elif idx2 == -1:
            return idx1
        # idx1번째 블럭이 idx2번째 블럭보다 높은 경우
        elif block[idx1] > block[idx2]:
            return idx2
        else:
            return idx1


if __name__ == '__main__':
    while True:
        _, *blocks = map(int, sys.stdin.readline().split())

        # 0이면 종료
        if not blocks:
            break

        tree = inflate_tree(blocks)

        print(search(tree, blocks, 4, 4, 1, 1, len(blocks)))
        print(tree)
