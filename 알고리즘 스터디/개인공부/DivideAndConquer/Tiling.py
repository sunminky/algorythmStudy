# https://www.acmicpc.net/problem/14600
# https://www.acmicpc.net/problem/14601

import sys

cnt = 1


#  _____
# |__  |
#   |__|
# 왼쪽 기역
def left_curve(field, N, x, y):
    global cnt

    if N == 1:
        field[y][x] = cnt
        field[y][x+1] = cnt
        field[y+1][x+1] = cnt
        cnt += 1
    else:
        right_curve(field, N//2, x, y)
        left_curve(field, N//2, x + N, y)
        left_curve(field, N//2, x + N//2, y + N//2)
        left_curve2(field, N//2, x + N, y + N)


#  _____
# |   __|
# |__|
# 오른쪽 기역
def right_curve(field, N, x, y):
    global cnt

    if N == 1:
        field[y][x] = cnt
        field[y][x+1] = cnt
        field[y+1][x] = cnt
        cnt += 1
    else:
        right_curve(field, N//2, x, y)
        left_curve(field, N//2, x + N, y)
        right_curve(field, N//2, x + N//2, y + N//2)
        right_curve2(field, N//2, x, y + N)


#    __
# __|  |
# |____|
# 왼쪽 니은
def left_curve2(field, N, x, y):
    global cnt

    if N == 1:
        field[y][x+1] = cnt
        field[y+1][x] = cnt
        field[y+1][x+1] = cnt
        cnt += 1
    else:
        left_curve(field, N//2, x + N, y)
        left_curve2(field, N//2, x + N//2, y + N//2)
        right_curve2(field, N//2, x, y + N)
        left_curve2(field, N//2, x + N, y + N)


#  __
# |  |__
# |____|
# 오른쪽 니은
def right_curve2(field, N, x, y):
    global cnt

    if N == 1:
        field[y][x] = cnt
        field[y+1][x] = cnt
        field[y+1][x+1] = cnt
        cnt += 1
    else:
        right_curve(field, N//2, x, y)
        right_curve2(field, N//2, x + N//2, y + N//2)
        right_curve2(field, N//2, x, y + N)
        left_curve2(field, N//2, x + N, y + N)


# # # #
# 1 2 #
# 3 4 #
# # # #
def select_position(field, N, x, y):
    # 1번 위치
    if field[y][x + N] == 0 and field[y + N][x] == 0 and field[y + N][x + N] == 0:
        return 1
    # 2번 위치
    elif field[y][x] == 0 and field[y + N][x] == 0 and field[y + N][x + N] == 0:
        return 2
    # 3번 위치
    elif field[y][x] == 0 and field[y][x + N] == 0 and field[y + N][x + N] == 0:
        return 3
    # 4번 위치
    elif field[y][x] == 0 and field[y][x + N] == 0 and field[y + N][x] == 0:
        return 4


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    field = [[0 for _ in range(2 ** N)] for _ in range(2 ** N)]
    drain = tuple(map(int, sys.stdin.readline().split()))
    field[drain[1] - 1][drain[0] - 1] = -1    #하수구 위치 표시
    movement = (left_curve2, right_curve2, left_curve, right_curve) #위치에 따라 타일의 모양이 바뀜

    for i in range(N):
        x = (drain[0] - 1) // (2 << i) * (2 << i)
        y = (drain[1] - 1) // (2 << i) * (2 << i)
        movement[select_position(field, 1 << i, x, y) - 1](field, 1 << i, x, y)

    for f in reversed(field):
        print(" ".join(map(str, f)))
