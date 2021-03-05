#https://www.acmicpc.net/problem/3078

import sys
from collections import deque

if __name__ == '__main__':
    n_school_mate, offset = tuple(map(int, sys.stdin.readline().split()))
    queue = deque()
    name_dict = dict()
    answer = 0

    for _ in range(offset):
        name_len = len(sys.stdin.readline())

        if name_dict.get(name_len, 0) == 0:
            name_dict[name_len] = 1
        else:
            answer += name_dict[name_len]
            name_dict[name_len] += 1

        queue.append(name_len)

    for _ in range(n_school_mate - offset):
        name_len = len(sys.stdin.readline())

        if name_dict.get(name_len, 0) == 0:
            name_dict[name_len] = 1
        else:
            answer += name_dict[name_len]
            name_dict[name_len] += 1

        queue.append(name_len)
        name_dict[queue.popleft()] -= 1

    print(answer)