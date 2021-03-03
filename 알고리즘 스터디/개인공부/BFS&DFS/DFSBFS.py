# https://www.acmicpc.net/problem/1260

import sys
from _collections import deque


def dfs(cur: int, path: list, visited: list):
    visited[cur] = True
    print(cur+1, end=" ")

    for n in path[cur]:
        if visited[n] is False:
            dfs(n, path, visited)


def bfs(cur: int, path: list, visited: list):
    queue = deque()
    queue.append(cur)
    visited[cur] = True

    while queue:
        c_node = queue.popleft()
        print(c_node+1, end=" ")

        for n in path[c_node]:
            if visited[n] is False:
                queue.append(n)
                visited[n] = True


if __name__ == '__main__':
    n_node, n_edge, src_node = tuple(map(int, sys.stdin.readline().split()))
    path = [list() for _ in range(n_node)]

    for _ in range(n_edge):
        src, dst = tuple(map(int, sys.stdin.readline().split()))
        path[src - 1].append(dst - 1)
        path[dst - 1].append(src - 1)

    for i in range(n_node):
        path[i].sort()

    dfs(src_node-1, path, [False for _ in range(n_node)])
    print()

    bfs(src_node-1, path, [False for _ in range(n_node)])
    print()
