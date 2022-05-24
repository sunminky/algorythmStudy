# https://www.acmicpc.net/problem/9465
import sys

if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        width = int(sys.stdin.readline())
        matrix = [tuple(map(int, sys.stdin.readline().split()))for _ in range(2)]
        max_value = [[0] * (width + 1) for _ in range(3)]

        for i in range(1, width + 1):
            max_value[0][i] = matrix[0][i - 1] + max(max_value[1][i - 1], max_value[2][i - 1])  # 첫번째 스티커
            max_value[1][i] = matrix[1][i - 1] + max(max_value[0][i - 1], max_value[2][i - 1])  # 두번째 스티커
            max_value[2][i] = max(max_value[0][i - 1], max_value[1][i - 1], max_value[2][i - 1])  # 이번턴은 안 뜯을거

        print(max(max_value[0][-1], max_value[1][-1], max_value[2][-1]))

