# https://www.acmicpc.net/problem/10835
# pypy3는 python보다 메모리를 많이 사용한다
import sys

sys.setrecursionlimit(1000000)

n_card = int(sys.stdin.readline())
left = tuple(map(int, sys.stdin.readline().split()))
right = tuple(map(int, sys.stdin.readline().split()))
dp = [[-1] * n_card for _ in range(n_card)]


def calc(l_idx, r_idx):
    if l_idx >= n_card or r_idx >= n_card:
        return 0

    if dp[l_idx][r_idx] != -1:
        return dp[l_idx][r_idx]

    if left[l_idx] > right[r_idx]:
        dp[l_idx][r_idx] = calc(l_idx, r_idx + 1) + right[r_idx]
    else:
        dp[l_idx][r_idx] = max(calc(l_idx + 1, r_idx), calc(l_idx + 1, r_idx + 1))

    return dp[l_idx][r_idx]


if __name__ == '__main__':
    calc(0, 0)
    print(dp[0][0])
