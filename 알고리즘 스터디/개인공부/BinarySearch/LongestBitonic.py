# https://www.acmicpc.net/problem/11054
import sys
from bisect import bisect_left

if __name__ == '__main__':
    n_number = int(sys.stdin.readline())
    numbers = tuple(map(int, sys.stdin.readline().split()))
    forward = [0] * n_number
    backward = [0] * n_number
    answer = 0

    lis = []
    for i in range(n_number):
        idx = bisect_left(lis, numbers[i])

        if idx == len(lis):
            lis.append(0)

        lis[idx] = numbers[i]
        forward[i] = idx + 1

    lis = []
    for i in range(n_number - 1, -1, -1):
        idx = bisect_left(lis, numbers[i])

        if idx == len(lis):
            lis.append(0)

        lis[idx] = numbers[i]
        backward[i] = idx + 1

    for i in range(n_number):
        answer = max(answer, forward[i] + backward[i] - 1)

    print(answer)
