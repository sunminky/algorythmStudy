# https://www.acmicpc.net/problem/1939
import sys
import heapq

if __name__ == '__main__':
    n_island, n_bridge = map(int, sys.stdin.readline().split())
    island_dict = [dict() for _ in range(n_island)]
    costs = [0] * n_island
    queue = []

    for _ in range(n_bridge):
        src, dst, limit = map(int, sys.stdin.readline().split())

        island_dict[src - 1][dst - 1] = max(island_dict[src - 1].get(dst - 1, 0), limit)
        island_dict[dst - 1][src - 1] = max(island_dict[dst - 1].get(src - 1, 0), limit)

    start, end = map(int, sys.stdin.readline().split())
    heapq.heappush(queue, (-1000000000, start - 1))  # (노드, 비용)
    costs[start - 1] = 1000000000

    while queue:
        cur_cost, cur_node = heapq.heappop(queue)

        if cur_node == end - 1:
            break

        for _neigh in island_dict[cur_node].keys():
            if costs[_neigh] < min(island_dict[cur_node][_neigh], -cur_cost):
                costs[_neigh] = min(island_dict[cur_node][_neigh], -cur_cost)
                heapq.heappush(queue, (-costs[_neigh], _neigh))

    print(costs[end - 1])
