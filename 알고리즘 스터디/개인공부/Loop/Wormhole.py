# https://www.acmicpc.net/problem/1865
import sys


def BellmanFord(n_point, costs, paths):
    for i in range(n_point):
        for cur, path in enumerate(paths):
            for key in path.keys():
                if costs[key] > costs[cur] + path[key]:
                    costs[key] = costs[cur] + path[key]

    for cur, path in enumerate(paths):
        for key in path.keys():
            if costs[key] > costs[cur] + path[key]:
                return True

    return False


if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        n_point, n_road, n_wormhole = map(int, sys.stdin.readline().split())
        paths = [dict() for _ in range(n_point)]
        costs = [10000001] * n_point

        for _ in range(n_road):
            src, dst, cost = map(int, sys.stdin.readline().split())

            paths[src - 1][dst - 1] = min(paths[src - 1].get(dst - 1, 10000), cost)
            paths[dst - 1][src - 1] = min(paths[dst - 1].get(src - 1, 10000), cost)

        for _ in range(n_wormhole):
            src, dst, cost = map(int, sys.stdin.readline().split())

            paths[src - 1][dst - 1] = min(paths[src - 1].get(dst - 1, 10000), -cost)

        print("YES" if BellmanFord(n_point, costs, paths) else "NO")
