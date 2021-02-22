# https://www.acmicpc.net/problem/10217
# 메모리초과..

import sys
from queue import PriorityQueue

if __name__ == '__main__':
    n_testcase = int(sys.stdin.readline())

    for _ in range(n_testcase):
        n_airport, support, ticket = tuple(map(int, sys.stdin.readline().split()))
        path = [[] for _ in range(n_airport)]  # 경로 저장
        cost_table = [[10000001 for _ in range(support+1)] for _ in range(n_airport)] #cost_table[노드][비용] = 시간

        for _ in range(ticket):
            src, dst, cost, time = tuple(map(int, sys.stdin.readline().split()))
            path[src - 1].append((dst - 1, cost, time))

        queue = PriorityQueue()
        cost_table[0][0] = 0
        queue.put((0, 0, 0))    #시간, 비용, 노드

        while not queue.empty():
            c_time, c_cost, c_node = queue.get()

            if n_dst == n_airport - 1:
                break

            #이웃들 조사
            for n_dst, n_cost, n_time in path[c_node]:
                if c_cost + n_cost <= support:
                    if cost_table[n_dst][c_cost+n_cost] > c_time+n_time:
                        cost_table[n_dst][c_cost + n_cost] = c_time + n_time
                        queue.put((c_time + n_time, c_cost + n_cost, n_dst))

        answer = min(cost_table[-1])
        if answer != 10000001:
            print(min(cost_table[-1]))
        else:
            print("Poor KCM")