#https://www.acmicpc.net/problem/12015

import sys
from bisect import bisect_right

if __name__ == '__main__':
    n_number = int(sys.stdin.readline())
    indices = [0 for _ in range(n_number)]
    numbers = [0 for _ in range(n_number)]
    cost = [0 for _ in range(n_number)]
    queue = []

    for seq, item in enumerate(sorted(list([num, seq] for seq, num in enumerate(map(int, sys.stdin.readline().split()))), key=lambda x:(x[0], x[1]))):
        numbers[seq] = item[0]
        indices[seq] = item[1]

    min_val = numbers[0]
    m_idx = 0

    print(numbers)
    print(indices)

    #제일 작은 값 비용 채워주기
    for i in range(len(numbers)):
        m_idx = i
        if numbers[i] == min_val:
            cost[i] = 1
        else:
            break

    prev_val = -1
    for i in range(m_idx, len(numbers)):
        if prev_val == numbers[i]:
            cost[i] = cost[i-1]
        else:
            print(bisect_right(indices[:i], indices[i])-1, i)
            cost[i] = cost[bisect_right(indices[:i], indices[i])-1] + 1

        prev_val = numbers[i]

    print(cost)
