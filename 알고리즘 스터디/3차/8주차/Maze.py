#https://www.acmicpc.net/problem/2178

import sys
import heapq

if __name__ == '__main__':
    height, width = tuple(map(int, sys.stdin.readline().split()))
    maze = [sys.stdin.readline().rstrip() for _ in range(height)]
    cost = [[10001 for _ in range(width)] for _ in range(height)]
    queue = []

    cost[0][0] = 1
    heapq.heappush(queue, (cost[0][0], 0, 0))   #cost, x, y

    x = y = 0

    while not (x == width-1 and y == height-1):
        c_cost, x, y = heapq.heappop(queue)

        # 위
        if y + 1 != height and int(maze[y + 1][x]) and c_cost + 1 < cost[y + 1][x]:
            cost[y + 1][x] = c_cost + 1
            heapq.heappush(queue, (cost[y + 1][x], x, y+1))
        # 아래
        if y - 1 != -1 and int(maze[y - 1][x]) and c_cost + 1 < cost[y - 1][x]:
            cost[y - 1][x] = c_cost + 1
            heapq.heappush(queue, (cost[y - 1][x], x, y - 1))
        # 우
        if x + 1 != width and int(maze[y][x + 1]) and c_cost + 1 < cost[y][x + 1]:
            cost[y][x + 1] = c_cost + 1
            heapq.heappush(queue, (cost[y][x + 1], x + 1, y))
        # 좌
        if x - 1 != -1 and int(maze[y][x - 1]) and c_cost + 1 < cost[y][x - 1]:
            cost[y][x - 1] = c_cost + 1
            heapq.heappush(queue, (cost[y][x - 1], x - 1, y))

    print(cost[-1][-1])