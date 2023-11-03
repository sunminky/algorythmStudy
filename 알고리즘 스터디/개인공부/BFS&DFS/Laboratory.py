# https://www.acmicpc.net/problem/14502
import sys
from collections import deque

if __name__ == '__main__':
    height, width = map(int, sys.stdin.readline().split())
    field = [list(map(int, sys.stdin.readline().split())) for _ in range(height)]
    virus_pos = []
    answer = 0
    movement = ((0, 1), (0, -1), (-1, 0), (1, 0))

    # 바이러스 위치 찾기
    for row in range(height):
        for col in range(width):
            if field[row][col] == 2:
                virus_pos.append((col, row))

    # 벽 3개 세우기
    for row1 in range(height):
        for col1 in range(width):
            if field[row1][col1] != 0:
                continue

            field[row1][col1] = 1

            for row2 in range(height):
                for col2 in range(width):
                    if field[row2][col2] != 0:
                        continue
                    if row1 == row2 and col1 == col2:
                        continue

                    field[row2][col2] = 1

                    for row3 in range(height):
                        for col3 in range(width):
                            if field[row3][col3] != 0:
                                continue
                            if row1 == row3 and col1 == col3:
                                continue
                            if row2 == row3 and col2 == col3:
                                continue

                            field[row3][col3] = 1

                            # BFS
                            queue = deque([e for e in virus_pos])
                            new_field = [[e2 for e2 in e1] for e1 in field]

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

                                    if new_field[new_y][new_x] == 0:
                                        new_field[new_y][new_x] = 2
                                        queue.append((new_x, new_y))

                            # 0칸 카운트
                            answer = max(answer, sum([e.count(0) for e in new_field]))

                            field[row3][col3] = 0

                    field[row2][col2] = 0

            field[row1][col1] = 0

    print(answer)
