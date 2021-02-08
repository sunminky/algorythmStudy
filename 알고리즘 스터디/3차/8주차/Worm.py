#https://www.acmicpc.net/problem/2606

import sys

def search(current):
    global visited
    global cnt

    #이미 방문했던 경우
    if visited[current]:
        return

    #방문 안한 곳 탐색
    else:
        visited[current] = True
        for node in connections[current]:
            search(node)

    cnt += 1

if __name__ == '__main__':
    global connections
    global visited
    n_computer = int(sys.stdin.readline())
    visited = [False for _ in range(n_computer+1)]
    connections = [set() for _ in range(n_computer+1)]
    cnt = 0

    for _ in range(int(sys.stdin.readline())):
        node1, node2 = tuple(map(int, sys.stdin.readline().split()))
        connections[node1].add(node2)
        connections[node2].add(node1)

    search(1)
    print(cnt-1)