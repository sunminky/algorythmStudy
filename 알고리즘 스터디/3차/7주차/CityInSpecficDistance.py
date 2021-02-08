#https://www.acmicpc.net/problem/18352

#다익스트리
#프루닝

import sys
import heapq

if __name__ == '__main__':
    city_num, road_num, target_distance, src_city = tuple(map(int, sys.stdin.readline().split()))   #도시의 개수, 길의 개수, 목표거리, 출발지
    neighbor = [[] for _ in range(city_num)]    #이웃노드 저장
    costs = [1000000 for _ in range(city_num)]  #출발지에서 각 노드까지 거리 저장
    queue = []

    for _ in range(road_num):
        src, dst = tuple(map(int, sys.stdin.readline().split()))
        neighbor[src-1].append(dst-1)

    costs[src_city - 1] = 0  # 출발지는 비용이 0
    heapq.heappush(queue, (0, src_city - 1))    #출발지를 큐에 넣음
    for n in neighbor[src_city-1]:
        heapq.heappush(queue, (1, n))   #출발지의 이웃노드를 큐에 넣음

    ### 다익스트라 ###
    while queue:
        h_cost, h_city = heapq.heappop(queue)

        if h_cost < costs[h_city]:
            costs[h_city] = h_cost
            for city in neighbor[h_city]:
                if costs[city] > h_cost+1 and h_cost+1 <= target_distance:  #거리 갱신 and 가지치기
                    heapq.heappush(queue, (h_cost+1, city))

    fulfill = False

    for seq, cost in enumerate(costs):
        if cost == target_distance:
            fulfill = True
            print(seq+1)

    if not fulfill:
        print(-1)
