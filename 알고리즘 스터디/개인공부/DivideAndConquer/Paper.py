#https://www.acmicpc.net/problem/2630

import sys

count = [0, 0]

def divide(size:int, x:int, y:int):
    global field

    if size == 1:
        count[field[y][x]] += 1

    else:
        sum_value = sum([sum(field[y+r][x:x+size]) for r in range(size)])

        if sum_value == size ** 2 or sum_value == 0:
            count[field[y][x]] += 1
        else:
            divide(size // 2, x, y)
            divide(size // 2, x + size // 2, y)
            divide(size // 2, x, y + size // 2)
            divide(size // 2, x + size // 2, y + size // 2)

if __name__ == '__main__':
    global field
    N = int(sys.stdin.readline())
    field = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

    divide(N, 0, 0)

    print(count[0], count[1], sep="\n")