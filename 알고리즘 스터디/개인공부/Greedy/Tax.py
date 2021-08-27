# https://www.acmicpc.net/problem/13907
import sys
import heapq

if __name__ == '__main__':
    n_city, n_edge, times = map(int, sys.stdin.readline().split())
    src, dst = map(int, sys.stdin.readline().split())
    edge = [dict() for _ in range(n_city)]
    costs = [[1300001] * n_city for _ in range(n_city)]  # costs[i][j], i번째 도시까지 j의 간선으로 오는 최소비용
    costs_min = [[n_city, 1300001] for _ in range(n_city)]  # [최소비용의 간선 개수, 최소 비용]
    djik_queue = []

    for _ in range(n_edge):
        _src, _dst, _cost = map(int, sys.stdin.readline().split())

        edge[_src - 1][_dst - 1] = min(edge[_src - 1].get(_dst - 1, 1000), _cost)
        edge[_dst - 1][_src - 1] = min(edge[_dst - 1].get(_src - 1, 1000), _cost)

    # 다익스트라
    costs[src - 1][0] = 0
    costs_min[src - 1] = [0, 0]
    heapq.heappush(djik_queue, (0, 0, src - 1))  # 비용, 간선 개수, 현재 노드

    while djik_queue:
        cur_cost, edge_cnt, cur_node = heapq.heappop(djik_queue)

        # 도시가 n개 일 때 거칠 수 있는 간선의 최대 개수는 n - 1개
        if edge_cnt + 1 < n_city:
            for neigh in edge[cur_node].keys():
                # 최소비용의 간선보다 많은 간선 쓰면서 비용도 높으면 cut
                # 최소 비용의 간선보다 적은 간선 쓰는 경우(나중에 세금 오르면 최소 비용이 될 수 있음)
                if costs_min[neigh][0] > edge_cnt + 1:
                    # 최소 비용 갱신이 가능한 경우 갱신
                    if costs_min[neigh][1] > cur_cost + edge[cur_node][neigh]:
                        costs_min[neigh][0] = edge_cnt + 1
                        costs_min[neigh][1] = cur_cost + edge[cur_node][neigh]

                    if cur_cost + edge[cur_node][neigh] < costs[neigh][edge_cnt + 1]:
                        costs[neigh][edge_cnt + 1] = cur_cost + edge[cur_node][neigh]
                        heapq.heappush(djik_queue, (costs[neigh][edge_cnt + 1], edge_cnt + 1, neigh))

                # 최소 비용인 경우 갱신
                elif costs_min[neigh][1] > cur_cost + edge[cur_node][neigh]:
                    costs_min[neigh][1] = cur_cost + edge[cur_node][neigh]
                    costs_min[neigh][0] = edge_cnt + 1

                    if cur_cost + edge[cur_node][neigh] < costs[neigh][edge_cnt + 1]:
                        costs[neigh][edge_cnt + 1] = cur_cost + edge[cur_node][neigh]
                        heapq.heappush(djik_queue, (costs[neigh][edge_cnt + 1], edge_cnt + 1, neigh))

    # 출력
    answer_queue = []

    for i in range(n_city):
        if costs[dst - 1][i] != 1300001:
            answer_queue.append((costs[dst - 1][i], i))  # 최소비용, 간선개수

    time = 0
    min_val = 0
    print(min(answer_queue, key=lambda x: x[0])[0])
    for _ in range(times):
        time = int(sys.stdin.readline())
        queue_copy = answer_queue.copy()
        answer_queue = []
        min_val = [1300001, n_city]

        for e in queue_copy:
            # 최소비용의 간선보다 많은 간선 쓰면서 비용도 높으면 cut
            # 최소 비용의 간선보다 적은 간선 쓰는 경우(나중에 세금 오르면 최소 비용이 될 수 있음)
            if min_val[1] > e[1]:
                if min_val[0] > e[0]:
                    min_val[0] = e[0]
                    min_val[1] = e[1]

            # 최소 비용인 경우 갱신
            elif min_val[0] > e[0]:
                min_val[0] = e[0]
                min_val[1] = e[1]

            else:
                continue
            answer_queue.append((e[0] + time * e[1], e[1]))

        print(min(answer_queue, key=lambda x: x[0])[0])

    '''
    # 출력 (간단함)
    time = 0
    print(min(costs[dst - 1]))
    for _ in range(times):
        time = int(sys.stdin.readline())

        for i in range(n_city):
            if costs[dst - 1][i] != 1300001:
                costs[dst - 1][i] += i * time

        print(min(costs[dst - 1]))
    '''