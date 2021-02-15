#https://www.acmicpc.net/problem/1655

import sys
from bisect import bisect_left

if __name__ == '__main__':
    n_numbers = int(sys.stdin.readline())
    numbers = []

    for stage in range(n_numbers):
        data = int(sys.stdin.readline())

        numbers.insert(bisect_left(numbers, data), data)

        if stage % 2 == 0:
            print(numbers[stage//2])
        else:
            print(min(numbers[stage//2], numbers[stage//2+1]))