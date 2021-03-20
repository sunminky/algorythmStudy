# https://www.acmicpc.net/problem/2136

import sys

if __name__ == '__main__':
    N, total = map(int, sys.stdin.readline().split())
    ants = [int(sys.stdin.readline()) for _ in range(N)]
    sorted_ants = sorted(ants, key=abs)

    leftTime = -1
    rightTime = 0
    leftCnt = 0
    
    for i in range(N):
        # 개미가 오른쪽 끝 에서 떨어지는 최대시간
        if sorted_ants[i] > 0:
            if leftTime == -1:
                leftTime = total - sorted_ants[i]
        # 개미가 왼쪽 끝에서 떨어지는 최대시간
        if sorted_ants[i] < 0:
            leftCnt += 1
            rightTime = -sorted_ants[i]

    # 오른쪽으로 떨어지는 개미가 가장 늦음
    if leftTime > rightTime:
        print(ants.index(sorted_ants[leftCnt]) + 1, leftTime)
    # 왼쪽으로 떨어지는 개미가 가장 늦음
    else:
        print(ants.index(sorted_ants[leftCnt - 1]) + 1, rightTime)
