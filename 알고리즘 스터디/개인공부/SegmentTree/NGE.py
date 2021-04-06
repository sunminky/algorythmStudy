# https://www.acmicpc.net/problem/17298

import sys
from collections import deque

if __name__ == '__main__':
    sys.stdin.readline()
    number = [*map(int, sys.stdin.readline().split())]
    answer = [-1] * len(number)
    stack = deque()

    for i in range(len(number)-1, -1, -1):
        # 자신보다 작은 원소들 제거하기
        while stack:
            if stack[-1] <= number[i]:
                stack.pop()
            else:
                answer[i] = stack[-1]
                break

        stack.append(number[i])

    print(" ".join(map(str, answer)))
