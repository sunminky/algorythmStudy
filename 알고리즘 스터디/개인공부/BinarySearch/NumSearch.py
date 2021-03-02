#https://www.acmicpc.net/problem/1920

import sys

def search(numbers, target):
    start_idx = 0
    end_idx = len(numbers)

    while start_idx < end_idx:
        middle = (start_idx + end_idx) // 2

        if numbers[middle] == target:
            return 1
        if numbers[middle] < target:
            start_idx = middle+1
        else:
            end_idx = middle

    return 0

if __name__ == '__main__':
    sys.stdin.readline()
    number = sorted(map(int, sys.stdin.readline().split()))

    sys.stdin.readline()
    for item in map(int, sys.stdin.readline().split()):
        print(search(number, item))