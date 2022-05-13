# https://www.acmicpc.net/problem/1012
import sys
from collections import deque

if __name__ == '__main__':
    movement = ((1, 0), (-1, 0), (0, 1), (0, -1))

    for _ in range(int(sys.stdin.readline())):
        width, height, n_pos = map(int, sys.stdin.readline().split())
        cabbage_pos = [tuple(map(int, sys.stdin.readline().split()))for _ in range(n_pos)]
        answer = 0
        field = [[False for _ in range(width)] for _ in range(height)]

        for pos in cabbage_pos:
            field[pos[1]][pos[0]] = True

        for pos in cabbage_pos:
            cnt = 0

            if field[pos[1]][pos[0]]:
                queue = deque([pos])
                field[pos[1]][pos[0]] = False
                answer += 1

                while queue:
                    cur_x, cur_y = queue.popleft()

                    for _move in movement:
                        new_x = cur_x + _move[0]
                        new_y = cur_y + _move[1]

                        # 바운더리 체크
                        if not 0 <= new_x < width:
                            continue
                        if not 0 <= new_y < height:
                            continue

                        if field[new_y][new_x]:
                            queue.append((new_x, new_y))

                        field[new_y][new_x] = False

        print(answer)
