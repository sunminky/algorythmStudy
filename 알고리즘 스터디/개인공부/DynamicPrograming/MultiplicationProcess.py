# https://www.acmicpc.net/problem/11049

import sys

if __name__ == '__main__':
    n_array = int(sys.stdin.readline())
    arrays = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n_array)]
    # cost_memo(row, col), col ~ row 까지 행렬을 곱했을 때 최소값 저장
    cost_memo = [[0] * n_array for _ in range(n_array)]

    for col in range(1, n_array):
        for row in range(n_array - col):
            cost_memo[row][col + row] = min(
                [cost_memo[row][i] + cost_memo[i + 1][col + row] + arrays[row][0] * arrays[i][1] * arrays[col + row][1]
                 for i in range(row, col + row)]
            )

    print(cost_memo[0][n_array - 1])
