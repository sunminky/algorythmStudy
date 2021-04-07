# https://www.acmicpc.net/problem/4991

import sys

if __name__ == '__main__':
    while True:
        width, height = map(int, sys.stdin.readline().split())
        field = [sys.stdin.readline().rstrip() for _ in range(height)]
        stain = [[0 for _ in range(11)] for _ in range(11)]     # 쓰레기들의 거리 저장

        if not (width and height):  # 둘 다 0 이면 종료
            break

        print(width, height)
        print(field)
        print(stain)
