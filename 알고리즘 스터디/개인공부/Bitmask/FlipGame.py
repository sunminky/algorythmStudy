# https://www.acmicpc.net/problem/23058
import sys
from copy import deepcopy

width = int(sys.stdin.readline())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(width)]


def countEach(field):
    return min(sum([e.count(0) for e in field]), sum([e.count(1) for e in field]))


def flip(flag) -> list:
    result = deepcopy(field)

    # 가로 뒤집기
    for row in range(width):
        if flag & (1 << row):
            for col in range(width):
                result[row][col] = (result[row][col] + 1) % 2

    # 세로 뒤집기
    for col in range(width):
        if flag & (1 << (col + width)):
            for row in range(width):
                result[row][col] = (result[row][col] + 1) % 2

    return result


def game(flag, remain):
    if not remain:
        return countEach(flip(flag)) + bin(flag)[2:].count('1')

    return min(game(flag | (1 << (remain - 1)), remain - 1), game(flag, remain - 1))


if __name__ == '__main__':
    answer = min(game(0, width * 2), 64)

    print(answer)
