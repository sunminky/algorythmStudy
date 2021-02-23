#https://www.acmicpc.net/problem/1003

import sys

if __name__ == '__main__':
    test_arr = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
    fibo_arr = [(1, 0), (0, 1)]

    for _ in range(2, max(test_arr) + 1):
        fibo_arr.append((fibo_arr[-1][0] + fibo_arr[-2][0], fibo_arr[-1][1] + fibo_arr[-2][1]))

    for e in test_arr:
        print(fibo_arr[e][0], fibo_arr[e][1])