#https://www.acmicpc.net/problem/12015
#세그먼트 트리로도 구현 가능

import sys
from bisect import bisect_left

if __name__ == '__main__':
    n_number = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().split()))
    lis = []

    for n in numbers:
        idx = bisect_left(lis, n)

        if idx == len(lis):
            lis.append(n)
        else:
            lis[idx] = n

    print(len(lis))
