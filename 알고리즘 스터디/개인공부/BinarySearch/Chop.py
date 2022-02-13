# https://www.acmicpc.net/problem/2805
import sys
from bisect import bisect_left

if __name__ == '__main__':
    n_tree, quota = map(int, sys.stdin.readline().split())
    trees = sorted(map(int, sys.stdin.readline().split()))
    answer = 0

    start = 0
    end = 1000000000

    while start < end:
        middle = (start + end) // 2
        total_chopped = 0

        for idx in range(bisect_left(trees, middle), n_tree):
            total_chopped += trees[idx] - middle

        if total_chopped >= quota:
            answer = max(answer, middle)
            start = middle + 1
        else:
            end = middle

    print(answer)
