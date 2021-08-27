# https://www.acmicpc.net/problem/1854
import sys
import heapq

if __name__ == '__main__':
    n_city, n_edge, kth = map(int, sys.stdin.readline().split())
    costs = [[-1000001] * kth for _ in range(n_city)]   # 0 ~ k번째 경로까지의 최대 힙
    edge = [list() for _ in range(n_city)]
    dijk_queue = []     # 다익스트라용 큐

    for _ in range(n_edge):
        src, dst, cost = map(int, sys.stdin.readline().split())
        edge[src - 1].append((dst - 1, cost))

    # 다익스트라
    heapq.heappop(costs[0])     # 1번 노드 -> 1번 노드 : 1번째 비용 0
    heapq.heappush(costs[0], 0)     # 1번 노드 -> 1번 노드 : 1번째 비용 0
    heapq.heappush(dijk_queue, (0, 0))  # 비용, 노드

    while dijk_queue:
        cur_cost, cur_node = heapq.heappop(dijk_queue)

        for neigh, n_cost in edge[cur_node]:
            if n_cost + cur_cost < -costs[neigh][0]:
                heapq.heappush(dijk_queue, (n_cost + cur_cost, neigh))

                heapq.heappop(costs[neigh])
                heapq.heappush(costs[neigh], -n_cost - cur_cost)

    for node in range(n_city):
        # k번재 경로가 존재하지 않는 경우
        if costs[node][0] == -1000001:
            print(-1)
        else:
            print(-costs[node][0])
