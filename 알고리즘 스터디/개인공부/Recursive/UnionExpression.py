# https://www.acmicpc.net/problem/1717

import sys
sys.setrecursionlimit(10000000)


def getRoot(parent, node):
    if parent[node] == node:
        return parent[node]

    parent[node] = getRoot(parent, parent[node])
    return parent[node]


if __name__ == '__main__':
    n_node, n_operation = map(int, sys.stdin.readline().split())
    operation = [[*map(int, sys.stdin.readline().split())] for _ in range(n_operation)]  # 명령어, 집합1, 집합2
    parent = [i for i in range(n_node + 1)]

    for op, src, dst in operation:
        # 합치기
        if op == 0:
            p1 = getRoot(parent, src)
            p2 = getRoot(parent, dst)
            parent[p1] = parent[p2] = parent[src] = parent[dst] = min(p1, p2)
        # 조회하기
        else:
            p1 = getRoot(parent, src)
            p2 = getRoot(parent, dst)

            if p1 == p2:
                print("YES")
            else:
                print("NO")
