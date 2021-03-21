# https://www.acmicpc.net/problem/2381

import sys

if __name__ == '__main__':
    n_num = int(sys.stdin.readline())
    calc = [[[0, i] for i in range(n_num)], [[0, i] for i in range(n_num)]]     # [x+y, seq], [x-y, seq]

    for i in range(n_num):
        x, y = map(int, sys.stdin.readline().split())
        calc[0][i][0] = x + y
        calc[1][i][0] = x - y

    answer = []
    # -(x + y) + (x + y)
    answer.append(-min(calc[0], key=lambda x: x[0])[0] + max(calc[0], key=lambda x: x[0])[0])
    # -(x - y) + (x - y)
    answer.append(-min(calc[1], key=lambda x: x[0])[0] + max(calc[1], key=lambda x: x[0])[0])
    # (x - y) - (x - y)
    answer.append(max(calc[1], key=lambda x: x[0])[0] - min(calc[1], key=lambda x: x[0])[0])
    # (x + y) - (x + y)
    answer.append(max(calc[0], key=lambda x: x[0])[0] - min(calc[0], key=lambda x: x[0])[0])

    print(max(answer))