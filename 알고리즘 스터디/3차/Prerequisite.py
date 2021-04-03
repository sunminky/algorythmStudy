# https://www.acmicpc.net/problem/14567

import sys
from collections import deque

if __name__ == '__main__':
    n_subject, n_contraint = map(int, sys.stdin.readline().split())
    inbound = [0] * n_subject
    outbound = [[] for _ in range(n_subject)]
    answer = [1] * n_subject
    queue = deque()

    for _ in range(n_contraint):
        pre, post = map(int, sys.stdin.readline().split())
        inbound[post-1] += 1
        outbound[pre-1].append(post-1)

    # 진입차수가 0인 노드 큐에 추가
    for i in range(n_subject):
        if inbound[i] == 0:
            queue.append(i)

    while queue:
        c_node = queue.popleft()

        for n in outbound[c_node]:
            inbound[n] -= 1
            answer[n] = max(answer[n], answer[c_node] + 1)

            if inbound[n] == 0:
                queue.append(n)

    print(" ".join(map(str, answer)))
