#https://www.acmicpc.net/problem/1009

import sys

def repeated_squaring(denominator, exponent, divisor):
    if denominator % 10 == 0:
        return 10
    else:
        return pow(denominator, exponent, divisor)


if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        d, e = tuple(map(int, sys.stdin.readline().split()))
        print(repeated_squaring(d, e, 10))