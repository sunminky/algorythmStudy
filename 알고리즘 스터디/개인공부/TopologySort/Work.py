# https://www.acmicpc.net/problem/2056

import sys
from collections import deque

if __name__ == '__main__':
    n_workers = int(sys.stdin.readline())
    times = [0] * n_workers #작업 별 걸리는 시간 저장
    cost = [0] * n_workers  #각 작업별 걸리는 시간
    out_node = [[] for _ in range(n_workers)]
    inbound = [0] * n_workers
    queue = deque()

    for i in range(n_workers):
        time, _, *post = map(int, sys.stdin.readline().split())
        times[i] = time

        for p in post:
            out_node[p-1].append(i)
            inbound[i] += 1

    for seq, cnt in enumerate(inbound):
        if cnt == 0:
            queue.append(seq)    #출발노드, 걸린 비용
    
    while queue:
        c_node = queue.popleft()
        cost[c_node] = cost[c_node] + times[c_node] #이전 작업중 가장 오래걸리는 작업 + 현재 작업 처리하는데 걸리는 시간

        for neigh in out_node[c_node]:
            inbound[neigh] -= 1
            cost[neigh] = max(cost[neigh], cost[c_node])

            if inbound[neigh] == 0:
                queue.append(neigh)

    print(max(cost))
