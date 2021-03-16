#https://www.acmicpc.net/problem/2252

import sys
from collections import deque

if __name__ == '__main__':
    n_people, n_edge = map(int, sys.stdin.readline().split())
    outbounds = [0 for _ in range(n_people)]
    comein_node = [[] for _ in range(n_people)]
    queue = deque()
    answer = []

    for _ in range(n_edge):
        prev, later = map(int, sys.stdin.readline().split())

        outbounds[prev-1] += 1
        comein_node[later-1].append(prev-1)

    for seq, out_cnt in enumerate(outbounds):
        #뒤에 서 있는 사람이 없는 경우 큐에 추가
        if out_cnt == 0:
            queue.append(seq)

    while queue:
        c_node = queue.popleft()
        answer.append(str(c_node + 1))

        for neigh in comein_node[c_node]:
            outbounds[neigh] -= 1

            # 앞에 서 있는 사람들이 더 이상 뒤에 서있는 사람이 없게 될 경우 큐에 추가
            if outbounds[neigh] == 0:
                queue.append(neigh)

    print(" ".join(reversed(answer)))