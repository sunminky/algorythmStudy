# https://www.acmicpc.net/problem/16235
import sys
from collections import deque


def breeding(plant, row, col) -> int:
    movement = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    new_tree = 0

    for tree in plant[row][col]:
        if tree % 5 != 0:
            continue

        for _col, _row in movement:
            new_y = row + _row
            new_x = col + _col

            if not 0 <= new_y < len(plant):
                continue

            if not 0 <= new_x < len(plant[new_y]):
                continue

            plant[new_y][new_x].appendleft(1)
            new_tree += 1

    return new_tree


def grow(plant, field, row, col) -> int:
    dead = False
    n_tree = dead_idx = len(plant[row][col])

    for seq, tree in enumerate(plant[row][col]):
        if dead:
            field[row][col] += tree // 2
            continue

        if field[row][col] < tree:
            dead = True
            field[row][col] += tree // 2
            dead_idx = seq
        else:
            field[row][col] -= plant[row][col][seq]
            plant[row][col][seq] += 1

    if dead:
        while len(plant[row][col]) != dead_idx:
            plant[row][col].pop()

    return n_tree - dead_idx


if __name__ == '__main__':
    width, n_tree, time_limit = map(int, sys.stdin.readline().split())
    field = [[5] * width for _ in range(width)]
    plant = [[deque() for _ in range(width)] for _ in range(width)]
    fertilizer = [tuple(map(int, sys.stdin.readline().split())) for _ in range(width)]
    answer = 0

    plant_pos = []

    for _ in range(n_tree):
        plant_pos.append(tuple(map(int, sys.stdin.readline().split())))

    plant_pos.sort(key=lambda x: x[2])

    for _y, _x, _age in plant_pos:
        plant[_y - 1][_x - 1].append(_age)
        answer += 1

    for _ in range(time_limit):
        # 봄, 여름
        for row in range(width):
            for col in range(width):
                answer -= grow(plant, field, row, col)
        # 가을
        for row in range(width):
            for col in range(width):
                answer += breeding(plant, row, col)
        # 겨울
        for row in range(width):
            for col in range(width):
                field[row][col] += fertilizer[row][col]

    print(answer)
