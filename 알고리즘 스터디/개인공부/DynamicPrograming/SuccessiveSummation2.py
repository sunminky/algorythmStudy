# https://www.acmicpc.net/problem/13398

import sys

if __name__ == '__main__':
    n_number = int(sys.stdin.readline())
    numbers = tuple(map(int, sys.stdin.readline().split()))
    forawrd_sum = [0] * n_number
    reverse_sum = [0] * n_number
    answer = -100000000

    # 정방향 누적합
    forawrd_sum[0] = numbers[0]
    for i in range(1, n_number):
        forawrd_sum[i] = max(forawrd_sum[i-1], 0) + numbers[i]
    
    # 역방향 누적합
    reverse_sum[-1] = numbers[-1]
    for i in range(n_number - 2, -1, -1):
        reverse_sum[i] = max(reverse_sum[i+1], 0) + numbers[i]
    
    # 숫자 하나 뺐을 경우
    for i in range(n_number - 2):
        answer = max(answer, forawrd_sum[i] + reverse_sum[i+2])

    # 숫자를 하나도 안뺏을 경우와 비교
    answer = max(answer, max(forawrd_sum), max(reverse_sum))
    print(answer)
