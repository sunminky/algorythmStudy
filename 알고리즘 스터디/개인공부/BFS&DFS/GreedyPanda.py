# https://www.acmicpc.net/problem/1937

import sys

field = [[*map(int, sys.stdin.readline().split())] for _ in range(int(sys.stdin.readline()))]
cost = [[-1 for _ in range(len(field))] for _ in range(len(field))]


def search(x, y):
    result = 0

    # 이미 계산한 적이 있으면 패스
    if cost[y][x] != -1:
        return cost[y][x]
    
    # 상
    if y + 1 < len(field):
        if field[y + 1][x] > field[y][x]:
            result = max(result, search(x, y + 1))
    # 하
    if y - 1 >= 0:
        if field[y - 1][x] > field[y][x]:
            result = max(result, search(x, y - 1))
    # 좌
    if x - 1 >= 0:
        if field[y][x - 1] > field[y][x]:
            result = max(result, search(x - 1, y))
    # 우
    if x + 1 < len(field):
        if field[y][x + 1] > field[y][x]:
            result = max(result, search(x + 1, y))

    cost[y][x] = result + 1
    return result + 1


if __name__ == '__main__':
    answer = 0

    for row in range(len(field)):
        for col in range(len(field)):
            answer = max(answer, search(col, row))

    print(answer)
