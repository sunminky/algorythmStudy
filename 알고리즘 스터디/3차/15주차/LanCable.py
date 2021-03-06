#https://www.acmicpc.net/problem/1654

import sys

if __name__ == '__main__':
    n_cable, n_require = tuple(map(int, sys.stdin.readline().split()))
    cable = [int(sys.stdin.readline()) for _ in range(n_cable)]
    min_val = 1
    max_val = max(cable) + 1
    answer = 1

    while min_val < max_val:
        middle = (max_val + min_val) // 2

        if sum(e // middle for e in cable) >= n_require:
            min_val = middle + 1
            answer = middle
        else:
            max_val = middle

    print(answer)