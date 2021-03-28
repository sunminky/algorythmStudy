# https://www.acmicpc.net/problem/15922

import sys

if __name__ == '__main__':
    cur_x = cur_y = -1000000000
    answer = 0

    for _ in range(int(sys.stdin.readline())):
        x, y = map(int, sys.stdin.readline().split())

        # 이전 범위에서 벗어난 경우
        if not cur_x <= x <= cur_y:
            answer += cur_y - cur_x
            cur_x = x
            cur_y = y

        else:
            cur_y = max(cur_y, y)

    # 마지막 구간 계산
    answer += cur_y - cur_x
    print(answer)
