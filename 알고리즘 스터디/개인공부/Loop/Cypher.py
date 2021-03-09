#https://www.acmicpc.net/problem/1759

import sys
from itertools import combinations

def check_valid(text):
    collection = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1} #모음
    consonant = {'b': 1, 'c': 1, 'd': 1, 'f': 1, 'g': 1, 'h': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1,
                 'n': 1, 'p': 1, 'q': 1, 'r': 1, 's': 1, 't': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1}  #자음
    col_cnt = cons_cnt = 0

    for ch in text:
        col_cnt += collection.get(ch, 0)
        cons_cnt += consonant.get(ch, 0)

    return col_cnt >= 1 and cons_cnt >= 2


if __name__ == '__main__':
    c_len, _ = tuple(map(int, sys.stdin.readline().split()))
    alphabets = sorted(sys.stdin.readline().split())

    for c in combinations(alphabets, c_len):
        text = "".join(c)
        if check_valid(text):
            print(text)