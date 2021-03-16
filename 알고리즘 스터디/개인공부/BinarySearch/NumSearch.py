#https://www.acmicpc.net/problem/1920

import sys
from bisect import bisect_right

if __name__ == '__main__':
    sys.stdin.readline()
    number = sorted(map(int, sys.stdin.readline().split()))

    sys.stdin.readline()
    for item in map(int, sys.stdin.readline().split()):
        idx = bisect_right(number, item)

        if idx == 0 or number[idx-1] != item:
            print(0)
        else:
            print(1)
