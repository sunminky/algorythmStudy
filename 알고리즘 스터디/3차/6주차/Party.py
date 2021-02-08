# https://www.acmicpc.net/problem/1238

import sys
import heapq

MAX_COST = 1000000

def dijkstra(nodes, weights, start_node) -> list:
    queue = []  #탐색 큐
    costs = [MAX_COST for _ in range(nodes)]  #각 노드까지의 거리
    
    heapq.heappush(queue, (0, start_node-1))  #시작노드를 탐색큐에 추가
    costs[start_node-1] = 0

    while queue:
        m_time, m_node = heapq.heappop(queue)

        if costs[m_node] >= m_time:
            for dst, time in weights[m_node]:
                if costs[dst] >= time + m_time:
                    costs[dst] = time + m_time
                    heapq.heappush(queue, (costs[dst], dst))

    return costs


if __name__ == '__main__':
    n_students, n_paths, occasion = map(int, sys.stdin.readline().rstrip().split())  # 학생이 사는 마을 수, 길의 개수, 행사장소
    way_to_occasion = [[] for _ in range(n_students)]  # 집에서 파티장으로 가는 경로 저장
    way_to_home = [[] for _ in range(n_students)]  # 파티장에서 집으로 가는 경로 저장

    for _ in range(n_paths):
        src, dst, cost = map(int, sys.stdin.readline().rstrip().split())  # 출발지, 도착지, 소요시간
        way_to_occasion[src-1].append((dst-1, cost))
        way_to_home[dst-1].append((src-1, cost))

    solution = [dijkstra(n_students, way_to_occasion, occasion), dijkstra(n_students, way_to_home, occasion)]
    print(max([solution[0][seq]+solution[1][seq] for seq in range(len(solution[0]))]))