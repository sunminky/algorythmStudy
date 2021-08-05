# https://www.acmicpc.net/problem/14889
import sys
from itertools import combinations

if __name__ == '__main__':
    n_member = int(sys.stdin.readline())
    cost = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n_member)]
    answer = 4000

    for team in combinations(range(n_member), n_member // 2):
        flag = [0] * n_member
        ability = [0, 0]

        for mem in team:
            flag[mem] = 1

        for i in range(n_member):
            for j in range(n_member):
                if flag[j] == flag[i]:
                    ability[flag[i]] += cost[i][j]

        answer = min(answer, abs(ability[0] - ability[1]))

    print(answer)

    '''
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    each = [sum(x) + sum(y) for x, y in zip(arr, zip(*arr))]
    total = sum(each) // 2
    
    print(min(abs(total - sum(each[e] for e in c)) for c in combinations(range(1, n), n // 2)))
    '''
