# https://www.acmicpc.net/problem/23058
import sys
from copy import deepcopy


def count(flag, width, field):
    new_field = deepcopy(field)
    cnt = 0

    # 뒤집기
    for row in range(width):
        if flag & (1 << row):
            cnt += 1

            for col in range(width):
                new_field[row][col] = not new_field[row][col]

    for col in range(width):
        if flag & (1 << (col + width)):
            cnt += 1

            for row in range(width):
                new_field[row][col] = not new_field[row][col]

    return cnt + min(sum((e.count(True) for e in new_field)), sum((e.count(False) for e in new_field)))


if __name__ == '__main__':
    width = int(sys.stdin.readline())
    field = [[True if e == '1' else False for e in sys.stdin.readline().split()] for _ in range(width)]
    answer = 64

    for i in range(1 << (width * 2)):
        answer = min(answer, count(int(bin(i)[2:]), width, field))

    print(answer)
