#https://www.acmicpc.net/problem/13397

import sys

if __name__ == '__main__':
    n_numbers, n_group = tuple(map(int, sys.stdin.readline().split()))
    numbers = tuple(map(int, sys.stdin.readline().split()))
    prev_division_cost = None    #division_cost[y][x] : y개의 구간으로 x까지 담았을 때 구간 값
    cur_division_cost = [0 for _ in range(n_numbers)]  # division_cost[y][x] : y개의 구간으로 x까지 담았을 때 구간 값

    #첫 번째 구간 값 계산
    min_val = max_val = numbers[0]
    for c in range(n_numbers):
        max_val = max(max_val, numbers[c])
        min_val = min(min_val, numbers[c])
        cur_division_cost[c] = max_val - min_val

    #첫 번째 이후 구간 값 계산
    for g in range(1, n_group):
        print(cur_division_cost)
        prev_division_cost = cur_division_cost.copy()
        min_val = max_val = numbers[g]
        for c in range(g, n_numbers):
            max_val = max(max_val, numbers[c])
            min_val = min(min_val, numbers[c])
            v1 = prev_division_cost[c-1] + 0    #g-1개 까지의 그룹으로 만든 최대값 + g번째 그룹이 나혼자인 경우(구간 값 0)
            v2 = max(cur_division_cost[c-1], max_val-min_val)    #g번째 그룹에 현재 원소를 추가하는 경우

            if v1 < v2:
                cur_division_cost[c] = v1
                max_val = min_val = numbers[c]  #g번째 그룹이 새로 시작하므로 최대값과 최소값 갱신
            else:
                cur_division_cost[c] = v2

    print(cur_division_cost)
    print(cur_division_cost[n_numbers-1])
