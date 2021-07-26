# https://www.acmicpc.net/problem/3176
import sys
from math import ceil, log2
from collections import deque


class node:
    def __init__(self):
        self.layer = -1
        self.neighbor = []  # (노드, 비용)
        self.parent = [0] * MAX_HEIGHT  # i번째 노드 : 2**i 번째 부모
        self.minmax = [[1000000, 1] for _ in range(MAX_HEIGHT)]  # i번째 노드 : 2**i 번째 부모까지의 최소값, 최대값


def calc_layer():
    queue = deque()
    queue.append((0, 1))
    visited = [False] * N_NODE

    while queue:
        cur_node, cur_layer = queue.popleft()
        nodes[cur_node].layer = cur_layer
        visited[cur_node] = True

        for neigh, cost in nodes[cur_node].neighbor:
            if visited[neigh]:
                continue
            nodes[neigh].parent[0] = cur_node   # 바로 위의 부모세팅
            nodes[neigh].minmax[0][0] = nodes[neigh].minmax[0][1] = cost
            queue.append((neigh, cur_layer + 1))


# 부모 노드 계산
def calc_parent():
    for i in range(1, MAX_HEIGHT):
        for n in nodes:
            n.parent[i] = nodes[n.parent[i-1]].parent[i-1]  # 2 ** 2 번째 부모의 2 ** 2번째 부모 == 자신의 2 ** 3 번째 부모
            n.minmax[i][0] = min(n.minmax[i-1][0], nodes[n.parent[i-1]].minmax[i-1][0])
            n.minmax[i][1] = max(n.minmax[i - 1][1], nodes[n.parent[i - 1]].minmax[i - 1][1])


N_NODE = int(sys.stdin.readline())
MAX_HEIGHT = ceil(log2(N_NODE))
nodes = [node() for _ in range(N_NODE)]


if __name__ == '__main__':
    for _ in range(N_NODE - 1):
        src, dst, cost = map(int, sys.stdin.readline().split())
        nodes[src-1].neighbor.append((dst-1, cost))
        nodes[dst - 1].neighbor.append((src - 1, cost))

    calc_layer()
    calc_parent()

    for _ in range(int(sys.stdin.readline())):
        node1, node2 = map(lambda x: int(x) - 1, sys.stdin.readline().split())
        p_max = node1 if nodes[node1].layer > nodes[node2].layer else node2
        p_min = node2 if nodes[node1].layer > nodes[node2].layer else node1
        answer_min = 1000000
        answer_max = 1
        
        # 층 맞춰주기
        for i in range(MAX_HEIGHT - 1, -1, -1):
            if nodes[nodes[p_max].parent[i]].layer >= nodes[p_min].layer:
                answer_min = min(nodes[p_max].minmax[i][0], answer_min)
                answer_max = max(nodes[p_max].minmax[i][1], answer_max)
                p_max = nodes[p_max].parent[i]

        # 최소공통조상 구하기
        if p_max == p_min:
            pass
        else:
            for i in range(MAX_HEIGHT - 1, -1, -1):
                if nodes[p_max].parent[i] != nodes[p_min].parent[i]:
                    answer_min = min(nodes[p_max].minmax[i][0], nodes[p_min].minmax[i][0], answer_min)
                    answer_max = max(nodes[p_max].minmax[i][1], nodes[p_min].minmax[i][1], answer_max)
                    p_max = nodes[p_max].parent[i]
                    p_min = nodes[p_min].parent[i]

            answer_min = min(nodes[p_max].minmax[0][0], nodes[p_min].minmax[0][0], answer_min)
            answer_max = max(nodes[p_max].minmax[0][1], nodes[p_min].minmax[0][1], answer_max)
            p_max = nodes[p_max].parent[0]
            p_min = nodes[p_min].parent[0]

        print(answer_min, answer_max)
