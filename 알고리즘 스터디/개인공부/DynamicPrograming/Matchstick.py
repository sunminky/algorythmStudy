# https://www.acmicpc.net/problem/3687
import sys
from math import ceil, log10


def get_biggest(cnt):
    if cnt & 1:
        return f"7{'1' * ((cnt - 3) // 2)}"

    return f"{'1' * (cnt // 2)}"


def get_smallest(cnt, dp):
    price = {2: 1, 3: 7, 4: 4, 5: 2, 6: 0, 7: 8}  # 가격별 숫자
    digit_length = ceil(cnt / 7)

    if dp[1][cnt] is not None:
        return dp[1][cnt]

    dp[0][cnt] = dp[1][cnt] = 999999999999999999999999999999999999999999999999999

    for i in range(2, 8):
        # 자리수 체크
        if ceil((cnt - i) / 7) + 1 > digit_length:
            continue

        # 음수 체크
        if cnt - i < 0:
            continue

        head = price[i]
        tail = get_smallest(cnt - i, dp)

        dp[0][cnt] = min((6 if head == 0 else head) * (10 ** (digit_length - 1)) + tail, dp[0][cnt])
        dp[1][cnt] = min(head * (10 ** (digit_length - 1)) + tail, dp[1][cnt])

    return dp[1][cnt]


if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        cnt = int(sys.stdin.readline())
        dp = [[None] * 101 for _ in range(2)]

        dp[1][2] = dp[0][2] = 1
        dp[1][3] = dp[0][3] = 7
        dp[1][4] = dp[0][4] = 4
        dp[1][5] = dp[0][5] = 2
        dp[1][6], dp[0][6] = 0, 6
        dp[1][7] = dp[0][7] = 8

        get_smallest(cnt, dp)

        print(dp[0][cnt], get_biggest(cnt))
