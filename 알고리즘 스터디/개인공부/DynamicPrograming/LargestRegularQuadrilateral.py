# https://www.acmicpc.net/problem/1915

import sys

if __name__ == '__main__':
    height, width = map(int, sys.stdin.readline().split())
    field = [sys.stdin.readline().rstrip() for _ in range(height)]
    cost = [[1 if field[row][col] == '1' and (col == 0 or row == 0) else 0 for col in range(width)] for row in
            range(height)]
    answer = 0

    # 첫 번째 행과 첫 번째 열에 1이 있는 경우 최소 넓이는 1
    answer = 1 if '1' in field[0] else 0
    if answer == 0:
        for row in range(height):
            if field[row][0] == '1':
                answer = 1
                break

    for row in range(1, height):
        for col in range(1, width):
            # 현재 위치에서 만들수 있는 가장 큰 정사각형의 길이 : (col-1, row-1), (col-1, row), (col, row-1) 중 가장 작은 값 + 1임
            if field[row][col] == '1':
                cost[row][col] = \
                    min(
                        cost[row - 1][col - 1],
                        cost[row - 1][col],
                        cost[row][col - 1]
                    ) + 1
                answer = max(answer, cost[row][col])

    print(answer ** 2)
