# https://www.acmicpc.net/problem/15999

import sys

if __name__ == '__main__':
    height, width = map(int, sys.stdin.readline().split())
    field = [sys.stdin.readline().rstrip() for _ in range(height)]
    variable = [[False for _ in range(width)] for _ in range(height)]

    # 다른 색깔이 붙어 있는 경우는 바뀔 수 없는 경우임
    for row in range(height):
        for col in range(width):
            # 왼쪽과 색깔이 다른지 체크
            if col - 1 >= 0:
                if field[row][col - 1] != field[row][col]:
                    variable[row][col] = True
                    continue
            # 오른쪽과 색깔이 다른지 체크
            if col + 1 < width:
                if field[row][col + 1] != field[row][col]:
                    variable[row][col] = True
                    continue
            # 위와 색깔이 다른지 체크
            if row - 1 >= 0:
                if field[row - 1][col] != field[row][col]:
                    variable[row][col] = True
                    continue
            # 아래와 색깔이 다른지 체크
            if row + 1 < height:
                if field[row + 1][col] != field[row][col]:
                    variable[row][col] = True

    print(pow(2, width * height - sum([sum(variables) for variables in variable]), 1000000007))
