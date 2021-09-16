# https://www.acmicpc.net/problem/1029
import sys

n_artist = int(sys.stdin.readline())
price = [[int(e) for e in sys.stdin.readline().rstrip()] for _ in range(n_artist)]
cost = [[[-1] * 10 for _ in range(1 << n_artist)] for _ in range(n_artist)]


def tsp(visited, cur, bid):
    # 이미 계산됬으면 패스
    if cost[cur][visited][bid] == -1:
        cost[cur][visited][bid] = 1

        for other in range(n_artist):
            # 이미 방문했으면 패스
            if visited & (1 << other):
                continue

            # 돈을 더 주고 팔 수 없으면 패스
            if bid > price[cur][other]:
                continue

            cost[cur][visited][bid] = max(cost[cur][visited][bid],
                                          tsp(visited | (1 << other), other, price[cur][other]) + 1)

    return cost[cur][visited][bid]


if __name__ == '__main__':
    print(tsp(1 << 0, 0, 0))
