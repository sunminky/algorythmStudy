# https://www.acmicpc.net/problem/13913

import sys


class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.next_node = None

    def chaining(self, child_node):
        self.next_node = child_node


if __name__ == '__main__':
    me, you = tuple(map(int, sys.stdin.readline().split()))
    boundary = max(me, you * 2)
    tree = [None for _ in range(boundary + 1)]
    queue = []
    cnt = 0

    tree[me] = Node(me, None)
    if me != you:
        queue.append(me)

    while queue:
        new_queue = []

        for n in queue:
            for op in [tree[n].value - 1, tree[n].value + 1, tree[n].value * 2]:
                if 0 <= op <= boundary:
                    if tree[op] is None:
                        tree[op] = Node(op, tree[n])
                        new_queue.append(op)

            if tree[you] is not None:
                new_queue = None
                break

        queue = new_queue
        cnt += 1

    print(cnt)

    #동생 위치까지 오는데 필요한 노드를 연결
    cur_node = tree[you]
    while cur_node.parent is not None:
        cur_node.parent.chaining(cur_node)
        cur_node = cur_node.parent

    cur_node = tree[me]
    while True:
        if cur_node.value == you:
            print(cur_node.value)
            break
        else:
            print(cur_node.value, end=" ")
        cur_node = cur_node.next_node
