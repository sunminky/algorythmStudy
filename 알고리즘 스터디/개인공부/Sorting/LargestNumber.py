# https://www.acmicpc.net/problem/16496
# https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3
import sys


def matching(values: list) -> list:
    matched = []
    max_digit = len(max(values, key=len)) + 1  # 가장 긴 숫자의 길이

    for value in values:
        calc = [value[0]] * max_digit  # 가장 맨 앞자리 값 * 가장 긴 숫자의 길이

        # 앞에서 부터 차례대로 넣어줌
        for i in range(len(value)):
            calc[i] = value[i]

        matched.append([int("".join(calc)), value])  # [변환 값, 입력받은 값]

    return matched


if __name__ == '__main__':
    sys.stdin.readline()  # 필요없음
    answer = [e[1] for e in sorted(matching(sys.stdin.readline().split()),
                                   key=lambda x: (x[0], x[1][-1], -len(x[1])),  # 변환 값이 같을 경우 마지막 문자를 따라 정렬
                                   reverse=True)]
    print(int("".join(answer)))

## 다른 사람의 풀이 ##
# int(''.join(sorted(sys.stdin.readline().split(), key=lambda x: x*10, reverse=True)))
