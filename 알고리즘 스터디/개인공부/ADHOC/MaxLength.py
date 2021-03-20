# https://www.acmicpc.net/problem/2381

import sys

if __name__ == '__main__':
    n_num = int(sys.stdin.readline())
    x = [0] * n_num
    y = [0] * n_num

    for i in range(n_num):
        x[i], y[i] = map(int, sys.stdin.readline().split())

    ground = [sum(x) / n_num, sum(y) / n_num]
    max_point_val = 0
    max_point = ground.copy()

    for i in range(n_num):
        if max_point_val < abs(x[i] - ground[0]) + abs(y[i] - ground[1]):
            max_point_val = abs(x[i] - ground[0]) + abs(y[i] - ground[1])
            max_point = [x[i], y[i]]

    max_point_val2 = 0
    max_point2 = max_point.copy()
    for i in range(n_num):
        if max_point_val2 < abs(x[i] - max_point[0]) + abs(y[i] - max_point[1]):
            max_point_val2 = abs(x[i] - max_point[0]) + abs(y[i] - max_point[1])
            max_point2 = [x[i], y[i]]

    print(max_point_val2)