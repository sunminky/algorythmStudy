# https://www.acmicpc.net/problem/2436

import sys
from math import isqrt


# 서로수인지 체크
def func_gcd(num1, num2):
    n1 = max(num1, num2)
    n2 = min(num1, num2)
    remainder = n2

    # 둘의 최대공약수가 1이 될 때까지 나누기
    while remainder != 1:
        _, remainder = divmod(n1, n2)

        # 둘이 나눠 떨어짐, 서로수가 아님
        if remainder == 0:
            return False

        n1, n2 = n2, remainder

    # 서로수임
    return True


if __name__ == '__main__':
    gcd, gcm = map(int, sys.stdin.readline().split())
    answer = None

    # 자연수1 = gcd * x, 자연수2 = gcd * y 일때, x * y = gcm // gcd
    multiplicand = gcm // gcd
    multiplicand_root = isqrt(multiplicand)

    # 제곱근 보다 작은 약수 탐색
    for i in range(multiplicand_root, 0, -1):
        # 약수 발견
        if multiplicand % i == 0:
            # 두 약수는 서로수여야 최대공약수에 영향을 미치지 않음
            if func_gcd(i, multiplicand // i):
                answer = [i * gcd, multiplicand // i * gcd]
                break   # 제곱근에 가까운 약수 일수록 둘의 합이 작음

    print(" ".join(map(str, sorted(answer))))
