# https://school.programmers.co.kr/learn/courses/30/lessons/152995
def solution(scores):
    prev_max = -1
    wanho_score, wanho_scores = sum(scores[0]), scores[0]
    scores = sorted(scores, key=lambda x: (-x[0], x[1]))

    for e in scores:
        prev_max = max(prev_max, e[1])

        # 완호가 다른 사람보다 점수가 둘 다 작음
        if wanho_scores[0] < e[0] and wanho_scores[1] < e[1]:
            return -1

        # 다른 사람보다 점수가 둘 다 작음
        if e[1] < prev_max:
            e[0] = e[1] = -1

    return len(tuple(filter(lambda x: sum(x) > wanho_score, scores))) + 1


if __name__ == '__main__':
    print(solution([[2, 2], [1, 4], [3, 2], [3, 2], [2, 1]]))  # 4
    print(solution([[2, 2], [2, 2], [2, 3], [3, 2]]))  # 3
    print(solution([[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]))  # 1
    print(solution([[3, 1], [1, 4], [2, 3], [2, 3], [1, 5], [1, 0], [1, 0]]))  # 5
