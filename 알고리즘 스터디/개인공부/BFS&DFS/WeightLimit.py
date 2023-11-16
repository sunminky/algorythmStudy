# https://www.acmicpc.net/problem/1939
import sys
import heapq

if __name__ == '__main__':
    n_island, n_bridge = map(int, sys.stdin.readline().split())
    path = [dict() for _ in range(n_island)]
    limit = [0] * n_island
    queue = []

    for _ in range(n_bridge):
        _island1, _island2, _limit = map(int, sys.stdin.readline().split())
        path[_island1 - 1][_island2 - 1] = max(path[_island1 - 1].get(_island2 - 1, 0), _limit)
        path[_island2 - 1][_island1 - 1] = max(path[_island2 - 1].get(_island1 - 1, 0), _limit)

    src, dst = map(int, sys.stdin.readline().split())

    heapq.heappush(queue, (-1000000001, src - 1))

    while queue:
        cur_cost, cur_island = heapq.heappop(queue)

        for _neigh in path[cur_island]:
            _limit = min(-cur_cost, path[cur_island][_neigh])

            if _limit > limit[_neigh]:
                limit[_neigh] = _limit
                heapq.heappush(queue, (-_limit, _neigh))

    print(limit[dst - 1])
