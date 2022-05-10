# https://www.acmicpc.net/problem/1202
import sys
import heapq
from collections import deque

if __name__ == '__main__':
    n_jewel, n_backpack = map(int, sys.stdin.readline().split())
    jewel = deque(
        sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(n_jewel)], key=lambda x: (x[0], -x[1])))
    backpack = sorted([int(sys.stdin.readline()) for _ in range(n_backpack)])
    queue = []
    answer = 0

    for _backpack in backpack:
        while jewel and jewel[0][0] <= _backpack:
            weight, value = jewel.popleft()
            heapq.heappush(queue, (-value, weight))

        if queue:
            answer -= heapq.heappop(queue)[0]

    print(answer)
