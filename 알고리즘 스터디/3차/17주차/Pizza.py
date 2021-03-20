# https://www.acmicpc.net/problem/1756

import sys
from bisect import bisect_left, bisect_right


if __name__ == '__main__':
    sys.stdin.readline()    #필요없음
    oven = list(map(int, sys.stdin.readline().split()))
    dough = list(map(int, sys.stdin.readline().split()))
    answer = -1

    min_val = oven[0]
    for i in range(len(oven)):
        if oven[i] < min_val:
            min_val = oven[i]
        else:
            oven[i] = min_val

    oven.reverse()

    for d in dough:
        answer = max(bisect_left(oven, d), answer + 1)

    print(max(len(oven) - answer, 0))