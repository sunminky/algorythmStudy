# https://www.acmicpc.net/problem/1509
import sys


if __name__ == '__main__':
    text = sys.stdin.readline().rstrip()
    memo = [[0] * len(text) for _ in range(len(text))]
    answer = [2500] * len(text)

    for col in range(len(text)):
        for row in range(len(text) - col):
            if not col:
                memo[row][row + col] = 1
                continue

            if text[row] == text[row + col] and memo[row + 1][row + col - 1] != -1:
                memo[row][row + col] = memo[row + 1][row + col - 1] + 2
            else:
                memo[row][row + col] = -1

    for col in range(len(text)):
        for row in range(col + 1):
            if memo[row][col] != -1:
                if col - memo[row][col] >= 0:
                    answer[col] = min(answer[col], answer[col - memo[row][col]] + 1)
                else:
                    answer[col] = min(answer[col], 1)

    print(answer[-1])
