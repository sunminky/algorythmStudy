# https://www.acmicpc.net/problem/14567
import sys
from collections import deque

if __name__ == '__main__':
    n_subject, n_prerequisite = map(int, sys.stdin.readline().split())
    inbound = [0] * n_subject
    complete = [0] * n_subject
    outbound = [list() for _ in range(n_subject)]
    queue = deque()

    for _ in range(n_prerequisite):
        forehead, tail = map(int, sys.stdin.readline().split())
        outbound[forehead - 1].append(tail - 1)
        inbound[tail - 1] += 1

    for seq in range(n_subject):
        if inbound[seq]:
            continue
        queue.append(seq)

    for semester in range(1, n_subject + 1):
        new_queue = deque()
        while queue:
            sub = queue.popleft()
            complete[sub] = semester

            for neigh in outbound[sub]:
                inbound[neigh] -= 1

                if inbound[neigh] == 0:
                    new_queue.append(neigh)

        queue = new_queue

    print(" ".join(map(str, complete)))