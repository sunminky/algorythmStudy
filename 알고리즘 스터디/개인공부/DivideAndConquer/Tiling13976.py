# https://www.acmicpc.net/problem/13976
import sys

matrix_dict = {0: ((1, 0), (0, 1)),
               1: ((4, -1), (1, 0))}


def multiple_matrix(cnt):
    if cnt in matrix_dict:
        return matrix_dict[cnt]

    matrix_a = multiple_matrix(cnt // 2)
    matrix_b = multiple_matrix(cnt - cnt // 2)
    matrix_dict[cnt] = (((matrix_a[0][0] * matrix_b[0][0] + matrix_a[0][1] * matrix_b[1][0]) % 1000000007,
                         (matrix_a[0][0] * matrix_b[0][1] + matrix_a[0][1] * matrix_b[1][1]) % 1000000007),
                        ((matrix_a[1][0] * matrix_b[0][0] + matrix_a[1][1] * matrix_b[1][0]) % 1000000007,
                         (matrix_a[1][0] * matrix_b[0][1] + matrix_a[1][1] * matrix_b[1][1]) % 1000000007))

    return matrix_dict[cnt]


if __name__ == '__main__':
    n = int(sys.stdin.readline())

    if n & 1:
        print(0)
    else:
        matrix = multiple_matrix(n // 2 - 1)

        print((matrix[0][0] * 3 + matrix[0][1] * 1) % 1000000007)
