# https://www.acmicpc.net/problem/14002
# https://www.acmicpc.net/problem/14003
# 세그먼트 트리로도 구현 가능

import sys
from bisect import bisect_left

if __name__ == '__main__':
    n_number = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().split()))
    lis = []
    idx_lis = [None] * n_number     # 인데스 저장

    for seq, n in enumerate(numbers):
        idx = bisect_left(lis, n)

        if idx == len(lis):
            lis.append(n)
        else:
            lis[idx] = n

        idx_lis[seq] = (idx, n)

    cnt = len(lis) - 1
    for i in range(n_number-1, -1, -1):
        # cnt와 동일한 인덱스를 가지는 가장 먼저 등장하는 숫자를 lis에 넣음
        if idx_lis[i][0] == cnt:
            lis[cnt] = idx_lis[i][1]
            cnt -= 1

            if cnt == -1:
                break

    print(len(lis))
    print(" ".join(map(str, lis)))
