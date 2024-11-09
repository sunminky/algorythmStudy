# https://school.programmers.co.kr/learn/courses/30/lessons/87946
from itertools import permutations


def solution(k, dungeons):
    answer = -1

    for e in permutations(dungeons):
        new_k = k
        cnt = 0

        for d in e:
            if d[0] <= new_k:
                cnt += 1
                new_k -= d[1]

        answer = max(answer, cnt)

    return answer


if __name__ == '__main__':
    solution(80, [[80, 20], [50, 40], [30, 10]])  # 3
