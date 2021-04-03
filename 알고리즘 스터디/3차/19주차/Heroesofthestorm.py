# https://www.acmicpc.net/problem/16564

import sys

if __name__ == '__main__':
    n_charactor, total_levelup = map(int, sys.stdin.readline().split())
    charactor = [int(sys.stdin.readline()) for _ in range(n_charactor)]
    answer = 0

    min_val = 1
    max_val = 1000000000000000001

    while min_val < max_val:
        middle = (min_val + max_val) // 2
        goal = 0

        for char in charactor:
            offset = max(middle - char, 0)
            goal += offset
        
        # 목표가 너무 높음
        if goal > total_levelup:
            max_val = middle
        else:
            min_val = middle + 1
            answer = max(answer, middle)

    print(answer)
