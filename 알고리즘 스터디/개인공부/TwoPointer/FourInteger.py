# https://www.acmicpc.net/problem/7453
import sys


def get_matrix(matrix1, matrix2):
    result = []

    for e1 in matrix1:
        for e2 in matrix2:
            result.append(e1 + e2)

    return sorted(result)


if __name__ == '__main__':
    n_matrix = int(sys.stdin.readline())
    matrix = [[0] * n_matrix for _ in range(4)]
    answer = 0

    for idx in range(n_matrix):
        for seq, e in enumerate(map(int, sys.stdin.readline().split())):
            matrix[seq][idx] = e

    ab_matrix = get_matrix(matrix[0], matrix[1])
    cd_matrix = get_matrix(matrix[2], matrix[3])
    pointer1, pointer2 = 0, len(cd_matrix) - 1

    while pointer1 < len(ab_matrix) and 0 <= pointer2:
        summation = ab_matrix[pointer1] + cd_matrix[pointer2]

        if summation == 0:
            ab_cnt, cd_cnt = pointer1, pointer2

            while ab_cnt < len(ab_matrix) and ab_matrix[ab_cnt] == ab_matrix[pointer1]:
                ab_cnt += 1

            while 0 <= cd_cnt and cd_matrix[cd_cnt] == cd_matrix[pointer2]:
                cd_cnt -= 1

            answer += (ab_cnt - pointer1) * (pointer2 - cd_cnt)
            pointer1, pointer2 = ab_cnt, cd_cnt

        elif summation < 0:
            pointer1 += 1
        else:
            pointer2 -= 1

    print(answer)
