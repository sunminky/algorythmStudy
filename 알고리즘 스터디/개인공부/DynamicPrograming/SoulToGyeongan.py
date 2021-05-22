# https://www.acmicpc.net/problem/14863
import sys

if __name__ == '__main__':
    n_path, limit = map(int, sys.stdin.readline().split())  # 도시의 개수, 시간제한
    cost = {0: 0}   # 현재 도시까지 {시간 : 비용} 저장

    for _ in range(n_path):
        time1, reward1, time2, reward2 = map(int, sys.stdin.readline().split())
        new_cost = dict()

        for c_time in cost:
            if c_time + time1 <= limit:
                new_cost[c_time + time1] = max(new_cost.get(c_time + time1, 0), cost[c_time] + reward1)
            if c_time + time2 <= limit:
                new_cost[c_time + time2] = max(new_cost.get(c_time + time2, 0), cost[c_time] + reward2)

        cost = new_cost

    print(max(cost.values()))
