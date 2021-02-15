#https://www.acmicpc.net/problem/1652

import sys
import re

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    room = []
    horizon = 0
    vertical = 0

    for _ in range(n):
        room.append(sys.stdin.readline().rstrip())

    #가로 탐색
    for r in room:
        horizon += len(re.findall('[.]{2,}', r))

    #세로 탐색
    for j in range(n):
        vertical += len(re.findall('[.]{2,}', "".join([room[i][j] for i in range(n)])))

    print(horizon, vertical)