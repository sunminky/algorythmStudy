# https://www.acmicpc.net/problem/1197
# 프림 알고리즘
import sys
import heapq

if __name__ == '__main__':
    n_node, n_edge = map(int, sys.stdin.readline().split())
    path = [dict() for _ in range(n_node)]
    visited = [False] * n_node
    queue = [(0, 0)]  # 비용, 노드
    answer = 0

    for _ in range(n_edge):
        _src, _dst, _dis = map(int, sys.stdin.readline().split())

        path[_src - 1][_dst - 1] = min(path[_src - 1].get(_dst - 1, 2147483647), _dis)
        path[_dst - 1][_src - 1] = min(path[_dst - 1].get(_src - 1, 2147483647), _dis)

    while queue:
        cur_cost, cur_node = heapq.heappop(queue)

        if visited[cur_node]:
            continue

        visited[cur_node] = True
        answer += cur_cost

        for _neigh in path[cur_node]:
            if visited[_neigh]:
                continue

            heapq.heappush(queue, (path[cur_node][_neigh], _neigh))

    print(answer)
