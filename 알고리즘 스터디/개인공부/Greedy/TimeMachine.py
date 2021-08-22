# https://www.acmicpc.net/problem/11657
# 밸만포드 알고리즘
import sys

if __name__ == '__main__':
    n_node, n_edge = map(int, sys.stdin.readline().split())
    cost = [5000001] * n_node
    edge = [dict() for _ in range(n_node)]
    inf_loop = False

    for _ in range(n_edge):
        src, dst, _cost = map(int, sys.stdin.readline().split())
        edge[src - 1][dst - 1] = min(_cost, edge[src - 1].get(dst - 1, 5000001))

    # 벨만포드
    cost[0] = 0     # 출발지 -> 출발지 비용 : 0
    for _ in range(n_node - 1):
        for cur_node in range(n_node):
            if cost[cur_node] != 5000001:
                # 가중치 갱신
                for neigh in edge[cur_node].keys():
                    cost[neigh] = min(cost[neigh], cost[cur_node] + edge[cur_node][neigh])
    
    # 여기서 갱신이 일어나면 무한 음수 간선 존재하는 거임
    for cur_node in range(n_node):
        if cost[cur_node] != 5000001:
            # 가중치 갱신
            for neigh in edge[cur_node].keys():
                if cost[neigh] > cost[cur_node] + edge[cur_node][neigh]:
                    inf_loop = True
                    break

            if inf_loop:
                break

    if inf_loop:
        print(-1)
    else:
        # 비용 출력
        for i in range(1, n_node):
            if cost[i] == 5000001:
                print(-1)
            else:
                print(cost[i])
