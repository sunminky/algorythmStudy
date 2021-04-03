# https://www.acmicpc.net/problem/11437
# https://www.acmicpc.net/problem/11438

import sys
from _collections import deque
from math import log2, ceil


class node:
    def __init__(self, layers):
        self.neighbor = []
        self.layer = -1
        self.parent = [0] * layers


def calc_layer(node_num, layer, parent, height):
    global nodes
    queue = deque()

    queue.append((node_num, layer, parent))

    while queue:
        c_node, c_layer, c_parent = queue.popleft()

        nodes[c_node].layer = c_layer
        nodes[c_node].parent[0] = c_parent

        for n in nodes[c_node].neighbor:
            if nodes[n].layer == -1:
                queue.append((n, c_layer + 1, c_node))
                
    #parent[i] == 2 ** i 번째 위에 있는 부모
    for i in range(1, height):
        for n in nodes:
            n.parent[i] = nodes[n.parent[i-1]].parent[i-1]  #2 ** 2 번째 부모의 2 ** 2번째 부모 == 자신의 2 ** 3 번째 부모


if __name__ == '__main__':
    global nodes

    n_node = int(sys.stdin.readline())
    node_height = ceil(log2(n_node))
    nodes = [node(node_height) for i in range(n_node)]

    for _ in range(n_node - 1):
        src, dst = tuple(map(int, sys.stdin.readline().split()))
        nodes[src - 1].neighbor.append(dst - 1)
        nodes[dst - 1].neighbor.append(src - 1)

    # 노드의 층 계산하기
    calc_layer(0, 0, 0, node_height)

    for _ in range(int(sys.stdin.readline())):
        node1, node2 = tuple(map(int, sys.stdin.readline().split()))

        if nodes[node1 - 1].layer > nodes[node2 - 1].layer:
            p_max = node1 - 1
            p_min = node2 - 1
        else:
            p_max = node2 - 1
            p_min = node1 - 1

        # 층 맞춰주기
        for i in range(node_height-1, -1, -1):
            if nodes[nodes[p_max].parent[i]].layer >= nodes[p_min].layer:
                p_max = nodes[p_max].parent[i]

        if p_max == p_min:
            print(p_max + 1)
        else:
            # 최소 공통 조상 찾기
            for i in range(node_height-1, -1, -1):
                if nodes[p_max].parent[i] != nodes[p_min].parent[i]:
                    p_max = nodes[p_max].parent[i]
                    p_min = nodes[p_min].parent[i]

            print(nodes[p_max].parent[0] + 1)
