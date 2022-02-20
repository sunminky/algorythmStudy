# https://www.acmicpc.net/problem/2866
import sys


def transpose(heigh, width) -> list:
    matrix = [sys.stdin.readline().rstrip() for _ in range(height)]
    return [''.join([matrix[col][row] for col in range(heigh)]) for row in range(width)]


if __name__ == '__main__':
    height, width = map(int, sys.stdin.readline().split())
    matrix = transpose(height, width)
    answer = height - 1

    for i in range(height - 1):
        dup_test = set()
        for row in range(width):
            dup_test.add(matrix[row][i + 1:height])
        if len(dup_test) != width:
            answer = i
            break

    print(answer)
