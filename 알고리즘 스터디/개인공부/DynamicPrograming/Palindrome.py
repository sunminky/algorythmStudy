# https://www.acmicpc.net/problem/2079

import sys

if __name__ == '__main__':
    target = sys.stdin.readline().rstrip()
    palindrome_avail = [[1] * len(target) for _ in range(len(target))]  # 팰른드롬 여부 저장
    partition_cost = [0] + [len(target)] * len(target)

    # 팰린드롬 여부 구하기
    for col in range(1, len(target)):
        for row in range(len(target) - col):
            if target[row] == target[row + col]:
                palindrome_avail[row][row + col] = palindrome_avail[row + 1][row + col - 1]
            else:
                palindrome_avail[row][row + col] = 0

    # 현재위치까지 고려했을 때 팰린드롬의 최소개수 저장
    for col in range(1, len(target) + 1):
        for row in range(col):
            # row 까지 하나의 팰린드롬이 있다면 partition_cost[row - 1]에 1(현재 위치를 포함하는 팰린드롬의 수)을 더한 값
            if palindrome_avail[row][col - 1] == 1:
                partition_cost[col] = min(partition_cost[col], partition_cost[row] + 1)

    print(partition_cost[-1])
