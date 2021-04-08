# https://www.acmicpc.net/problem/3584

import sys
from collections import deque
from math import log2, ceil


class Node:
    def __init__(self, tree_height):
        self.layer = -1
        self.neighbor = []
        self.parent = [0] * tree_height  # parent[i]는 2 ** i번 째 부모


def calc_layer(nodes, root_node, tree_height):
    queue = deque()
    # 0번 노드가 항상 루트 노드가 되게 함
    queue.append((root_node, 0, root_node))  # 현재노드, 층 수, 부모노드

    while queue:
        c_node, c_layer, c_parent = queue.popleft()

        nodes[c_node].layer = c_layer
        nodes[c_node].parent[0] = c_parent

        for n in nodes[c_node].neighbor:
            if nodes[n].layer == -1:
                queue.append((n, c_layer + 1, c_node))

    for i in range(1, tree_height):
        for node in nodes:  # parent[i]는 2 ** i번 째 부모
            node.parent[i] = nodes[node.parent[i - 1]].parent[i - 1]  # 2 ** 2 번째 부모의 2 ** 2번째 부모 == 자신의 2 ** 3 번째 부모


if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        n_node = int(sys.stdin.readline())
        tree_height = ceil(log2(n_node))
        nodes = [Node(tree_height) for _ in range(n_node)]
        root_node_flag = [True] * n_node    # 루트노드 찾기

        for _ in range(n_node - 1):
            parent, child = map(int, sys.stdin.readline().split())

            nodes[parent - 1].neighbor.append(child - 1)
            nodes[child - 1].neighbor.append(parent - 1)
            root_node_flag[child - 1] = False   # 자식노드가 된 경험이 있는 노드는 루트노드 후보에서 탈락

        # 층 계산
        calc_layer(nodes, root_node_flag.index(True), tree_height)

        # 두 노드의 최소공통조상 구하기
        node1, node2 = map(int, sys.stdin.readline().split())

        # 층이 높은 노드 찾기
        if nodes[node1-1].layer > nodes[node2-1].layer:
            node_max = node1-1
            node_min = node2-1
        else:
            node_max = node2 - 1
            node_min = node1 - 1

        # 층 맞추기
        for i in range(tree_height-1, -1, -1):
            if nodes[node_min].layer <= nodes[nodes[node_max].parent[i]].layer:
                node_max = nodes[node_max].parent[i]

        # 둘 중 하나가 최소공통부모였던 경우
        if node_max == node_min:
            print(node_max + 1)
        else:
            # 공통부모 찾기
            for i in range(tree_height - 1, -1, -1):
                if nodes[node_max].parent[i] != nodes[node_min].parent[i]:
                    node_max = nodes[node_max].parent[i]
                    node_min = nodes[node_min].parent[i]

            print(nodes[node_max].parent[0] + 1)
