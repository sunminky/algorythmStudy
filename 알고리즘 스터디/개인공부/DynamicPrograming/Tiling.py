#https://www.acmicpc.net/problem/11726
# https://programmers.co.kr/learn/courses/30/lessons/12900

import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    cost = [i for i in range(1, N+1)]

    for i in range(2, N):
        cost[i] = (cost[i-1] + cost[i-2]) % 1000000007

    print(cost[N-1])
