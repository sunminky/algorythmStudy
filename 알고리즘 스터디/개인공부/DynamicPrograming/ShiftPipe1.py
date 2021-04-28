# https://www.acmicpc.net/problem/17070

import sys

if __name__ == '__main__':
    n_size = int(sys.stdin.readline())
    field = [sys.stdin.readline().split() for _ in range(n_size)]
    cost = [[[0, 0, 0] for _ in range(n_size)] for _ in range(n_size)]  # [가로, 세로, 대각선]

    # cost[0][:] = [1, 0, 0], cost[0][-1] = [0, 0, 0]
    for col in range(n_size - 1):
        if field[0][col] == '1':
            break
        cost[0][col] = [1, 0, 0]

    # 비용 계산
    for row in range(1, n_size):
        for col in range(2, n_size):
            # 현재 위치가 벽인경우 pass
            if field[row][col] == '1':
                continue

            cost[row][col][0] = cost[row][col-1][0] + cost[row][col-1][2]
            cost[row][col][1] = cost[row-1][col][1] + cost[row-1][col][2]

            # 대각선으로 굴리는데 벽에 긁히지 않는 경우에만 굴림
            if not (field[row-1][col] == '1' or field[row][col-1] == '1'):
                cost[row][col][2] = cost[row-1][col-1][0] + cost[row-1][col-1][1] + cost[row-1][col-1][2]

    print(sum(cost[-1][-1]))
