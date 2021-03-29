# https://www.acmicpc.net/problem/2170

import sys

if __name__ == '__main__':
    lines = sorted([[*map(int, sys.stdin.readline().split())] for _ in range(int(sys.stdin.readline()))],
                   key=lambda x: x[0])
    cur_x = cur_y = -1000000001
    answer = 0

    for line in lines:
        if not cur_x <= line[0] <= cur_y:
            answer += cur_y - cur_x
            cur_x = line[0]
            cur_y = line[1]
        else:
            cur_y = max(cur_y, line[1])

    answer += cur_y - cur_x
    print(answer)
