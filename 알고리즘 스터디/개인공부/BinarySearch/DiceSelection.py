# https://school.programmers.co.kr/learn/courses/30/lessons/258709
from itertools import combinations, product
from bisect import bisect_right


def solution(dice):
    n_dice = len(dice)
    dice.append([0])
    answer = [-1, None]  # 승리 횟수, 조합

    for _case in combinations(range(n_dice), n_dice // 2):
        comb = [i if i not in _case else -1 for i in range(n_dice)]
        carr = sorted((sum(ee) for ee in product(*(dice[e] for e in comb))))
        win_cnt = 0

        for e in (sum(ee) for ee in product(*(dice[e] for e in _case))):
            win_cnt += bisect_right(carr, e - 1)

        if answer[0] < win_cnt:
            answer[0] = win_cnt
            answer[1] = _case

    return list(map(lambda x: x + 1, answer[1]))


if __name__ == '__main__':
    solution([[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]])  # [1, 4]
    solution([[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]])  # [2]
    solution(
        [[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]])  # [1, 3]
