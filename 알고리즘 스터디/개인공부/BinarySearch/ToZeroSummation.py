# https://www.acmicpc.net/problem/3151
import sys
from bisect import bisect_right, bisect_left

sys.stdin.readline()  # 안씀
solutions = sorted(map(int, sys.stdin.readline().split()))

if __name__ == '__main__':
    answer = 0

    for i in range(len(solutions) - 1):
        for j in range(i + 1, len(solutions)):
            diff = -(solutions[i] + solutions[j])
            high = bisect_right(solutions, diff, i + 1, j)
            low = bisect_left(solutions, diff, i + 1, high)
            answer += high - low

    print(answer)
