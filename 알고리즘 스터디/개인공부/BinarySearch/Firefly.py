# https://www.acmicpc.net/problem/3020

import sys
from bisect import bisect_left

if __name__ == '__main__':
    width, height = map(int, sys.stdin.readline().split())
    stalagmite = []  # 석순
    stalactite = []  # 종유석
    answer = 200001
    answer_cnt = 0

    for i in range(width):
        if i & 1 == 0:  # 짝수인 경우
            stalagmite.append(int(sys.stdin.readline()))
        else:  # 홀수인 경우
            stalactite.append(height - int(sys.stdin.readline()))

    stalagmite.sort()
    stalactite.sort()

    for h in range(1, height + 1):
        collision = len(stalagmite) - bisect_left(stalagmite, h) + bisect_left(stalactite, h)

        if collision < answer:
            answer = collision
            answer_cnt = 0

        if collision == answer:
            answer_cnt += 1

    print(answer, answer_cnt)
