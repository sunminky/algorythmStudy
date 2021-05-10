# https://www.acmicpc.net/problem/1450
import sys
from bisect import bisect_right


# 냅섹
def case(start, end, pack, limit) -> dict:
    cost = dict()

    for i in range(start, end):
        prev_cost = cost.copy()

        for k in prev_cost.keys():
            if k + pack[i] <= limit:
                cost[k + pack[i]] = cost.get(k + pack[i], 0) + prev_cost[k]

        if pack[i] <= limit:
            cost[pack[i]] = cost.get(pack[i], 0) + 1

    cost[0] = 1
    return cost


if __name__ == '__main__':
    n_pack, limit = map(int, sys.stdin.readline().split())
    pack = [*map(int, sys.stdin.readline().split())]

    cost1 = case(0, len(pack) // 2, pack, limit)  # 반절의 물건만 가방에 넣는 것을 고려함
    cost2 = case(len(pack) // 2, len(pack), pack, limit)  # 나머지 반절의 물건만 가방에 넣는 것을 고려함
    cost2 = dict(sorted(cost2.items(), key=lambda x: x[0]))  # 키를 오름차순 정렬
    cost2_keys = list(cost2.keys())  # cost2 키 값
    cost2_acc = [0] * len(cost2)  # 0 ~ 키 값까지 누적합 저장

    # 누적합 만들기
    for seq, key in enumerate(cost2.keys()):
        if seq == 0:
            cost2_acc[seq] = cost2[key]
        else:
            cost2_acc[seq] = cost2_acc[seq - 1] + cost2[key]

    answer = 0
    for k1 in cost1.keys():
        # limit - k1 보다 작은 cost2의 키 중 가장 큰 키의 경우의 수를 구해서 k1의 경우의 수와 곱함
        answer += cost1[k1] * cost2_acc[max(0, min(bisect_right(cost2_keys, limit - k1) - 1, len(cost2_keys) - 1))]

    print(answer)
