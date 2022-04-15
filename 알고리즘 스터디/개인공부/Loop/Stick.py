# https://www.acmicpc.net/problem/1094
import sys

if __name__ == '__main__':
    target = int(sys.stdin.readline())
    remain = 64
    cur_stick = 64
    n_stick = 1

    while remain != target:
        cur_stick //= 2

        if remain - cur_stick >= target:
            remain -= cur_stick
            n_stick -= 1

        n_stick += 1

    print(n_stick)
