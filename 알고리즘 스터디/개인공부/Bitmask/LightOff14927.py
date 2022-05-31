# https://www.acmicpc.net/problem/14927
import sys


def toggle(x, y, width, field):
    movement = ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1))

    for move in movement:
        new_x = x + move[0]
        new_y = y + move[1]

        # 바운더리
        if 0 <= new_x < width and 0 <= new_y < width:
            field[new_y][new_x] = not field[new_y][new_x]


def check(case, width, field) -> int:
    new_field = [field[seq][:] for seq in range(width)]
    cnt = 0

    # 첫번째 줄 토글
    for i in range(width):
        if case & (1 << i):
            toggle(i, 0, width, new_field)
            cnt += 1

    # 2 ~ 마지막 줄 까지 토글
    for row in range(1, width):
        for col in range(width):
            if new_field[row - 1][col]:
                toggle(col, row, width, new_field)
                cnt += 1

    return 401 if any(new_field[-1]) else cnt


if __name__ == '__main__':
    width = int(sys.stdin.readline())
    field = [[True if ch == '1' else False for ch in sys.stdin.readline().split()] for _ in range(width)]
    answer = 401

    for case in range(1 << width):
        answer = min(answer, check(case, width, field))

    print(answer if answer != 401 else -1)
