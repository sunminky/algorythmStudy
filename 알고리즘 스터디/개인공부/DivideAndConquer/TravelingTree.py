# https://www.acmicpc.net/problem/2263
import sys

sys.setrecursionlimit(1 << 25)

n_node = int(sys.stdin.readline())
in_order = [*map(int, sys.stdin.readline().split())]
post_order = [*map(int, sys.stdin.readline().split())]
in_order_dict = {e: seq for seq, e in enumerate(in_order)}


def search(in_ord_start, in_ord_end, post_ord_start, post_ord_end):
    root = post_order[post_ord_end]
    root_idx = in_order_dict[root] - in_ord_start

    print(root, end=" ")  # 가운데 노드 출력

    # 왼쪽 노드 출력
    if 0 <= root_idx - 1:
        search(in_ord_start, in_ord_start + root_idx - 1, post_ord_start, post_ord_start + root_idx - 1)
    # 오른쪽 노드 출력
    if in_ord_start + root_idx + 1 <= in_ord_end and post_ord_start + root_idx <= post_ord_end - 1:
        search(in_ord_start + root_idx + 1, in_ord_end, post_ord_start + root_idx, post_ord_end - 1)


if __name__ == '__main__':
    search(0, n_node - 1, 0, n_node - 1)
