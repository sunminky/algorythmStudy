# https://www.acmicpc.net/problem/2589

import sys
from collections import deque


def farthest(field, x, y):
    # 가장 먼곳 탐색 시작
    queue = deque()
    queue.append((x, y, 0))  # 현재 좌표, 카운트
    visited = [[False for _ in range(width)] for _ in range(height)]
    visited[y][x] = True
    cur_x = cur_y = cur_cnt = None

    while queue:
        cur_x, cur_y, cur_cnt = queue.popleft()

        if cur_x - 1 >= 0 and visited[cur_y][cur_x - 1] is False and field[cur_y][cur_x - 1] == 'L':
            queue.append((cur_x - 1, cur_y, cur_cnt+1))
            visited[cur_y][cur_x - 1] = True
        if cur_x + 1 < width and visited[cur_y][cur_x + 1] is False and field[cur_y][cur_x + 1] == 'L':
            queue.append((cur_x + 1, cur_y, cur_cnt+1))
            visited[cur_y][cur_x + 1] = True
        if cur_y - 1 >= 0 and visited[cur_y - 1][cur_x] is False and field[cur_y - 1][cur_x] == 'L':
            queue.append((cur_x, cur_y - 1, cur_cnt+1))
            visited[cur_y - 1][cur_x] = True
        if cur_y + 1 < height and visited[cur_y + 1][cur_x] is False and field[cur_y + 1][cur_x] == 'L':
            queue.append((cur_x, cur_y + 1, cur_cnt+1))
            visited[cur_y + 1][cur_x] = True

    #print(f"[{x}][{y}] -> [{cur_x}][{cur_y}] ... {cur_cnt}")
    return cur_x, cur_y, cur_cnt


if __name__ == '__main__':
    height, width = map(int, sys.stdin.readline().split())
    field = [sys.stdin.readline().rstrip() for _ in range(height)]
    answer = 0

    for row in range(height):
        for col in range(width):
            if field[row][col] == 'L':
                far_x, far_y, cnt = farthest(field, col, row)
                answer = max(answer, cnt)

    print(answer)
