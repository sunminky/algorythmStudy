#https://www.acmicpc.net/problem/9252
#레벤슈타인 거리

import sys

if __name__ == '__main__':
    text = [sys.stdin.readline().rstrip() for _ in range(2)]
    cost = [0 for _ in range(len(text[0]))]
    common_string = [[] for _ in range(len(text[0]))]

    for i in range(len(text[1])):
        prev_cost = cost.copy()
        prev_cs = common_string.copy()

        if text[0][0] == text[1][i]:
            cost[0] = 1
            common_string[0] = [text[1][i]]
        else:
            cost[0] = prev_cost[0]
            common_string[0] = prev_cs[0]

        for j in range(1, len(cost)):
            if text[1][i] == text[0][j]:
                cost[j] = prev_cost[j-1] + 1
                common_string[j] = prev_cs[j-1] + [text[1][i]]
            else:
                if prev_cost[j] > cost[j-1]:
                    cost[j] = prev_cost[j]
                    common_string[j] = prev_cs[j]
                else:
                    cost[j] = cost[j-1]
                    common_string[j] = common_string[j-1]

    print(cost[-1])
    print("".join(common_string[-1]))