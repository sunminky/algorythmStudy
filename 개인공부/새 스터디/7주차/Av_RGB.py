#https://www.acmicpc.net/problem/1149

#유사 문제#
#https://programmers.co.kr/learn/courses/30/lessons/12913

import sys

if __name__ == '__main__':
    residents = int(sys.stdin.readline())   #집의 개수
    painting_cost = []  #페인트 비용
    estimate = [[[0, 0], [1, 0], [2, 0]] for _ in range(residents)] #각 페인트를 선택했을 때 비용

    for _ in range(residents):
        painting_cost.append(tuple(map(int, sys.stdin.readline().split())))

    estimate[0] = tuple(zip([0, 1, 2], painting_cost[0]))   #맨 처음 집의 견적은 페인트 비용과 같음

    for i in range(1, len(estimate)):
        s_list_prev = sorted(estimate[i-1], key=lambda x:x[1])

        #위에 집과 색깔이 겹치면 그 다음으로 싼 페인트를 칠함
        estimate[i][0][1] = painting_cost[i][0] + s_list_prev[0][1] if s_list_prev[0][0] != 0 else painting_cost[i][0] + s_list_prev[1][1]
        estimate[i][1][1] = painting_cost[i][1] + s_list_prev[0][1] if s_list_prev[0][0] != 1 else painting_cost[i][1] + s_list_prev[1][1]
        estimate[i][2][1] = painting_cost[i][2] + s_list_prev[0][1] if s_list_prev[0][0] != 2 else painting_cost[i][2] + s_list_prev[1][1]

    print(min(estimate[-1], key=lambda x:x[1])[1])