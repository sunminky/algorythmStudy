# https://www.acmicpc.net/problem/1162
import sys
import heapq

if __name__ == '__main__':
    n_city, n_road, n_pave = map(int, sys.stdin.readline().split())
    path = [dict() for _ in range(n_city)]  # 경로 저장
    costs = [[10000000000 if i else 0] * (n_pave + 1) for i in range(n_city)]
    visited = [[False] * (n_pave + 1) for i in range(n_city)]
    queue = [(0, 0, 0)]    # 비용, 도시, 포장횟수

    for _ in range(n_road):
        _city1, _city2, _cost = map(int, sys.stdin.readline().split())

        path[_city1 - 1][_city2 - 1] = min(path[_city1 - 1].get(_city2 - 1, 10000000000), _cost)
        path[_city2 - 1][_city1 - 1] = min(path[_city2 - 1].get(_city1 - 1, 10000000000), _cost)

    # 트릭
    if n_road <= n_pave:
        print(0)
        exit(0)

    while queue:
        cur_cost, cur_city, cur_pave = heapq.heappop(queue)

        if visited[cur_city][cur_pave]:
            continue

        visited[cur_city][cur_pave] = True

        for _neigh in path[cur_city].keys():
            _neigh_cost = path[cur_city][_neigh]
            # 현재 길 포장
            if cur_pave + 1 <= n_pave:
                if costs[_neigh][cur_pave + 1] > cur_cost:
                    costs[_neigh][cur_pave + 1] = cur_cost
                    # 큐에 추가
                    heapq.heappush(queue, (cur_cost, _neigh, cur_pave + 1))
            # 현재 길 포장 안함
            if costs[_neigh][cur_pave] > cur_cost + _neigh_cost:
                costs[_neigh][cur_pave] = cur_cost + _neigh_cost
                # 큐에 추가
                heapq.heappush(queue, (cur_cost + _neigh_cost, _neigh, cur_pave))

    print(min(costs[-1]))
