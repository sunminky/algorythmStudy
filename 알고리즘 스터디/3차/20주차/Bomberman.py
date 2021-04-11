# https://www.acmicpc.net/problem/16918

import sys

height, width, time = map(int, sys.stdin.readline().split())
field = [list(sys.stdin.readline().rstrip()) for _ in range(height)]
bomb_field = [[-1 for _ in range(width)] for _ in range(height)]    # 현재 위치에서 폭탄이 터질 시간 기록


def explode(c_time):
    for row in range(height):
        for col in range(width):
            if bomb_field[row][col] == c_time:
                bomb_field[row][col] = -1
                field[row][col] = '.'
                #상
                if row - 1 >= 0 and bomb_field[row-1][col] != c_time:
                    bomb_field[row - 1][col] = -1
                    field[row-1][col] = '.'
                #하
                if row + 1 < height and bomb_field[row+1][col] != c_time:
                    bomb_field[row + 1][col] = -1
                    field[row+1][col] = '.'
                #좌
                if col - 1 >= 0 and bomb_field[row][col-1] != c_time:
                    bomb_field[row][col-1] = -1
                    field[row][col-1] = '.'
                #우
                if col + 1 < width and bomb_field[row][col+1] != c_time:
                    bomb_field[row][col+1] = -1
                    field[row][col+1] = '.'


def install(c_time):
    for row in range(height):
        for col in range(width):
            if bomb_field[row][col] == -1:
                bomb_field[row][col] = c_time + 3
                field[row][col] = 'O'


if __name__ == '__main__':
    # 초기 폭탄 위치 탐색
    for row in range(height):
        for col in range(width):
            if field[row][col] == 'O':
                bomb_field[row][col] = 3

    for c_time in range(2, time+1):
        # 폭발
        if c_time & 1:
            explode(c_time)
        # 설치
        else:
            install(c_time)

    for row in field:
        print("".join(row))