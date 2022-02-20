# https://www.acmicpc.net/problem/17245
import sys
from math import ceil


if __name__ == '__main__':
    height = int(sys.stdin.readline())
    field = [tuple(map(int, sys.stdin.readline().split())) for _ in range(height)]
    target = ceil(sum(sum(e) for e in field) / 2)
    start = 0
    end = 10000001
    answer = 10000001

    while start < end:
        middle = (start + end) // 2

        if sum(sum(min(middle, e) for e in line) for line in field) >= target:
            end = middle
            answer = min(answer, middle)
        else:
            start = middle + 1

    print(answer)
