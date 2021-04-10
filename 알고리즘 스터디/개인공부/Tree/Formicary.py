# https://www.acmicpc.net/problem/14725

import sys


class node:
    def __init__(self, value):
        self.value = value
        self.child = dict()

    # 자식 노드 반환
    def chaining(self, value):
        if self.child.get(value, False) is False:
            self.child[value] = node(value)
        return self.child[value]    # 자식 노드 반환

    # 개미굴 탐색
    def traveling(self, layer):
        # 루트노드가 아니면 현재 개미굴에 있는 음식 출력
        if layer != -1:
            print(f"{'--' * layer}{self.value}")

        for child_node in sorted(self.child.keys()):
            self.child[child_node].traveling(layer+1)


if __name__ == '__main__':
    root_node = node(None)

    for _ in range(int(sys.stdin.readline())):
        _, *foods = sys.stdin.readline().split()
        
        # 음식 위치 저장
        c_node = root_node
        for food in foods:
            c_node = c_node.chaining(food)

    # 개미굴 출력
    root_node.traveling(-1)
