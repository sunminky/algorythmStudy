#https://www.acmicpc.net/problem/1922

import sys
from queue import PriorityQueue

if __name__ == '__main__':
    n_computers = int(sys.stdin.readline()) #컴퓨터의 개수
    n_connection = int(sys.stdin.readline())    #컴퓨터간의 연결 개수
    path = [set() for _ in range(n_computers)]  #연결 경로
    visited = [False for _ in range(n_computers + 1)]   #네트워크에 연결 됬는지 여부 저장
    queue = PriorityQueue()
    answer = 0  #네트워크 구축에 필요한 비용

    for _ in range(n_connection):
        src, dst, cost = tuple(map(int, sys.stdin.readline().split()))
        #양방향으로 입력해야 함
        path[src-1].add((dst-1, cost))
        path[dst - 1].add((src - 1, cost))

    queue.put((0, 0, 0))   # 연결비용, 시작노드, 도착노드

    while not queue.empty():
        c_cost, src_node, dst_node = queue.get()

        #이미 네트워크에 있는 노드라면 패스
        if visited[dst_node]:
            continue
        else:
            answer += c_cost
            visited[dst_node] = True

        #이웃 노드들과의 연결 큐에 넣음
        for n_dst, n_cost in path[dst_node]:
            if not visited[n_dst]:
                queue.put((n_cost, dst_node, n_dst))

    print(answer)