#https://meet.google.com/ovw-ympa-hjp?pli=1&authuser=1

import sys
sys.setrecursionlimit(99999)


class node:
    def __init__(self, sequence):
        self.sequence = sequence
        self.neighbor = []
        self.layer = -1
        self.parent = sequence

    def chaining(self, neigh):
        self.neighbor.append(neigh)


def calc_layer(node, layer, parent):
    global nodes

    if nodes[node].layer != -1:
        return

    nodes[node].layer = layer
    nodes[node].parent = parent

    for n in nodes[node].neighbor:
        calc_layer(n, layer+1, node)


if __name__ == '__main__':
    global nodes

    n_node = int(sys.stdin.readline())
    nodes = [node(i) for i in range(n_node)]

    for _ in range(n_node-1):
        src, dst = tuple(map(int, sys.stdin.readline().split()))
        nodes[src-1].chaining(dst-1)
        nodes[dst-1].chaining(src-1)
        
    #노드의 층 계산하기
    calc_layer(0, 0, 0)

    n_query = int(sys.stdin.readline())

    for _ in range(n_query):
        node1, node2 = tuple(map(int, sys.stdin.readline().split()))

        if nodes[node1-1].layer > nodes[node2-1].layer:
            p_max = node1-1
            p_min = node2-1
        else:
            p_max = node2-1
            p_min = node1-1

        # 층 맞춰주기
        for _ in range(nodes[p_max].layer - nodes[p_min].layer):
            p_max = nodes[p_max].parent

        while p_max != p_min:
            p_max = nodes[p_max].parent
            p_min = nodes[p_min].parent

        print(p_max + 1)
