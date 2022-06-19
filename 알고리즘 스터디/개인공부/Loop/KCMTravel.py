# https://www.acmicpc.net/problem/10217
import sys

if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        n_airport, budget, n_ticket = map(int, sys.stdin.readline().split())
        edges = [list() for _ in range(n_airport)]
        cost = [dict() for _ in range(n_airport)]
        answer = 100001

        for _ in range(n_ticket):
            _src, _dst, _fee, _time = map(int, sys.stdin.readline().split())
            edges[_src - 1].append([_dst - 1, _fee, _time])

        for e in edges:
            e.sort(key=lambda x: x[2])

        cost[0][0] = 0

        for cur_budget in range(budget + 1):
            for node in range(n_airport):
                if cur_budget not in cost[node]:
                    continue

                cur_time = cost[node][cur_budget]

                for _dst, _fee, _time in edges[node]:
                    if cur_time + _time >= answer:
                        break

                    if cur_budget + _fee > budget:
                        continue

                    cost[_dst][cur_budget + _fee] = min(cost[_dst].get(cur_budget + _fee, 100001), cur_time + _time)

                    if _dst == n_airport - 1:
                        answer = min(cost[_dst][cur_budget + _fee], answer)

        if not cost[-1]:
            print("Poor KCM")
        else:
            print(answer)
