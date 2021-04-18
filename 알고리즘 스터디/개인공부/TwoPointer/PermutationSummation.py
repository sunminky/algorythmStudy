# https://www.acmicpc.net/problem/2143

import sys


# 누적합 구하기
def accumulation(number):
    result = dict()

    for i in range(len(number)):
        total = 0
        for j in range(i, len(number)):
            total += number[j]
            result[total] = result.get(total, 0) + 1    # 이 부분합이 나올 수 있는 경우의 수를 구함

    return result


if __name__ == '__main__':
    target = int(sys.stdin.readline())
    sys.stdin.readline()
    arr1 = [*map(int, sys.stdin.readline().split())]    # 배열1
    acc1 = accumulation(arr1)   # 배열1의 부분합의 등장 횟수
    sys.stdin.readline()
    arr2 = [*map(int, sys.stdin.readline().split())]    # 배열2
    acc2 = accumulation(arr2)   # 배열2의 부분합의 등장 횟수
    acc1_key = sorted(acc1.keys())  # 배열1의 부분합 정렬
    acc2_key = sorted(acc2.keys())  # 배열2의 부분합 정렬
    answer = 0

    ## 투포인터 ##
    a1_idx = 0
    a2_idx = len(acc2_key) - 1
    while a1_idx < len(acc1_key) and a2_idx >= 0:
        calc = acc1_key[a1_idx] + acc2_key[a2_idx]  # 두 부분합의 합

        # 타겟인 경우
        if calc == target:
            answer += acc1[acc1_key[a1_idx]] * acc2[acc2_key[a2_idx]]

        if calc <= target:
            a1_idx += 1
        else:
            a2_idx -= 1

    print(answer)