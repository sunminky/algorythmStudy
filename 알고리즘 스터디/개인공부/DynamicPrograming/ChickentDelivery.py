# https://www.acmicpc.net/problem/15686
import sys
from itertools import combinations


def get_pos(field: list, width: int) -> tuple:
    home_pos, chicken_pos = dict(), dict()

    for row in range(width):
        for col in range(width):
            if field[row][col] == 1:
                home_pos[len(home_pos)] = (row, col)
            elif field[row][col] == 2:
                chicken_pos[len(chicken_pos)] = (row, col)

    return home_pos, chicken_pos


def get_distance(home_pos, chicken_pos) -> list:
    result = [[0] * len(home_pos) for _ in range(len(chicken_pos))]

    for row in range(len(chicken_pos)):
        for col in range(len(home_pos)):
            result[row][col] = abs(chicken_pos[row][0] - home_pos[col][0]) + abs(chicken_pos[row][1] - home_pos[col][1])

    return result


def calc(candidate, distance_matrix, chicken_pos):
    result = 0

    for col in range(len(distance_matrix[0])):
        value = 2500

        for k in chicken_pos:
            if k in candidate:
                continue
            value = min(value, distance_matrix[k][col])

        result += value

    return result


if __name__ == '__main__':
    width, n_close_chicken = map(int, sys.stdin.readline().split())
    field = [tuple(map(int, sys.stdin.readline().split())) for _ in range(width)]
    home_pos, chicken_pos = get_pos(field, width)
    distance_matrix = get_distance(home_pos, chicken_pos)
    answer = 2500

    for e in combinations(chicken_pos.keys(), len(chicken_pos) - n_close_chicken):
        answer = min(answer, calc(set(e), distance_matrix, chicken_pos))

    print(answer)
