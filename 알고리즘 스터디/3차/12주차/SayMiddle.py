#https://www.acmicpc.net/problem/1655

import sys
import heapq

if __name__ == '__main__':
    n_numbers = int(sys.stdin.readline())
    lower = []
    upper = []

    for _ in range(n_numbers):
        num = int(sys.stdin.readline())

        if len(lower) == len(upper):
            heapq.heappush(lower, -num)
        else:
            heapq.heappush(upper, num)

        if upper and -lower[0] > upper[0]:
            min_value = -heapq.heappop(lower)
            max_value = heapq.heappop(upper)

            heapq.heappush(lower, -max_value)
            heapq.heappush(upper, min_value)

        print(-lower[0])