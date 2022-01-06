# https://www.acmicpc.net/problem/19641
import sys
from collections import deque
sys.setrecursionlimit(100001)


class Node:
    def __init__(self):
        self.layer = -1
        self.neigh = None
        self.start = 0
        self.end = 0

    def set_range(self, parent_start, nodes):
        max_child_end = parent_start + 1

        for _neigh in self.neigh:
            # 내 자식이 아닌 경우 패스
            if nodes[_neigh].layer != self.layer + 1:
                continue
            max_child_end = max(max_child_end, nodes[_neigh].set_range(max_child_end, nodes))

        self.start = parent_start + 1
        self.end = max_child_end + 1

        return max_child_end + 1


if __name__ == '__main__':
    n_node = int(sys.stdin.readline())
    nodes = [Node() for _ in range(n_node)]
    root_node = -1
    layer_queue = deque()

    for _ in range(n_node):
        seq, *neigh = map(lambda x: int(x) - 1, sys.stdin.readline().split())
        nodes[seq].neigh = sorted(neigh[:-1])

    root_node = int(sys.stdin.readline()) - 1

    # 층 계산하기
    layer_queue.append((root_node, 0))  # 현재 노드, 층수
    nodes[root_node].layer = 0

    while layer_queue:
        cur_node, cur_layer = layer_queue.popleft()

        for _neigh in nodes[cur_node].neigh:
            # 이미 층이 계산된 경우 패스
            if nodes[_neigh].layer != -1:
                continue
            nodes[_neigh].layer = cur_layer + 1
            layer_queue.append((_neigh, cur_layer + 1))

    # 시작 ~ 끝 범위 정하기
    nodes[root_node].set_range(0, nodes)

    # 노드 출력
    for seq, n in enumerate(nodes):
        print(seq + 1, n.start, n.end)
