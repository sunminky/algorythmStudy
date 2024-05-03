# https://school.programmers.co.kr/learn/courses/30/lessons/181188
def solution(targets):
    answer = 0
    cur_pos = -1

    for _src, _dst in sorted(targets, key=lambda x: (x[1], x[0])):
        if cur_pos <= _src:
            answer += 1
            cur_pos = _dst

    return answer


if __name__ == '__main__':
    solution([[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]])  # 3
    solution([[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4], [10, 11]])  # 4
