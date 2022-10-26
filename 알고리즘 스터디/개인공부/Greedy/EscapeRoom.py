# https://www.acmicpc.net/problem/23743
import sys
import heapq

if __name__ == '__main__':
    n_room, n_warp = map(int, sys.stdin.readline().split())
    path = {i: dict() for i in range(1, n_room + 2)}
    visited = [False] * (n_room + 2)
    queue = []
    answer = 0
    remain = n_room

    for _ in range(n_warp):
        src, dst, cost = map(int, sys.stdin.readline().split())
        path[src][dst] = min(path[src].get(dst, 10000), cost)
        path[dst][src] = min(path[dst].get(src, 10000), cost)

    for seq, e in enumerate(map(int, sys.stdin.readline().split())):
        path[seq + 1][n_room + 1] = e
        path[n_room + 1][seq + 1] = e

    heapq.heappush(queue, (0, 1))   # 비용, 노드

    while queue and remain:
        cur_cost, cur_node = heapq.heappop(queue)

        if visited[cur_node]:
            continue

        answer += cur_cost
        visited[cur_node] = True

        for neigh in path[cur_node].keys():
            if visited[neigh]:
                continue

            heapq.heappush(queue, (path[cur_node][neigh], neigh))

    print(answer)
