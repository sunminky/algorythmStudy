#https://www.acmicpc.net/problem/2839

import sys

if __name__ == '__main__':
    target = int(sys.stdin.readline())
    dp = [[j*3 + i*5 for j in range(target//3 + 1)] for i in range(target//5 + 1)]
    min_val = -1

    for r in range(len(dp)):
        for c in range(len(dp[r])):
            if dp[r][c] == target:
                if min_val == -1 or min_val > r + c:
                    min_val = r + c

    print(min_val)

    #dp가 아닌 풀이
    '''target = int(sys.stdin.readline())
    min_val = 1700

    for i in range(target // 5, -1, -1):
        unit5 = i
        unit3 = (target - 5 * i) / 3

        if unit3 == int(unit3):
            if min_val > int(unit3) + unit5:
                min_val = int(unit3) + unit5

    if min_val == 1700:
        print(-1)
    else:
        print(min_val)'''