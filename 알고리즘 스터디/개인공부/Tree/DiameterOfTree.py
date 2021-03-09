# https://www.acmicpc.net/problem/1167
# https://www.quora.com/How-does-following-algorithm-for-finding-longest-path-in-tree-work

import sys
from collections import deque

n_node = int(sys.stdin.readline())


# 가장 먼 노드를 찾음
def farthest_node(node: int):
    global path
    queue = deque()
    visited = [False for _ in range(n_node)]
    max_val = 0
    max_node = node

    queue.append((node, 0))
    while queue:
        c_node, cost = queue.popleft()
        visited[c_node] = True

        # 가장 거리가 먼 노드를 갱신
        if cost > max_val:
            max_val = cost
            max_node = c_node

        for n_dst, n_cost in path[c_node]:
            if visited[n_dst] is False:
                queue.append((n_dst, n_cost + cost))

    return max_node, max_val


if __name__ == '__main__':
    global path
    path = [list() for _ in range(n_node)]  # [도착지, 비용]
    path = [[] for _ in range(n_node)]

    for _ in range(n_node):
        src, *p, _ = tuple(map(int, sys.stdin.readline().split()))

        for i in range(len(p) // 2):
            path[src - 1].append([p[i * 2] - 1, p[i * 2 + 1]])

    f_node1, _ = farthest_node(0)  # 임의의 노드에서 가장 먼 노드(트리를 펼쳤을 때 지름의 시작점이 되는 노드)를 찾음
    f_node2, distance = farthest_node(f_node1)  # 지름의 시작점이 되는 노드에서 가장 먼 노드(지름의 끝이 되는 노드)를 찾음

    print(distance)
