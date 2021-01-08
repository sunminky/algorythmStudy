# https://www.acmicpc.net/problem/1753

import sys
import heapq

MAX_COST = 300001


def print_cost(cost):
    for e in cost:
        if e == MAX_COST:
            print("INF")
        else:
            print(e)


if __name__ == '__main__':
    n_points, n_lines = map(int, sys.stdin.readline().rstrip().split())  # (정점의 개수, 간선의 개수)
    s_point = int(sys.stdin.readline().rstrip())  # 시작 정점
    weights = [[] for _ in range(n_points)]  # 간선들의 가중치 저장
    queue = []  # 탐색할 정점들을 대기시킬 장소
    costs = [MAX_COST for _ in range(n_points)]  # 시작 정점에서 비용들 저장

    ## init ##
    heapq.heappush(queue, (0, s_point-1))   # 출발 정점에서 부터 탐색시작
    costs[s_point - 1] = 0  # 출발 정점은 비용이 0

    for _ in range(n_lines):
        depart, *dest_cost = map(int, sys.stdin.readline().rstrip().split())  # 출발지, [도착지, 가중치]
        weights[depart - 1].append(dest_cost)

    while queue:  # 방문해야 할 정점이 없을 때 까지 탐색
        ## 큐에서 가중치가 제일 작은 정점부터 탐색 ##
        m_cost, m_point = heapq.heappop(queue)

        if m_cost >= costs[m_point]:
            ## m_point와 연결된 정점들 큐에 추가 ##
            for dst, cost in weights[m_point]:
                ## 비용 갱신 ##
                if costs[m_point] + cost < costs[dst - 1]:
                    costs[dst - 1] = costs[m_point] + cost
                    heapq.heappush(queue, (costs[dst - 1], dst - 1))

    print_cost(costs)
