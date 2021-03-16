# https://www.acmicpc.net/problem/1766

import sys
from queue import PriorityQueue

if __name__ == '__main__':
    n_questions, n_associations = map(int, sys.stdin.readline().split())
    inbounds = [0 for _ in range(n_questions)]
    out_node = [[] for _ in range(n_questions)]
    queue = PriorityQueue()

    for _ in range(n_associations):
        pre, post = map(int, sys.stdin.readline().split())
        out_node[pre-1].append(post-1)
        inbounds[post-1] += 1

    for seq, cnt in enumerate(inbounds):
        if cnt == 0:
            queue.put(seq)

    while not queue.empty():
        c_node = queue.get()

        print(c_node + 1, end=" ")

        for neigh in out_node[c_node]:
            inbounds[neigh] -= 1

            if inbounds[neigh] == 0:
                queue.put(neigh)