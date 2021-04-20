# https://www.acmicpc.net/problem/2631

import sys
from collections import deque
from bisect import bisect_left

if __name__ == '__main__':
    child = [int(sys.stdin.readline().rstrip()) for _ in range(int(sys.stdin.readline().rstrip()))]
    queue = deque(maxlen=len(child))

    for children in child:
        if queue:
            idx = bisect_left(queue, children)

            if idx == len(queue):
                queue.append(children)
            else:
                queue[idx] = children
        else:
            queue.append(children)

    print(len(child) - len(queue))
