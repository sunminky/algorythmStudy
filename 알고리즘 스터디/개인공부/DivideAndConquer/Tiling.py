# https://www.acmicpc.net/problem/14600

import sys

cnt = 1


def fill(field, N, x, y):
    global cnt

    if N > len(field):
        return

    for row in range(N):
        for col in range(N):
            if field[y + row][x + col] == 0:
                field[y + row][x + col] = cnt

    cnt += 1

    fill(field, N * 2, x // 2, y // 2)



if __name__ == '__main__':
    N = int(sys.stdin.readline())
    field = [[0 for _ in range(2 ** N)] for _ in range(2 ** N)]
    drain = tuple(map(int, sys.stdin.readline().split()))
    field[drain[1] - 1][drain[0] - 1] = -1    #하수구 위치 표시

    fill(field, 2, (drain[1]-1) // 2, (drain[0]-1) // 2)

    for f in field:
        print(f)
