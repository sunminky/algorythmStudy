#https://www.acmicpc.net/problem/1715

import sys
import heapq

if __name__ == '__main__':
    shuffle_cnt = 0
    queue = []

    for _ in range(int(sys.stdin.readline())):
        heapq.heappush(queue, int(sys.stdin.readline()))

    while len(queue) != 1:
        x = heapq.heappop(queue)
        y = heapq.heappop(queue)

        shuffle_cnt += x + y
        heapq.heappush(queue, x+y)

    print(shuffle_cnt)