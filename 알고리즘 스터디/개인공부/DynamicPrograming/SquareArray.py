# https://www.acmicpc.net/problem/10830
import sys
from math import log2


def mul_matrix(m1, m2):
    result = [[0] * matrix_size for _ in range(matrix_size)]

    for row in range(matrix_size):
        for col in range(matrix_size):
            # 행렬 곱
            for idx in range(matrix_size):
                result[row][col] = (result[row][col] + m1[row][idx] * m2[idx][col]) % 1000

    return result


def divide(cnt):
    # 2의 제곱수인 경우
    if log2(cnt) % 1 == 0:
        return memo[int(log2(cnt))]

    # 2의 제곱수가 아닌 경우
    square_number = int(log2(cnt))

    return mul_matrix(divide(1 << square_number), divide(cnt - (1 << square_number)))


if __name__ == '__main__':
    matrix_size, mul_cnt = map(int, sys.stdin.readline().split())
    memo = [None] * 37
    memo[0] = [list(map(lambda x: int(x) % 1000, sys.stdin.readline().split())) for _ in range(matrix_size)]

    for i in range(1, 37):
        memo[i] = mul_matrix(memo[i - 1], memo[i - 1])

    for e in divide(mul_cnt):
        print(' '.join(map(str, e)))
