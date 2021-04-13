# https://www.acmicpc.net/problem/2263

import sys
sys.setrecursionlimit(1 << 25)

sys.stdin.readline()    #노드의 개수, 필요없음
in_order = [*map(int, sys.stdin.readline().split())]
post_order = [*map(int, sys.stdin.readline().split())]
element_idx = dict(zip(range(1, len(in_order) + 1), [-1] * len(in_order)))  # in 오더에 있는 요소들의 위치 저장


# in 오더에 있는 원소의 인덱스를 구함
def index(target):
    if element_idx[1] == -1:
        for i in range(len(element_idx)):
            element_idx[in_order[i]] = i

    return element_idx[target]


def search(in_ord_start, in_ord_end, post_ord_start, post_ord_end):
    # 가운데 노드 출력
    root = post_order[post_ord_end]
    root_idx = index(root) - in_ord_start

    print(root, end=" ")

    # 왼쪽 노드 출력
    if 0 <= root_idx - 1 and 0 <= root_idx - 1:
        # search(in_ord[:root_idx], post_ord[:root_idx])
        search(in_ord_start, in_ord_start + root_idx - 1, post_ord_start, post_ord_start + root_idx - 1)
    # 오른쪽 노드 출력
    if in_ord_start + root_idx + 1 <= in_ord_end and post_ord_start + root_idx <= post_ord_end - 1:
        # search(in_ord[root_idx + 1:], post_ord[root_idx:-1])
        search(in_ord_start + root_idx + 1, in_ord_end, post_ord_start + root_idx, post_ord_end - 1)


if __name__ == '__main__':
    search(0, len(in_order)-1, 0, len(post_order)-1)
