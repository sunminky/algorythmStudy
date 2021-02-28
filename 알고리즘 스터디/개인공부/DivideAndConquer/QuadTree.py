#https://www.acmicpc.net/problem/1992

import sys

def divide(unit:int, x:int, y:int):
    global field

    if unit == 1:
        print(field[y][x], end="")
        return
    else:
        sum_val = sum([sum(field[y+i][x:x+unit]) for i in range(unit)])
        if sum_val == 0 or sum_val == unit**2:
            print(field[y][x], end="")
        else:
            print("(", end="")
            divide(unit // 2, x, y)
            divide(unit // 2, x + unit // 2, y)
            divide(unit // 2, x, y + unit // 2)
            divide(unit // 2, x + unit // 2, y + unit // 2)
            print(")", end="")

if __name__ == '__main__':
    global field
    N = int(sys.stdin.readline())
    field = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

    divide(N, 0, 0)