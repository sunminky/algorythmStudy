#https://www.acmicpc.net/problem/1005

import sys
from collections import deque

if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        n_structure, n_rule = map(int, sys.stdin.readline().split())
        structure_cost = list(map(int, sys.stdin.readline().split()))
        path = [[] for _ in range(n_structure)]
        build_cost = [0] * n_structure
        queue = deque()

        for _ in range(n_rule):
            src, dst = map(int, sys.stdin.readline().split())

            path[dst-1].append(src-1)

        start = int(sys.stdin.readline())
        queue.append(start - 1)
        build_cost[start - 1] = structure_cost[start - 1]

        while queue:
            c_node = queue.popleft()

            for neigh in path[c_node]:
                if build_cost[c_node] + structure_cost[neigh] > build_cost[neigh]:
                    build_cost[neigh] = build_cost[c_node] + structure_cost[neigh]
                    queue.append(neigh)

        print(max(build_cost))