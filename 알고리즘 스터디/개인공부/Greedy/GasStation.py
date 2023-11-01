# https://www.acmicpc.net/problem/13305
import sys

if __name__ == '__main__':
    answer = 0
    n_city = int(sys.stdin.readline())
    distance = tuple(map(int, sys.stdin.readline().split()))
    costs = list(map(int, sys.stdin.readline().split()))

    prev_cost = costs[0]
    move = 0
    costs[-1] = -1

    for i in range(1, n_city):
        move += distance[i - 1]
        if costs[i] < prev_cost:
            answer += move * prev_cost
            prev_cost = costs[i]
            move = 0

    print(answer)
