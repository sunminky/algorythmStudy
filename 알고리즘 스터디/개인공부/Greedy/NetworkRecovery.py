# https://www.acmicpc.net/problem/2211
import sys
from queue import PriorityQueue

if __name__ == '__main__':
    n_computer, n_edge = map(int, sys.stdin.readline().split())
    edge = [dict() for _ in range(n_computer)]
    costs = [[10001, -1] for _ in range(n_computer)]  # [비용, 이전노드]
    queue = PriorityQueue()

    for _ in range(n_edge):
        computer1, computer2, cost = map(int, sys.stdin.readline().split())
        edge[computer1 - 1][computer2 - 1] = min(edge[computer1 - 1].get(computer2 - 1, 11), cost)
        edge[computer2 - 1][computer1 - 1] = min(edge[computer2 - 1].get(computer1 - 1, 11), cost)

    # 다익스트라
    costs[0][0] = 0    # 1번 노드 -> 1번 노드 : 비용 0
    queue.put((costs[0][0], 0))

    while not queue.empty():
        cur_cost, cur_node = queue.get()

        for neigh in edge[cur_node].keys():
            if cur_cost + edge[cur_node][neigh] < costs[neigh][0]:
                costs[neigh][0] = cur_cost + edge[cur_node][neigh]
                costs[neigh][1] = cur_node
                queue.put((costs[neigh][0], neigh))

    # 출력하기
    print(n_computer - 1)

    for i in range(1, n_computer):
        print(i + 1, costs[i][1] + 1)
