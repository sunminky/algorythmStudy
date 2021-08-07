# https://www.acmicpc.net/problem/14442
import sys
from collections import deque

if __name__ == '__main__':
    height, width, pierce_cnt = tuple(map(int, sys.stdin.readline().split()))
    field = [sys.stdin.readline() for _ in range(height)]
    visited = [[[False] * (pierce_cnt + 1) for _ in range(width)] for _ in range(height)]
    queue = deque()
    movement = ((1, 0), (-1, 0), (0, 1), (0, -1))
    answer = -1

    visited[0][0] = [False] * (pierce_cnt + 1)
    queue.append((1, pierce_cnt, (0, 0))) #시작지점을 큐에 넣음, (비용, 남은 관통횟수, (x좌표, y좌표))

    while queue:
        cost, remain_pierce, cur_loc = queue.popleft()

        if (width-1, height-1) == cur_loc:
            answer = cost
            break

        for _move in movement:
            x = cur_loc[0] + _move[0]
            y = cur_loc[1] + _move[1]

            #바운더리
            if 0 <= x < width and 0 <= y < height:
                #벽을 부순 경우
                if field[y][x] == '1' and remain_pierce > 0:
                    #비용갱신
                    if not visited[y][x][remain_pierce]:
                        visited[y][x][remain_pierce] = True
                        queue.append((cost + 1, remain_pierce - 1, (x, y)))

                elif field[y][x] == '0':
                    # 비용갱신
                    if not visited[y][x][remain_pierce]:
                        visited[y][x][remain_pierce] = True
                        queue.append((cost + 1, remain_pierce, (x, y)))

    print(answer)
