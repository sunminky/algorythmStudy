# https://www.acmicpc.net/problem/1005

import sys
from collections import deque

if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        n_structure, n_rule = map(int, sys.stdin.readline().split())
        costs = tuple(map(int, sys.stdin.readline().split()))
        waiting = [0] * n_structure
        outbound = [list() for _ in range(n_structure)]
        inbound_cnt = [0] * n_structure
        queue = deque()

        for _ in range(n_rule):
            ancestor, descendant = map(int, sys.stdin.readline().split())

            outbound[ancestor - 1].append(descendant - 1)
            inbound_cnt[descendant - 1] += 1

        for node in range(n_structure):
            if inbound_cnt[node] == 0:
                queue.append(node)
                waiting[node] = costs[node]

        while queue:
            cur_node = queue.popleft()

            for neigh in outbound[cur_node]:
                inbound_cnt[neigh] -= 1
                waiting[neigh] = max(waiting[neigh], waiting[cur_node] + costs[neigh])

                if inbound_cnt[neigh] == 0:
                    queue.append(neigh)

        print(waiting[int(sys.stdin.readline()) - 1])
