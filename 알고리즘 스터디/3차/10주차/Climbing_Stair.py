#https://www.acmicpc.net/problem/2579

import sys

if __name__ == '__main__':
    n_stair = int(sys.stdin.readline())
    cost = [[0, 0, 0] for _ in range(n_stair + 2)]  #앞에 2행 패딩

    for i in range(2, n_stair + 2):
        stair = int(sys.stdin.readline())
        cost[i][0] = cost[i-1][1] + stair  #FTT
        cost[i][1] = cost[i-1][2] + stair  #TFT
        cost[i][2] = max(cost[i-1][0], cost[i-1][1])  #TTF, 두칸 연속뛰기 안됨
    print(max(cost[-1][:2]))    #마지막 계단은 무조건 밟아야 함(FTT 또는 TFT)