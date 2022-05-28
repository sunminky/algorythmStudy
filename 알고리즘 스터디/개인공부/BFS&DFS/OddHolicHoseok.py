# https://www.acmicpc.net/problem/20164
import sys
from math import log10, floor
from itertools import combinations

min_answer = sys.maxsize
max_answer = 0


def count_odd(target):
    result = 0

    while target:
        result += (target % 10) & 1
        target //= 10

    return result


def split(target, start, end):
    return target % (10 ** start) // (10 ** end)


def divide(target, acc):
    odd_cnt = count_odd(target)

    # 한 자리 수
    if log10(target if target else 1) < 1:
        global max_answer, min_answer

        max_answer = max(max_answer, acc + odd_cnt)
        min_answer = min(min_answer, acc + odd_cnt)
        return

    # 두 자리 수
    if 1 <= log10(target) < 2:
        divide(target // 10 + target % 10, acc + odd_cnt)
        return

    target_len = floor(log10(target if target else 1)) + 1

    for e in combinations(range(target_len - 1), 2):
        idx1, idx2 = e
        divide(split(target, target_len, idx2 + 1) + split(target, idx2 + 1, idx1 + 1) + split(target, idx1 + 1, 0),
               acc + odd_cnt)


if __name__ == '__main__':
    divide(int(sys.stdin.readline()), 0)

    print(min_answer, max_answer)
