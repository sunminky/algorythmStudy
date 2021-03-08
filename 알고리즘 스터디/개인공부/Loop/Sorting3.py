#https://www.acmicpc.net/problem/10989

import sys

if __name__ == '__main__':
    numbers = [0] * 10001

    for _ in range(int(sys.stdin.readline())):
        numbers[int(sys.stdin.readline())] += 1

    for i in range(1, 10001):
        print(f"{i}\n" * numbers[i], end="")