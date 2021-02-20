#https://www.acmicpc.net/problem/2636

import sys
from _collections import deque

#공기와 닿아있는 치즈들 녹임
def scalp(field : list) -> int:
    visited = [[False for _ in range(width)] for _ in range(height)]
    movement = ((1, 0), (-1, 0), (0, 1), (0, -1))
    queue = deque() #공기 범위 탐색 큐
    melt_cnt = 0    #녹인 치즈의 수

    queue.append((0, 0))
    visited[0][0] = True

    while queue:
        #탐색 시작
        x, y = queue.popleft()

        for _movement in movement:
            new_x = x + _movement[0]
            new_y = y + _movement[1]

            if 0 <= new_x < width and 0 <= new_y < height and visited[new_y][new_x] is False:
                visited[new_y][new_x] = True

                if field[new_y][new_x] == 0:
                    queue.append((new_x, new_y))
                else:   #치즈인 경우
                    field[new_y][new_x] = 0 #치즈를 녹임
                    melt_cnt += 1

    return melt_cnt


if __name__ == '__main__':
    height, width = tuple(map(int, sys.stdin.readline().split()))
    field = [list(map(int, sys.stdin.readline().split())) for _ in range(height)]
    cnt = prev = answer = 0

    while True:
        prev = answer
        answer = scalp(field)

        if answer == 0:
            print(cnt)
            print(prev)
            break

        cnt += 1
