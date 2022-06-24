# https://www.acmicpc.net/problem/11066
import sys

if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        n_file = int(sys.stdin.readline())
        files = tuple(map(int, sys.stdin.readline().split()))
        dp = [[2500000000] * n_file for _ in range(n_file)]
        summation = [0] * (n_file + 1)

        for seq in range(n_file):
            summation[seq + 1] = summation[seq] + files[seq]

        for row in range(n_file):
            dp[row][row] = 0

        for i in range(n_file):
            for row in range(n_file - i):
                # 나누기
                for sp in range(row, row + i):
                    dp[row][row + i] = min(dp[row][row + i],
                                           dp[row][sp] + dp[sp + 1][row + i] + summation[row + i + 1] - summation[row])

        print(dp[0][n_file - 1])
