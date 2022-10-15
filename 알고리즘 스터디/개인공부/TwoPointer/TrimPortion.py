# https://www.acmicpc.net/problem/2283
import sys

if __name__ == '__main__':
    times, goal = map(int, sys.stdin.readline().split())
    field = [0] * 1000001
    start = end = acc = upper = 0

    for _ in range(times):
        _start, _end = map(int, sys.stdin.readline().split())
        upper = max(upper, _end)

        field[_start] += 1
        field[_end] -= 1

    for i in range(1000000):
        field[i + 1] += field[i]

    while start < upper and end <= upper:
        if acc < goal:
            acc += field[end]
            end += 1
        elif acc > goal:
            acc -= field[start]
            start += 1
        elif acc == goal:
            print(start, end)
            break
    else:
        print("0 0")
