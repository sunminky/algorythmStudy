#https://www.acmicpc.net/problem/1940

import sys

if __name__ == '__main__':
    sys.stdin.readline()    #필요없음
    goal = int(sys.stdin.readline())
    materials = sorted(list(map(int, sys.stdin.readline().split())))

    s_idx = 0
    e_idx = len(materials) - 1
    answer = 0

    while s_idx < e_idx:
        armor = materials[s_idx] + materials[e_idx]

        if armor > goal:
            e_idx -= 1
        elif armor < goal:
            s_idx += 1
        elif armor == goal:
            answer += 1
            s_idx += 1
            e_idx -= 1

    print(answer)