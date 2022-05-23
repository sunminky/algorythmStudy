# https://www.acmicpc.net/problem/1759

import sys
from itertools import combinations


def check_valid(text):
    collection = {'a', 'e', 'i', 'o', 'u'}  # 모음
    consonant = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}  # 자음
    collection_cnt = 0
    consonant_cnt = 0

    for e in text:
        collection_cnt += e in collection
        consonant_cnt += e in consonant

    return collection_cnt >= 1 and consonant_cnt >= 2


if __name__ == '__main__':
    length, _ = map(int, sys.stdin.readline().split())
    alpha = tuple(sorted(sys.stdin.readline().split()))

    for e in combinations(alpha, length):
        if check_valid(e):
            print("".join(e))
