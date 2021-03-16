# https://www.acmicpc.net/problem/2623

import sys
from collections import deque

if __name__ == '__main__':
    n_singer, n_pd = map(int, sys.stdin.readline().split())
    inbound = [0 for _ in range(n_singer)]
    out_node = [[] for _ in range(n_singer)]
    queue = deque()
    answer = []

    for _ in range(n_pd):
        _, *singer = map(int, sys.stdin.readline().split())

        for i in range(1, len(singer)):
            out_node[singer[i-1]-1].append(singer[i]-1)
            inbound[singer[i]-1] += 1

    for seq, cnt in enumerate(inbound):
        if cnt == 0:
            queue.append(seq)

    while queue:
        c_node = queue.popleft()

        answer.append(c_node + 1)

        for neigh in out_node[c_node]:
            inbound[neigh] -= 1

            if inbound[neigh] == 0:
                queue.append(neigh)

    if len(answer) != n_singer:
        print(0)
    else:
        for s in answer:
            print(s)
