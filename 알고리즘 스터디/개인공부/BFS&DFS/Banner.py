# https://www.acmicpc.net/problem/14716
import sys
from collections import deque

row, col = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]


def dig(x, y):
    queue = deque([(x, y)])
    movement = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))  # 상, 우상, 우, 우하, 하, 좌하, 좌, 좌상

    while queue:
        cur_x, cur_y = queue.popleft()

        for _x, _y in movement:
            new_x = cur_x + _x
            new_y = cur_y + _y

            # 바운더리 체크
            if not 0 <= new_x < col:
                continue
            if not 0 <= new_y < row:
                continue

            if field[new_y][new_x] == 1:
                field[new_y][new_x] = 0
                queue.append((new_x, new_y))

    return 1


if __name__ == '__main__':
    cnt = 0

    for _row in range(row):
        for _col in range(col):
            if field[_row][_col] == 0:
                continue
            cnt += dig(_col, _row)

    print(cnt)
