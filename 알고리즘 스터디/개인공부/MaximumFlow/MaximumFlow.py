# https://www.acmicpc.net/problem/6086
import sys
from collections import deque

if __name__ == '__main__':
    edge_value = [dict() for _ in range(52)]  # [현재 유량, 최대 유량]
    answer = 0
    alpha_dict = dict(zip([chr(i) for i in range(65, 65 + 26)] + [chr(i) for i in range(97, 97 + 26)], range(52)))  # 출발지, 도착지 문자 매칭

    # 그래프 생성
    for _ in range(int(sys.stdin.readline())):
        src, dst, capacity = sys.stdin.readline().split()
        src = alpha_dict[src]
        dst = alpha_dict[dst]
        capacity = int(capacity)

        # 목적지와 도착지가 같은 간선이 여러개 존재할 경우 두 개를 하나의 파이프로 합침
        if edge_value[src].get(dst, False) is False:
            edge_value[src][dst] = [0, 0]
            edge_value[dst][src] = [0, 0]  # 음의 가중치를 위한 반대 간선 생성

        edge_value[src][dst][1] += capacity
        edge_value[dst][src][1] += capacity

    while True:
        queue = deque()
        queue.append(0)  # 시작점 넣어주기
        tracking = [None] * 52

        while queue:
            current_node = queue.popleft()

            for neigh in edge_value[current_node].keys():
                # 방문하지 않았고 최대 유량까지 아직 여유가 있을 때
                if tracking[neigh] is None and edge_value[current_node][neigh][1] > edge_value[current_node][neigh][0]:
                    queue.append(neigh)
                    tracking[neigh] = current_node

                    # Z에 도착한 경우 탐색 중지
                    if neigh == 25:
                        queue.clear()
                        break

        # 전부 탐색했는 데 Z에 도착하지 못함 (=더 이상 경로가 존재하지 않음)
        if tracking[25] is None:
            break

        avail_flow = 1000   # 찾은 경로로 최대로 흐를 수 있는 양
        # Z에서 A까지 추적
        cur_node = 25   # Z에서 부터 역추적

        # A에 도착할 때 까지 역추적
        while cur_node != 0:
            prev_node = tracking[cur_node]
            avail_flow = min(avail_flow, edge_value[prev_node][cur_node][1] - edge_value[prev_node][cur_node][0])
            cur_node = prev_node

        answer += avail_flow

        # A에서 Z 까지 추적
        cur_node = 25

        while cur_node != 0:
            prev_node = tracking[cur_node]
            edge_value[prev_node][cur_node][0] += avail_flow
            edge_value[cur_node][prev_node][0] -= avail_flow    # 반대 간선에 음의 가중치 더해줌
            cur_node = prev_node

    print(answer)
