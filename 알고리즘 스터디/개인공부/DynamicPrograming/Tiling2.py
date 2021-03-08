#https://www.acmicpc.net/problem/11727

import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    a, b = 1, 3

    if N == 1:
        print(a)
    elif N == 2:
        print(b)
    else:
        for i in range(2, N):
            a, b = b, (a * 2 + b) % 10007
        print(b)
