# https://www.acmicpc.net/problem/2436
import sys
from math import sqrt, ceil


def gcd(a, b):
    while a:
        a, b = max(a, b) % min(a, b), min(a, b)

    return b


if __name__ == '__main__':
    common_factor, common_multiple = map(int, sys.stdin.readline().split())
    target = common_multiple / common_factor
    answer = 2000000000
    answer_element = [0, 0]

    for i in range(1, ceil(sqrt(target)) + 1):
        if target % i == 0:
            # 서로수여야 함
            if gcd(i, target / i) == 1:
                if answer > i + target / i:
                    answer = i + target / i
                    answer_element[0] = i
                    answer_element[1] = target / i

    answer_element.sort()

    print(f"{int(answer_element[0] * common_factor)} {int(answer_element[1] * common_factor)}")
