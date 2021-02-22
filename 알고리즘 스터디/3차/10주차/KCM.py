#https://www.acmicpc.net/problem/10217
#메모리초과..
import sys
import heapq

if __name__ == '__main__':
    n_testcase = int(sys.stdin.readline())

    for _ in range(n_testcase):
        n_airport, support, ticket = tuple(map(int, sys.stdin.readline().split()))
        path = [[] for _ in range(n_airport)]   #경로 저장
        cost_table = [[support+1 for _ in range(support + 1)] for _ in range(n_airport)]    #각 노드별 소요시간 : 비용 저장

        for _ in range(ticket):
            src, dst, cost, time = tuple(map(int, sys.stdin.readline().split()))
            path[src-1].append((dst-1, cost, time))

        queue = []
        cost_table[0][0] = 0    #소요시간 0으로 1번 노드가는 비용 : 0
        heapq.heappush(queue, (0, 0, 0))   #(시간, 비용, 노드)
        #다익스트라
        while queue:
            c_time, c_cost, c_node = heapq.heappop(queue)

            for n_dst, n_time, n_cost in path[c_node]:
                if c_time + n_time <= support:
                    if cost_table[n_dst][c_time + n_time] > c_cost + n_cost:
                        cost_table[n_dst][c_time + n_time] = c_cost + n_cost
                        heapq.heappush(queue, (c_time + n_time, c_cost + n_cost, n_dst))

        answer = min(cost_table[-1])

        if answer == support + 1:
            print('Poor KCM')
        else:
            print(answer)