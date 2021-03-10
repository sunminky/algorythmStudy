# https://www.acmicpc.net/problem/11780

import sys

if __name__ == '__main__':
    n_city = int(sys.stdin.readline())
    n_bus = int(sys.stdin.readline())
    cost_table = [[0 for _ in range(n_city)] for _ in range(n_city)]  # 비용 저장
    path_table = [[list() for _ in range(n_city)] for _ in range(n_city)]  # 경로 저장

    for _ in range(n_bus):
        src, dst, cost = map(int, sys.stdin.readline().split())
        if cost_table[src - 1][dst - 1] == 0 or cost_table[src - 1][dst - 1] > cost:
            cost_table[src - 1][dst - 1] = cost
            path_table[src - 1][dst - 1] = [src - 1, dst - 1]

    # 플로이드 와샬
    for passby in range(n_city):
        for row in range(n_city):
            if cost_table[row][passby] == 0:
                continue
            for col in range(n_city):
                if cost_table[passby][col] == 0 or row == col:
                    continue
                if cost_table[row][col] == 0 or cost_table[row][col] > cost_table[row][passby] + cost_table[passby][
                    col]:
                    cost_table[row][col] = cost_table[row][passby] + cost_table[passby][col]
                    path_table[row][col] = path_table[row][passby] + path_table[passby][col][1:]

    # 비용 출력
    for ctr in cost_table:
        for ctc in ctr:
            print(ctc, end=" ")
        print()

    # 경로 출력
    for ptr in path_table:
        for ptc in ptr:
            if ptc == []:
                print(0)
            else:
                print(len(ptc), end=" ")
                for e in ptc:
                    print(e + 1, end=" ")
                print()