# https://www.acmicpc.net/problem/13334

import sys
import heapq

if __name__ == '__main__':
    pos = sorted([sorted(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))],
                 key=lambda x: x[1])
    rail = int(sys.stdin.readline())    #선로의 길이
    queue = []     # 역세권인 (사무실, 집)
    answer = 0

    for src, dst in pos:
        boundery = dst - rail   # 철로의 처음

        # 현재 철로에 속한다면 큐에 추가
        if src >= boundery:
            heapq.heappush(queue, src)

        # 현재 철로를 벗어난 곳이 있으면 제거
        while queue and queue[0] < boundery:
            heapq.heappop(queue)

        answer = max(answer, len(queue))

    print(answer)
