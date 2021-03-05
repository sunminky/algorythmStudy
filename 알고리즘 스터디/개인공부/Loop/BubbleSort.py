#https://www.acmicpc.net/problem/1517

import sys

if __name__ == '__main__':
    sys.stdin.readline()
    numbers = list(map(int, sys.stdin.readline().split()))
    swap_cnt = 0

    for i in range(len(numbers)-1):
        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                swap_cnt += 1

    print(swap_cnt)
    print(numbers)