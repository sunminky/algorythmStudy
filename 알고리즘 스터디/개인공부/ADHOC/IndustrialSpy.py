# https://www.acmicpc.net/problem/3671

import sys
from itertools import permutations
import random


# 밀러라빈 소수판별 법
def isprime(n):
    if n == 2:
        return True
    if n < 2 or not n & 1:
        return False

    def mrtest(b):
        x = pow(b, t, n)
        if x == 1:
            return True
        for i in range(s):
            if x == n - 1:  # 나머지가 -1
                return True
            x = pow(x, 2, n)
        return False

    # n이 소수일 때, n -1 = t * pow(2, s), t는 홀수
    s = 0
    t = n - 1
    # t가 홀수가 될 때까지 2로 나눔
    while not t & 1:
        s += 1
        t >>= 1
    # n보다 작은 양의 정수에 대해 밀러라빈 판별식 15번 수행
    for i in range(15):
        b = random.randrange(2, n)
        # 밀러라핀 판별식 1번 수행할 때마다 틀릴 확률이 75% 감소
        if not mrtest(b):
            return False
    return True


if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        numbers = sys.stdin.readline().rstrip()
        answer = set()

        for i in range(1, len(numbers) + 1):
            # 숫자들 중 i개를 가지고 만들 수 있는 조합중 소수인 것을 찾음
            for comb in permutations(numbers, i):
                # 이미 계산한 적이 있는 경우 pass
                if not answer.__contains__(int("".join(comb))) and isprime(int("".join(comb))):
                    answer.add(int("".join(comb)))

        print(len(answer))
