# https://www.acmicpc.net/problem/1197
# 크루스칼 알고리즘
import sys
from collections import deque

sys.setrecursionlimit(10 ** 9)


def union_find(parent: list, node: int) -> int:
    if parent[node] == node:
        return node
    else:
        parent[node] = union_find(parent, parent[node])
        return parent[node]


if __name__ == '__main__':
    n_node, n_edge = map(int, sys.stdin.readline().split())
    path = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n_edge)]
    parent = [i for i in range(n_node)]
    answer = 0
    queue = deque(sorted(path, key=lambda x: x[2]))

    while queue:
        _src, _dst, _cost = queue.popleft()
        p1 = union_find(parent, _src - 1)
        p2 = union_find(parent, _dst - 1)

        if p1 == p2:
            continue

        parent[p1] = parent[p2] = p1
        answer += _cost

    print(answer)
    print(parent)
