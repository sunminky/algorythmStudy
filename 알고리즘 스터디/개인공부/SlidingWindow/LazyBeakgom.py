#https://www.acmicpc.net/problem/10025

import sys
from _collections import deque

if __name__ == '__main__':
    n_bucket, offset = tuple(map(int, sys.stdin.readline().split()))
    buckets = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(n_bucket)], key=lambda x: x[1])
    queue = deque()
    cur_pos = 0
    sum_ice = 0
    answer = 0

    for ice, pos in buckets:
        cur_pos = max(pos-offset, 0)    #현재 고려 중 인 얼음위치에서 offset만큼 떨어진 곳에 옴

        sum_ice += ice
        queue.append((pos, ice))

        while queue[0][0] < cur_pos - offset:
            sum_ice -= queue.popleft()[1]   #현재 위치에서 멀리 떨어진 얼음제거

        answer = max(answer, sum_ice)

    print(answer)