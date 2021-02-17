#https://www.acmicpc.net/problem/2228

import sys

if __name__ == '__main__':
    n_numbers, n_groups = tuple(map(int,sys.stdin.readline().split()))
    numbers = [int(sys.stdin.readline()) for _ in range(n_numbers)]
    values = [[None for _ in range(n_numbers)] for _ in range(n_groups)]    #구간 개수에 따른 값 저장, values[x][y] : x개의  구간을 가지고 y번째 까지 숫자를 담았을 때 값

    values[0][0] = numbers[0]   #구간이 1개이고 가장 첫번째 숫자만 구간에 포함한 경우

    #구간이 1개 인 경우
    for i in range(1, n_numbers):
        values[0][i] = max(numbers[i], values[0][i-1] + numbers[i]) #자기 자신만 구간에 포함, 이전까지 구간의 최대값 + 자기자신

    for r in range(1, n_groups):
        max_value = max(values[r-1][(r-1) * 2:r * 2 - 1])   #r-1개의 구간과 c-2까지의 원소를 가지고 만들 수 있는 최대값
        values[r][r*2] = max_value + numbers[r*2]   #r-1개의 구간과 c-2까지의 원소를 가지고 만들 수 있는 최대값 + 현재 위치의 값

        for c in range(r * 2 + 1, n_numbers):
            max_value = max(max_value, values[r-1][c - 2])
            values[r][c] = max(max_value, values[r][c-1]) + numbers[c]  #r-1개의 구간과 c-2까지의 최대값을 가지고 만들 수 있는 최대값, r개의 구간 중 맨마지막 구간에 현재원소 이어붙인 값 

    print(max(values[n_groups-1][(n_groups-1) * 2:]))