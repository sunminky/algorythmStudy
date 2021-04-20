# https://www.acmicpc.net/problem/1025

import sys


height, width = map(int, sys.stdin.readline().split())
field = [[*map(int, sys.stdin.readline().rstrip())] for _ in range(height)]


# 제곱수 체크
def square_check(num) -> bool:
    if (num ** 0.5) % 1 != 0:
        return False
    return True


def search(x, y) -> int:
    result = -1

    for x_d in range(-width, width):
        for y_d in range(-height, height):
            cur_x = x   # 현재 x좌표
            cur_y = y   # 현재 y좌표
            combi = 0   # 이어붙인 값

            while (0 <= cur_x < width) and (0 <= cur_y < height):
                combi = combi * 10 + field[cur_y][cur_x]    # 이어붙이기

                # 행 공차와 열 공차가 모두 0이면 무한루프 탈출 시켜야 함
                if x_d == 0 and y_d == 0:
                    break

                cur_x += x_d
                cur_y += y_d

                if square_check(combi):
                    result = max(result, combi)     # 제곱수이면 최대값 갱신

    return result


if __name__ == '__main__':
    answer = -1

    # 전체 타일에 대해 탐색
    for row in range(height):
        for col in range(width):
            answer = max(answer, search(col, row))

    print(answer)
