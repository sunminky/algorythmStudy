# https://www.acmicpc.net/problem/2176
import sys
import heapq

if __name__ == '__main__':
    n_node, n_path = map(int, sys.stdin.readline().split())
    path = [dict() for _ in range(n_node)]
    queue = [(0, 1)]  # 비용, 노드
    visited = [False] * n_node
    costs = [10000001] * n_node
    path_cnt = [0] * n_node

    for _ in range(n_path):
        _src, _dst, _cost = map(int, sys.stdin.readline().split())
        path[_src - 1][_dst - 1] = _cost
        path[_dst - 1][_src - 1] = _cost

    # 노드 1(T)에서 부터의 거리 구하기
    while queue:
        _cost, _node = heapq.heappop(queue)

        if visited[_node]:
            continue

        visited[_node] = True
        costs[_node] = min(costs[_node], _cost)

        for _neigh in path[_node]:
            if visited[_neigh]:
                continue
            heapq.heappush(queue, (_cost + path[_node][_neigh], _neigh))

    # 노드 0에서 탐색 시작
    visited = [False] * n_node
    queue = [(-costs[0], 0)]   # 비용, 노드
    path_cnt[0] += 1
    visited[0] = True

    while queue:
        _cost, _node = heapq.heappop(queue)

        for _neigh in path[_node]:
            if -_cost <= costs[_neigh]:
                continue

            path_cnt[_neigh] += path_cnt[_node]

            if visited[_neigh]:
                continue

            visited[_neigh] = True
            heapq.heappush(queue, (-costs[_neigh], _neigh))

    print(path_cnt[1])
