# https://www.acmicpc.net/problem/17471
import sys
from collections import deque
from math import log2

n_node = int(sys.stdin.readline())
costs = tuple(map(int, sys.stdin.readline().split()))
neighbor = [None for _ in range(n_node)]
total = sum(costs)


def check(bit, ex_bit):
    acc = 0
    queue = deque([0])  # 1번 노드에서 시작
    visited = [False] * n_node

    visited[0] = True
    bit -= 1

    while queue:
        cur_node = queue.popleft()
        acc += costs[cur_node]

        for neigh in neighbor[cur_node]:
            if visited[neigh - 1]:
                continue
            if bit & (1 << (neigh - 1)):
                queue.append(neigh - 1)
                visited[neigh - 1] = True
                bit -= 1 << (neigh - 1)

    if bit:
        return total

    ex_acc = 0
    ex_node = int(log2(ex_bit & -ex_bit))
    ex_queue = deque([ex_node])

    visited[ex_node] = True
    ex_bit -= (1 << ex_node)

    while ex_queue:
        cur_node = ex_queue.popleft()
        ex_acc += costs[cur_node]

        for neigh in neighbor[cur_node]:
            if visited[neigh - 1]:
                continue
            if ex_bit & (1 << (neigh - 1)):
                ex_queue.append(neigh - 1)
                visited[neigh - 1] = True
                ex_bit -= 1 << (neigh - 1)

    if ex_bit:
        return total

    return abs(ex_acc - acc)


if __name__ == '__main__':
    answer = total
    max_bit = (1 << n_node) - 1

    for seq in range(n_node):
        _, *neigh = map(int, sys.stdin.readline().split())
        neighbor[seq] = neigh

    # 1을 항상 포함하는 경로 만들기
    for bit in range(1, max_bit, 2):
        answer = min(answer, check(bit, max_bit - bit))

    print(-1 if answer == total else answer)
