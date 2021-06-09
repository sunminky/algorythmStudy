# https://www.acmicpc.net/problem/2923
import sys


def max_sum(arr1, arr2):
    result = 0
    arr2_idx = len(arr2) - 1
    arr2_remain = arr2[-1]  # 현재 arr2 인덱스에 해당하는 숫자의 등장횟수

    for i in range(1, len(arr1)):
        remain = arr1[i]

        while remain:
            if not arr2_remain:
                arr2_idx -= 1
                arr2_remain = arr2[arr2_idx]
                continue

            result = max(result, i + arr2_idx)

            if remain > arr2_remain:
                remain -= arr2_remain
                arr2_remain = 0
            else:
                arr2_remain -= remain
                remain = 0

    return result


if __name__ == '__main__':
    Array_A = [0] * 101
    Array_B = [0] * 101

    for _ in range(int(sys.stdin.readline())):
        A, B = map(int, sys.stdin.readline().split())
        Array_A[A] += 1
        Array_B[B] += 1

        print(max_sum(Array_A, Array_B))
