# https://programmers.co.kr/learn/courses/30/lessons/49189
from collections import deque


def solution(n, edge):
    farthest = 0
    queue = deque()
    path = [list() for _ in range(n)]
    visited = [False] * n
    costs = [0] * n

    for _edge in edge:
        src, dst = _edge
        path[src - 1].append(dst - 1)
        path[dst - 1].append(src - 1)

    queue.append((0, 0))  # 0 번 노드, 0의 비용
    visited[0] = True
    costs[0] += 1

    while queue:
        cur_node, cur_cost = queue.popleft()
        farthest = max(farthest, cur_cost)

        for neigh in path[cur_node]:
            if visited[neigh]:
                continue
            queue.append((neigh, cur_cost + 1))
            visited[neigh] = True
            costs[cur_cost + 1] += 1

    return costs[farthest]


if __name__ == '__main__':
    solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])  # 3
