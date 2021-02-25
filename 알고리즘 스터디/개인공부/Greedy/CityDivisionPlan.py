#https://www.acmicpc.net/problem/1647
#크루스칼

def RootRarent(node):
    global parent

    if parent[node] == node:
        return node
    parent[node] = RootRarent(parent[node])
    return parent[node]

import sys

if __name__ == '__main__':
    global parent
    n_node, n_edge = tuple(map(int, sys.stdin.readline().split()))
    path = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(n_edge)],
                  key=lambda x:x[2])
    parent = [i for i in range(n_node)]
    cnt = n_node-2  #n개의 노드를 모두 있는데 필요한 간선의 수(n -1) - (연결된 간선 중 가장 큰 간선)
    answer = 0  #n개의 노드를 모두 잇고 그중 가장 큰 간선을 뺀 값

    for p in path:
        #n-1개의 노드를 모두 연결함
        if cnt == 0:
            break

        p1 = RootRarent(p[0]-1)
        p2 = RootRarent(p[1]-1)

        #사이클인 경우
        if p1 == p2:
            continue

        parent[p1] = parent[p2] = min(p1, p2)
        answer += p[2]
        cnt -= 1

    print(answer)