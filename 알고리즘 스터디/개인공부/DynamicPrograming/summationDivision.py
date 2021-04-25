# https://www.acmicpc.net/problem/2225

import sys

if __name__ == '__main__':
    limit, tries = map(int, sys.stdin.readline().split())
    tries_memo = [[1] * (limit + 1)] * tries

    for try_cnt in range(1, tries):
        for number in range(1, limit + 1):
            # (숫자 하나 덜 쓴 것 + 0) + (하나 모자란 숫자에 1을 더한 것)
            tries_memo[try_cnt][number] = (tries_memo[try_cnt - 1][number] + tries_memo[try_cnt][number - 1]) % 1000000000

    print(tries_memo[-1][-1])
