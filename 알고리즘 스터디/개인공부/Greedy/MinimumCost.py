# https://www.acmicpc.net/problem/1916
import sys
from queue import PriorityQueue     # heapq 쓰면 더 빨라질 것

if __name__ == '__main__':
    n_city = int(sys.stdin.readline())
    n_edge = int(sys.stdin.readline())
    cost = [100000001] * n_city # 출발지 -> i번째 도시 비용 저장
    path = [dict() for _ in range(n_city)]  # 간선저장
    queue = PriorityQueue()

    for _ in range(n_edge):
        _src, _dst, _cost = map(int, sys.stdin.readline().split())
        path[_src - 1][_dst - 1] = min(path[_src - 1].get(_dst - 1, 100000001), _cost)

    src, dst = map(int, sys.stdin.readline().split())
    cost[src - 1] = 0   # 자기자신 -> 자기자신 : 비용 0
    queue.put((cost[src - 1], src - 1))

    # 다익스트라
    while not queue.empty():
        cur_cost, cur_node = queue.get()

        for neigh in path[cur_node].keys():
            if cur_cost + path[cur_node][neigh] < cost[neigh]:
                cost[neigh] = cur_cost + path[cur_node][neigh]
                queue.put((cost[neigh], neigh))

    print(cost[dst - 1])
