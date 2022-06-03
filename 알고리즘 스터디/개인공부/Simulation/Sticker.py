# https://www.acmicpc.net/problem/18808
import sys


def rotate(sticker):
    width = len(sticker[0])
    height = len(sticker)
    new_sticker = [[0] * height for _ in range(width)]

    for row in range(height):
        for col in range(width):
            new_sticker[col][height - row - 1] = sticker[row][col]

    return new_sticker


def fit(row, col, sticker, field) -> bool:
    for _row in range(len(sticker)):
        for _col in range(len(sticker[_row])):
            if sticker[_row][_col]:
                # 바운더리
                if not 0 <= _row + row < len(field):
                    return False
                if not 0 <= _col + col < len(field[_row]):
                    return False
                # 자리 체크
                if field[row + _row][col + _col]:
                    return False

    return True


def fill(row, col, sticker, field):
    cnt = 0

    for _row in range(len(sticker)):
        for _col in range(len(sticker[_row])):
            if sticker[_row][_col]:
                field[_row + row][_col + col] = True
                cnt += 1

    return cnt


def check(field, sticker) -> int:
    # 0, 90, 180, 270
    for _ in range(4):
        for row in range(len(field)):
            for col in range(len(field[row])):
                if fit(row, col, sticker, field):
                    return fill(row, col, sticker, field)

        sticker = rotate(sticker)

    return 0


if __name__ == '__main__':
    height, width, n_sticker = map(int, sys.stdin.readline().split())
    field = [[False] * width for _ in range(height)]
    answer = 0

    for _ in range(n_sticker):
        n_row, n_col = map(int, sys.stdin.readline().split())
        sticker = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n_row)]
        answer += check(field, sticker)

    print(answer)
