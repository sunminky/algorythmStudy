#https://www.acmicpc.net/problem/1197
#프림 알고리즘

import sys
from queue import PriorityQueue

if __name__ == '__main__':
    n_node, n_edge = tuple(map(int, sys.stdin.readline().split()))
    path = [list() for _ in range(n_node)]
    visited = [False for _ in range(n_node)]
    queue = PriorityQueue()
    cnt = n_node
    answer = 0

    for _ in range(n_edge):
        src, dst, cost = tuple(map(int, sys.stdin.readline().split()))
        path[src-1].append((dst-1, cost))
        path[dst-1].append((src-1, cost))
        
    queue.put((0, 0, 0))    #비용, 출발, 도착

    while not queue.empty():
        c_cost, c_src, c_dst = queue.get()

        if visited[c_dst]:
            continue
        else:
            visited[c_dst] = True
            answer += c_cost
            cnt -= 1
            if cnt == 0:
                break

        for next_dst, next_cost in path[c_dst]:
            if not visited[next_dst]:
                queue.put((next_cost, c_dst, next_dst))

    print(answer)
