# https://www.acmicpc.net/problem/10217
import sys

if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        n_airport, budget, n_ticket = map(int, sys.stdin.readline().split())
        edges = [list() for _ in range(n_airport)]
        cost = [[1000001] * (budget + 1) for _ in range(n_airport)]  # cost[a][b] a번 노드에 b 비용으로 갈 수 있는 최소거리
        answer = 1000001

        for _ in range(n_ticket):
            u, v, c, d = map(int, sys.stdin.readline().split())
            edges[u - 1].append([v - 1, c, d])

        cost[0][0] = 0  # 0번에서 비용 0 -> 시간 0

        for cur_budget in range(budget + 1):
            for node in range(n_airport):
                cur_time = cost[node][cur_budget]
                
                # 시간이 초과된 경우
                if cur_time == 1000001:
                    continue
                
                # 최소 도착시간 갱신
                if node == n_airport - 1:
                    answer = min(cur_time, answer)

                for v, c, d in edges[node]:
                    if cur_budget + c > budget or answer < cur_time + d:
                        continue
                    cost[v][cur_budget + c] = min(cost[v][cur_budget + c], cur_time + d)

        if answer == 1000001:
            print("Poor KCM")
        else:
            print(answer)
