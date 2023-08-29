# https://www.acmicpc.net/problem/14725
import sys


class node:
    def __init__(self, name: str):
        self.name = name
        self.child = {}
        self.end = True

    def add_child(self, child: str) -> None:
        if child not in self.child.keys():
            self.child[child] = node(child)

        self.end = False


def append_node(path: list, node: node):
    # 기저조건
    if not path:
        return

    node.add_child(path[0])
    append_node(path[1:], node.child[path[0]])


def travel_node(node: node, depth):
    print('--' * depth, node.name, sep='')

    for neigh in sorted(node.child):
        travel_node(node.child[neigh], depth + 1)


if __name__ == '__main__':
    root = node('R')  # 루트노드

    for _ in range(int(sys.stdin.readline())):
        _, *path = sys.stdin.readline().rstrip().split()

        append_node(path, root)

    for neigh in sorted(root.child):
        travel_node(root.child[neigh], 0)
