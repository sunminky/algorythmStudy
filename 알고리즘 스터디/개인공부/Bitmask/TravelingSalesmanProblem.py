# https://www.acmicpc.net/problem/2098
import sys

n_node = int(sys.stdin.readline())
field = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n_node)]
all_visited = (1 << (n_node - 1)) - 1


def tsp(dp, cur_node, visited):
    if dp[cur_node][visited] is None:
        dp[cur_node][visited] = 16000001

        for i in range(n_node - 1):
            if visited & 1 << i:
                continue
            if field[cur_node][i + 1] == 0:
                continue
            dp[cur_node][visited] = min(dp[cur_node][visited], tsp(dp, i + 1, visited | 1 << i) + field[cur_node][i + 1])

    return dp[cur_node][visited]


if __name__ == '__main__':
    dp = [[None] * (1 << (n_node - 1)) for _ in range(n_node)]

    for row in range(n_node):
        dp[row][all_visited] = field[row][0] if field[row][0] else 16000001

    print(tsp(dp, 0, 0))
