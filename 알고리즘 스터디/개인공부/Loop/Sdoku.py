# https://www.acmicpc.net/problem/2580
import sys

board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
row_arr = [[False] * 10 for _ in range(10)]
col_arr = [[False] * 10 for _ in range(10)]
box_arr = [[False] * 10 for _ in range(10)]
pos = []


def dfs(depth):
    if depth == len(pos):
        for e in board:
            print(' '.join(map(str, e)))
        exit(0)

    x, y = pos[depth]

    for n in range(1, 10):
        if not row_arr[y][n]:
            if not col_arr[x][n]:
                if not box_arr[y // 3 * 3 + x // 3][n]:
                    row_arr[y][n] = True
                    col_arr[x][n] = True
                    box_arr[y // 3 * 3 + x // 3][n] = True
                    board[y][x] = n

                    dfs(depth + 1)

                    row_arr[y][n] = False
                    col_arr[x][n] = False
                    box_arr[y // 3 * 3 + x // 3][n] = False
                    board[y][x] = 0


if __name__ == '__main__':
    for row in range(9):
        for col in range(9):
            if board[row][col]:
                row_arr[row][board[row][col]] = True
                col_arr[col][board[row][col]] = True
                box_arr[row // 3 * 3 + col // 3][board[row][col]] = True
            else:
                pos.append((col, row))

    dfs(0)
