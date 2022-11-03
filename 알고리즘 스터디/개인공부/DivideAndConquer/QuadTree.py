# https://www.acmicpc.net/problem/1992

import sys


def divide(field, width, position):  # x1, y1, x2, y2
    x1, y1, x2, y2 = position
    total = sum((sum((field[row][col] for col in range(x1, x2))) for row in range(y1, y2)))

    if total == width * width or total == 0:
        print(field[y1][x1], end="")
    else:
        print("(", end="")

        divide(field, width >> 1, (x1, y1, x1 + width // 2, y1 + width // 2))  # 좌상
        divide(field, width >> 1, (x1 + width // 2, y1, x2, y1 + width // 2))  # 우상
        divide(field, width >> 1, (x1, y1 + width // 2, x1 + width // 2, y2))  # 좌하
        divide(field, width >> 1, (x1 + width // 2, y1 + width // 2, x2, y2))  # 우하

        print(")", end="")


if __name__ == '__main__':
    width = int(sys.stdin.readline())
    field = [[int(ch) for ch in sys.stdin.readline().rstrip()] for _ in range(width)]

    divide(field, width, (0, 0, width, width))
