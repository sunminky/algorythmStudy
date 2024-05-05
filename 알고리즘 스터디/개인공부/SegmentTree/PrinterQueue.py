# https://www.acmicpc.net/problem/1966
# https://programmers.co.kr/learn/courses/30/lessons/42587
import sys
from collections import deque


def update(tree, nth_node, value):
    while nth_node < len(tree):
        tree[nth_node] += value
        nth_node += nth_node & -nth_node


def query(tree, start, end):
    r1 = r2 = 0

    while start:
        r1 += tree[start]
        start -= start & -start

    while end:
        r2 += tree[end]
        end -= end & -end

    return r2 - r1


if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        priority = [0] * 12
        n_doc, target = map(int, sys.stdin.readline().split())
        queue = deque()
        answer = 0

        for seq, _doc in enumerate(map(int, sys.stdin.readline().split())):
            queue.append((seq, _doc))
            update(priority, _doc, 1)

        while queue:
            _seq, cur_doc = queue.popleft()

            # 더 중요한 문서가 있는지 조사
            if query(priority, cur_doc, 11):
                queue.append((_seq, cur_doc))
                continue

            answer += 1
            update(priority, cur_doc, -1)

            if _seq == target:
                print(answer)
                break
