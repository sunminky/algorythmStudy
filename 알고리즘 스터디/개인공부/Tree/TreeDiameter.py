# https://www.acmicpc.net/problem/1967

import sys
from _collections import deque

n_node = int(sys.stdin.readline())


# 가장 먼노드를 찾는 함수
def farthest_node(node: int):
    global path
    visited = [False for _ in range(n_node)]
    queue = deque()
    max_val = 0
    max_node = 0

    queue.append((node, 0))    #도착지, 비용

    while queue:
        c_node, cost = queue.popleft()

        visited[c_node] = True

        #가장 먼 노드를 발견하면 갱신
        if max_val < cost:
            max_val = cost
            max_node = c_node

        for neigh, n_cost in path[c_node]:
            if visited[neigh] is False:
                queue.append((neigh, cost + n_cost))

    return max_node, max_val


if __name__ == '__main__':
    global path
    path = [[] for _ in range(n_node)]

    for _ in range(n_node - 1):
        src, dst, weight = tuple(map(int, sys.stdin.readline().split()))
        path[src - 1].append((dst - 1, weight))
        path[dst - 1].append((src - 1, weight))

    f_node1, _ = farthest_node(0)   #임의의 한점에서 가장 먼 노드(지름의 시작점)를 찾음
    f_node2, distance = farthest_node(f_node1)  #지름의 시작점에서 지름의 끝점(지름의 시작점에서 가장 멈)을 찾음

    print(distance)
