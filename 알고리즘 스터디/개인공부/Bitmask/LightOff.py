# https://www.acmicpc.net/problem/14939
import sys
from copy import deepcopy


def toggle(x, y, field):
    movement = ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1))

    for move in movement:
        new_x = x + move[0]
        new_y = y + move[1]

        # 바운더리
        if 0 <= new_x < 10 and 0 <= new_y < 10:
            field[new_y][new_x] = not field[new_y][new_x]


def check(flag, field):
    cnt = 0
    new_field = deepcopy(field)

    # 첫째 줄 토글
    for col in range(10):
        # 버튼 눌림
        if flag & (1 << col):
            toggle(col, 0, new_field)
            cnt += 1

    # 2 ~ 10번째 줄 토글
    for row in range(1, 10):
        # 이전 줄의 같은 위치가 켜져있는 경우
        for col in range(10):
            if new_field[row - 1][col]:
                toggle(col, row, new_field)
                cnt += 1

    return 100 if any(new_field[-1]) else cnt


if __name__ == '__main__':
    field = [[True if e == "O" else False for e in sys.stdin.readline().rstrip()] for _ in range(10)]
    answer = 100

    for i in range(1 << 10):
        answer = min(answer, check(int(bin(i)[2:]), field))

    print(answer)
