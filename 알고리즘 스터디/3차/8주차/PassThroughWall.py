#https://www.acmicpc.net/problem/2206

import sys
from collections import deque

if __name__ == '__main__':
    height, width = tuple(map(int, sys.stdin.readline().split()))
    field = []
    visited = [[[False, False] for _ in range(width)] for _ in range(height)]
    queue = deque()
    movement = ((1, 0), (-1, 0), (0, 1), (0, -1))

    for _ in range(height):
        field.append(sys.stdin.readline().rstrip())

    visited[0][0][0] = visited[0][0][1] = True
    queue.append((1, False, (0, 0))) #시작지점을 큐에 넣음

    while queue:
        cost, removed, cur_loc = queue.popleft()

        if (width-1, height-1) == cur_loc:
            print(cost)
            exit(0)

        for _move in movement:
            x = cur_loc[0] + _move[0]
            y = cur_loc[1] + _move[1]

            #바운더리
            if 0 <= x < width and 0 <= y < height:
                #벽을 부순 경우
                if field[y][x] == '1' and removed is False:
                    #비용갱신
                    if not visited[y][x][1]:
                        visited[y][x][1] = True
                        queue.append((cost + 1, True, (x, y)))

                elif field[y][x] == '0':
                    # 비용갱신
                    if not visited[y][x][removed]:
                        visited[y][x][removed] = True
                        queue.append((cost + 1, removed, (x, y)))

    print(-1)
