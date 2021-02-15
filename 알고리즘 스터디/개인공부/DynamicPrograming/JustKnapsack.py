#https://www.acmicpc.net/problem/12865

import sys

if __name__ == '__main__':
    n_equipments, capability = tuple(map(int, sys.stdin.readline().split()))
    costs = [-1 for _ in range(capability+1)]   #현재 물건을 담거나 담지않았을 때 비용 계산
    costs[0] = 0    #아무 것도 안 넣었을 때 무게와 가치는 0

    for _ in range(n_equipments):
        prev = costs.copy() #이전 비용을 저장한 리스트
        weight, value = tuple(map(int, sys.stdin.readline().split()))    #무게, 가치

        for i in range(capability+1):
            if prev[i] != -1:
                #최대값 갱신
                if i + weight <= capability and prev[i+weight] < value + prev[i]:
                    costs[i+weight] = value + prev[i]

    print(max(costs))
