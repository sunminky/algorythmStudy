# https://www.acmicpc.net/problem/13711
import sys
from bisect import bisect_left

if __name__ == '__main__':
    sys.stdin.readline()    # 필요없음
    text1 = list(map(int, sys.stdin.readline().split()))
    position_dict = [0] * len(text1)
    lcs = []

    for idx, ch in enumerate(text1):
        position_dict[ch - 1] = idx

    for ch in map(int, sys.stdin.readline().split()):
        idx = bisect_left(lcs, position_dict[ch - 1])

        if idx == len(lcs):
            lcs.append(position_dict[ch - 1])
        else:
            lcs[idx] = position_dict[ch - 1]

    print(len(lcs))
