# https://school.programmers.co.kr/learn/courses/30/lessons/152996
from collections import Counter


def solution(weights):
    answer = 0
    count = Counter(weights)
    weights = set(weights)
    multiple = (2 / 3, 2 / 4, 3 / 4)

    for _, _cnt in count.items():
        answer += _cnt * (_cnt - 1) // 2

    for _weight in weights:
        for _multiple in multiple:
            answer += count[_weight] * count.get(_weight * _multiple, 0)

    return answer


if __name__ == '__main__':
    print(solution([100, 180, 360, 100, 270]))  # 4
