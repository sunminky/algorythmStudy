# https://www.acmicpc.net/problem/11062

import sys


# min-max 알고리즘
def search(card, start, end, player, memo):
    # 이미 계산한 적이 있는 경우
    if memo[player][start][end] != -1:
        return memo[player][start][end]

    # 기저조건
    if start == end:
        if player == 0:  # 플레이어가 근수 인 경우
            memo[player][start][end] = card[start]
            return card[start]

        memo[player][start][end] = 0
        return 0

    if player == 0:
        memo[player][start][end] = \
            max(search(card, start + 1, end, player ^ 1, memo) + card[start],
                search(card, start, end - 1, player ^ 1, memo) + card[end])
        return memo[player][start][end]

    memo[player][start][end] = \
        min(search(card, start + 1, end, player ^ 1, memo),
            search(card, start, end - 1, player ^ 1, memo))

    return memo[player][start][end]


if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        sys.stdin.readline()  # 카드의 개수, 필요없음
        card = [*map(int, sys.stdin.readline().split())]

        print(search(card, 0, len(card) - 1, 0,
                     [
                         [
                             [-1 for _ in range(len(card))]
                             for _ in range(len(card))
                         ]
                         for _ in range(2)
                     ]
                     )
              )  # 전체 카드중 0(근수)가 얻을 수 있는 점수의 최대값
