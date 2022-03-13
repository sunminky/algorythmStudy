# https://www.acmicpc.net/problem/21924
# 프림 알고리즘
import sys
import heapq

if __name__ == '__main__':
    n_building, n_road = map(int, sys.stdin.readline().split())
    path = [dict() for _ in range(n_building)]
    visited = [False] * n_building
    queue = []
    remain = n_building     # 남은 도로의 수
    answer = 0
    total_cost = 0

    for _ in range(n_road):
        src, dst, cost = map(int, sys.stdin.readline().split())
        path[src - 1][dst - 1] = cost
        path[dst - 1][src - 1] = cost
        total_cost += cost
        
    # 0번 노드에서 시작
    heapq.heappush(queue, (0, 0))   # 비용, 노드

    while queue:
        cur_cost, cur_node = heapq.heappop(queue)

        if visited[cur_node]:
            continue

        visited[cur_node] = True
        answer += cur_cost
        remain -= 1

        for neigh in path[cur_node].keys():
            if visited[neigh]:
                continue
            heapq.heappush(queue, (path[cur_node][neigh], neigh))

    if remain:
        print(-1)
    else:
        print(total_cost - answer)
