#https://www.acmicpc.net/problem/1135

import sys

if __name__ == '__main__':
    n_employee = int(sys.stdin.readline())
    boss = tuple(map(int, sys.stdin.readline().split()))
    employee = [[] for _ in range(n_employee)]  #맨 마지막은 우두머리

    for i in range(1, len(boss)):
        employee[boss[i]].append(i)

    cur_node = employee[0]
    depth = 0

    while cur_node:
        depth += len(cur_node)
        next_node = []

        for e in cur_node:
            next_node.extend(employee[e])

        cur_node = next_node
    
    print(depth)
