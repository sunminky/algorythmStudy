# https://www.acmicpc.net/problem/3745
import sys
from bisect import bisect_left

if __name__ == '__main__':
    while sys.stdin.readline():
        try:
            lis = []

            for price in map(int, sys.stdin.readline().split()):
                idx = bisect_left(lis, price)

                if idx == len(lis):
                    lis.append(price)
                else:
                    lis[idx] = price

            print(len(lis))

        except EOFError:
            exit(0)
