# https://www.acmicpc.net/problem/14950
import sys
import heapq

if __name__ == '__main__':
    n_city, n_road, acc = map(int, sys.stdin.readline().split())
    path = {i: dict() for i in range(1, n_city + 1)}
    visited = [False] * (n_city + 1)
    queue = []
    answer = 0
    remain = n_city

    heapq.heappush(queue, (0, 1))   # 0번 노드에서 시작, (비용, 도착지)

    for _ in range(n_road):
        _src, _dst, _cost = map(int, sys.stdin.readline().split())
        path[_src][_dst] = min(_cost, path[_src].get(_dst, 30001))
        path[_dst][_src] = min(_cost, path[_dst].get(_src, 30001))

    while queue and remain:
        _cost, _cur_node = heapq.heappop(queue)

        if visited[_cur_node]:
            continue

        visited[_cur_node] = True
        answer += _cost
        remain -= 1

        for _neigh in path[_cur_node]:
            if visited[_neigh]:
                continue
            heapq.heappush(queue, (path[_cur_node][_neigh], _neigh))

    print(answer + acc * ((n_city - 2) * (n_city - 1)) // 2)
