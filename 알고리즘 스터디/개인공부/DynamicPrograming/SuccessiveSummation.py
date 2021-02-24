#https://www.acmicpc.net/problem/1912

import sys

if __name__ == '__main__':
    sys.stdin.readline()    #필요없음
    numbers = tuple(map(int, sys.stdin.readline().split()))
    reward = [0 for _ in range(len(numbers))]   #i번째 원소까지 고려했을 때 구간합의 초대

    reward[0] = numbers[0]

    for i in range(1, len(numbers)):
        reward[i] = max(reward[i-1], 0) + numbers[i]    #max(이전 값 + 현재 숫자, 현재 숫자)

    print(max(reward))  #최대 구간 합 출력