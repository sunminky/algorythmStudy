# https://www.acmicpc.net/problem/16953
import sys
from collections import deque

if __name__ == '__main__':
    src, target = map(int, sys.stdin.readline().split())
    queue = deque([(src, 1)])

    while queue:
        current, times = queue.popleft()

        if current > target:
            continue

        if current == target:
            print(times)
            break

        queue.append((current * 2, times + 1))
        queue.append((current * 10 + 1, times + 1))
    else:
        print(-1)
