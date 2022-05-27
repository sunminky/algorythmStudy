# https://www.acmicpc.net/problem/12100
import sys
from collections import deque

width = int(sys.stdin.readline())


# 상하로 밀기
def vertical_compress(field, direction) -> list:
    result = [[0] * width for _ in range(width)]
    movement = (0, width, 1) if direction == 0 else (width - 1, -1, -1)

    for col in range(width):
        stack = deque()

        for row in range(*movement):
            if stack:
                if stack[-1][1] is False:
                    if stack[-1][0] == field[row][col]:
                        stack[-1][0] *= 2
                        stack[-1][1] = True
                        continue
            if field[row][col] != 0:
                stack.append([field[row][col], False])

        for row in range(*movement):
            if not stack:
                break
            result[row][col] = stack.popleft()[0]

    return result


def horizontal_compress(field, direction) -> list:
    result = [[0] * width for _ in range(width)]
    movement = (0, width, 1) if direction == 0 else (width - 1, -1, -1)

    for row in range(width):
        stack = deque()

        for col in range(*movement):
            if stack:
                if stack[-1][1] is False:
                    if stack[-1][0] == field[row][col]:
                        stack[-1][0] *= 2
                        stack[-1][1] = True
                        continue

            if field[row][col] != 0:
                stack.append([field[row][col], False])

        for col in range(*movement):
            if not stack:
                break
            result[row][col] = stack.popleft()[0]

    return result


# 위로 밀기
def top_compress(field) -> list:
    return vertical_compress(field, 0)


# 아래로 밀기
def bottom_compress(field) -> list:
    return vertical_compress(field, 1)


# 왼쪽으로 밀기
def left_compress(field) -> list:
    return horizontal_compress(field, 0)


# 오른쪽으로 밀기
def right_compress(field) -> list:
    return horizontal_compress(field, 1)


def play(field, remain) -> int:
    answer = -1

    if remain == 0:
        return max((max(e) for e in field))

    # 위로 밀기
    answer = max(answer, play(top_compress(field), remain - 1))
    # 아래로 밀기
    answer = max(answer, play(bottom_compress(field), remain - 1))
    # 좌로 밀기
    answer = max(answer, play(left_compress(field), remain - 1))
    # 우로 밀기
    answer = max(answer, play(right_compress(field), remain - 1))

    return answer


if __name__ == '__main__':
    field = [list(map(int, sys.stdin.readline().split())) for _ in range(width)]

    print(play(field, 5))
