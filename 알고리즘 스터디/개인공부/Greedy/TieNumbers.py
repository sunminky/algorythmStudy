# https://www.acmicpc.net/problem/1744

import sys

if __name__ == '__main__':
    numbers = [[], []]  #음수, 양수
    answer = 0
    
    for _ in range(int(sys.stdin.readline())):
        num = int(sys.stdin.readline())

        if num <= 0:
            numbers[0].append(num)
        elif num == 1:
            answer += 1
        else:
            numbers[1].append(num)

    numbers[0].sort()
    numbers[1].sort(reverse=True)
    
    if len(numbers[0]) & 1: #길이가 홀수 인 경우
        answer += numbers[0][-1]
        del numbers[0][-1]

    if len(numbers[1]) & 1: #길이가 홀수 인 경우
        answer += numbers[1][-1]
        del numbers[1][-1]

    # 음수에 대해 계산
    for i in range(len(numbers[0]) // 2):
        # 가장 작은 음수 * 그 다음으로 작은 음수 = 큰 양수
        answer += numbers[0][i * 2] * numbers[0][i * 2 + 1]

    # 양수에 대해 계산
    for i in range(len(numbers[1]) // 2):
        # 가장 큰 양수 * 그 다음으로 큰 양수 = 큰 양수
        answer += numbers[1][i * 2] * numbers[1][i * 2 + 1]

    print(answer)