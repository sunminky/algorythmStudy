# https://www.acmicpc.net/problem/4307

import sys


if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        line_len, n_ant = map(int, sys.stdin.readline().split())
        fast = 0
        slow = 0

        for _ in range(n_ant):
            pos = int(sys.stdin.readline().rstrip())
            fast = max(fast, min(pos, line_len - pos))
            slow = max(slow, max(pos, line_len - pos))

        print(fast, slow)