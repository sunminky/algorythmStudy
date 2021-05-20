# https://www.acmicpc.net/problem/1016
import sys
from math import sqrt, ceil, floor

if __name__ == '__main__':
    min_val, max_val = map(int, sys.stdin.readline().split())
    sieve = [True] * (max_val - min_val + 1)    # 에라토스테너스의 체

    for n in range(2, floor(sqrt(max_val)) + 1):
        pow_val = n ** 2    # 현재 제곱수
        start = ceil(min_val / pow_val) * pow_val   # 제곱수 체크 시작 범위

        # 현재 제곱수로 나누어 떨어지는 수는 False로 바꿈
        for i in range(start, max_val + 1, pow_val):
            sieve[i - min_val] = False

    print(sum(sieve))   # 체에서 True의 개수를 셈
