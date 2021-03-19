# https://www.acmicpc.net/problem/13305

import sys

if __name__ == '__main__':
    n_gasStation = int(sys.stdin.readline())
    distance = list(map(int, reversed(sys.stdin.readline().split())))
    cost_dict = dict()  #기름가격별 도착지에서 가장 먼 노드 저장
    max_distance = 0    #출발지에서 도착지의 거리
    cur_loc = 0
    answer = 0

    for seq, _cost in enumerate(map(int, reversed(sys.stdin.readline().split()[:-1]))):
        max_distance += distance[seq]   #도착지까지의 거리
        cost_dict[_cost] = max_distance

    #기름 가격이 싼 순서대로 탐색
    for k in sorted(cost_dict.keys()):
        #이전에 기름 넣었던 위치보다 더 멀어진 경우
        if cost_dict[k] > cur_loc:
            answer += k * (cost_dict[k] - cur_loc)
            cur_loc = cost_dict[k]

            # 출발지에 도착하면 종료
            if cur_loc == max_distance:
                break

    print(answer)
