#https://www.acmicpc.net/problem/1431

import sys

def sort_func(x):
    total = 0
    for char in x:
        if char.isdecimal():
            total += int(char)
    return total

if __name__ == '__main__':
    n_guitar = int(sys.stdin.readline())
    guitars = []

    for _ in range(n_guitar):
        guitars.append(sys.stdin.readline())

    guitars.sort(key=lambda x: (len(x), sort_func(x), x))

    for item in guitars:
        print(item, end="")