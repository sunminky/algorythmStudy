# https://school.programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):
    answer = n
    cloth = [1] * n

    for l in lost:
        cloth[l - 1] -= 1

    for r in reserve:
        cloth[r - 1] += 1

    for l in sorted(lost):
        if cloth[l - 1]:
            continue

        if 0 <= l - 1 - 1 and cloth[l - 1 - 1] > 1:
            cloth[l - 1 - 1] -= 1
            continue

        if n > l + 1 - 1 and cloth[l + 1 - 1] > 1:
            cloth[l + 1 - 1] -= 1
            continue

        answer -= 1

    return answer


if __name__ == '__main__':
    solution(5, [2, 4], [1, 3, 5])  # 5
    solution(5, [2, 4], [3])  # 4
    solution(5, [4, 2], [3, 5])  # 5
