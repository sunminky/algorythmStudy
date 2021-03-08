#https://www.acmicpc.net/problem/1932
#https://programmers.co.kr/learn/courses/30/lessons/43105

import sys

if __name__ == '__main__':
    triangle = [tuple(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))]
    cost = [0 for _ in range(len(triangle))]    #비용 저장

    cost[0] = triangle[0][0]

    for row in range(1, len(triangle)):
        prev_cost = cost.copy()
        for column in range(row + 1):
            cost[column] = max(prev_cost[min(column, row)], prev_cost[max(0, column - 1)]) + triangle[row][column]

    print(max(cost))
