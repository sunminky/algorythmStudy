# https://www.acmicpc.net/problem/2133
import sys


if __name__ == '__main__':
    n = int(sys.stdin.readline())

    if n & 1:
        print(0)
    else:
        acc = past = 1  # 누적합, 바로 직전 누적합

        for _ in range(0, n, 2):
            past += acc * 2
            acc += past

        print(past)
