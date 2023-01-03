# https://www.acmicpc.net/problem/1007
import sys
from itertools import combinations
from math import sqrt

if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        answer = 4000000
        n_pos = int(sys.stdin.readline())
        pos = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n_pos)]
        x_sum = sum(map(lambda x: x[0], pos))
        y_sum = sum(map(lambda x: x[1], pos))
        comb = tuple(combinations(pos, n_pos // 2))

        for e in comb[:len(comb) // 2]:
            x_sub = sum(map(lambda x: x[0], e))
            y_sub = sum(map(lambda x: x[1], e))

            answer = min(sqrt((x_sum - x_sub - x_sub) ** 2 + (y_sum - y_sub - y_sub) ** 2), answer)

        print(f"{answer:.7f}")
