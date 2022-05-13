# https://www.acmicpc.net/problem/9252
import sys

if __name__ == '__main__':
    text1 = sys.stdin.readline().rstrip()
    text2 = sys.stdin.readline().rstrip()
    cost = [[0] * len(text1) for _ in range(len(text2))]
    dp = [["" for _ in range(len(text1))] for _ in range(len(text2))]
    answer_pos = [0, 0]

    for row in range(len(text2)):
        for col in range(len(text1)):
            if text2[row] == text1[col]:
                if row - 1 >= 0 and col - 1 >= 0:
                    cost[row][col] += cost[row - 1][col - 1]
                    dp[row][col] = dp[row - 1][col - 1]

                cost[row][col] += 1
                dp[row][col] += str(text2[row])

                if cost[row][col] > cost[answer_pos[1]][answer_pos[0]]:
                    answer_pos[0] = col
                    answer_pos[1] = row
            else:
                if cost[row - 1][col] > cost[row][col]:
                    cost[row][col] = cost[row - 1][col]
                    dp[row][col] = dp[row - 1][col]

                if cost[row][col - 1] > cost[row][col]:
                    cost[row][col] = cost[row][col - 1]
                    dp[row][col] = dp[row][col - 1]

    print(cost[answer_pos[1]][answer_pos[0]])
    print(dp[answer_pos[1]][answer_pos[0]])
