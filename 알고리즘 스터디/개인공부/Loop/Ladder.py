# https://www.acmicpc.net/problem/15684
import sys
from itertools import combinations

n_horizontal, n_line, n_vertical = map(int, sys.stdin.readline().split())


def check(field) -> bool:
    for col in range(n_horizontal):
        cur_x = col
        for row in range(n_vertical):
            if cur_x - 1 >= 0 and field[row][cur_x - 1]:
                cur_x -= 1
            elif cur_x < n_horizontal - 1 and field[row][cur_x]:
                cur_x += 1
        if cur_x != col:
            return False

    return True


if __name__ == '__main__':
    field = [[False] * (n_horizontal - 1) for _ in range(n_vertical)]
    candidate = []
    answer = -1

    for _ in range(n_line):
        row, col = map(int, sys.stdin.readline().split())
        field[row - 1][col - 1] = True

    for row in range(n_vertical):
        for col in range(n_horizontal - 1):
            if not field[row][col]:
                candidate.append((col, row))

    for i in range(4):
        for com in combinations(candidate, i):
            # 줄 긋기
            for col, row in com:
                field[row][col] = True

            if check(field):
                answer = i
                break

            # 원상 복구
            for col, row in com:
                field[row][col] = False
        else:
            continue
        break

    print(answer)
