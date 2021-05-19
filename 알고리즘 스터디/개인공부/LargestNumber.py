# https://www.acmicpc.net/problem/16496
import sys


# 최대 10자리 값 반환
def matching(values: list) -> list:
    matched = []
    max_digit = len(max(values, key=len)) + 1   # 가장 긴 숫자의 길이

    for value in values:
        calc = [value[0]] * max_digit   # 가장 맨 앞자리 값 * 가장 긴 숫자의 길이

        # 앞에서 부터 차례대로 넣어줌
        for i in range(len(value)):
            calc[i] = value[i]

        matched.append([int("".join(calc)), value])     # [변환 값, 입력받은 값]

    return matched


if __name__ == '__main__':
    sys.stdin.readline()    # 필요없음
    answer = [e[1] for e in sorted(matching(sys.stdin.readline().split()), key=lambda x: x[0], reverse=True)]
    print(int("".join(answer)))
