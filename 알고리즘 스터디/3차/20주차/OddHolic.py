# https://www.acmicpc.net/problem/20164

import sys


def divide(number, max_memo: dict, min_memo: dict):
    odd_cnt = sum([int(digit) & 1 for digit in number])  # 홀수 개수 세기

    # 기저조건, 글자수가 한자리
    if len(number) == 1:
        if max_memo.get(number, False) is False or min_memo.get(number, False) is False:
            max_memo[number] = odd_cnt
            min_memo[number] = odd_cnt

        return min_memo[number], max_memo[number]

    # 글자수가 2자리
    elif len(number) == 2:
        if max_memo.get(number, False) is False or min_memo.get(number, False) is False:
            min_memo[number], max_memo[number] = divide(str(int(number[0]) + int(number[1])), max_memo, min_memo)
            min_memo[number] += odd_cnt
            max_memo[number] += odd_cnt

        return min_memo[number], max_memo[number]

    # 글자수가 3자리 이상
    else:
        if max_memo.get(number, False) is False:
            for p1 in range(len(number)):
                for p2 in range(p1 + 1, len(number) - 1):
                    combination = str(int(number[:p1 + 1]) + int(number[p1 + 1:p2 + 1]) + int(number[p2 + 1:]))

                    if max_memo.get(combination, False) is False or min_memo.get(combination, False) is False:
                        min_memo[combination], max_memo[combination] = divide(combination, max_memo, min_memo)

                    min_val, max_val = divide(combination, max_memo, min_memo)

                    max_memo[combination] = max(max_memo[combination], max_val)
                    min_memo[combination] = min(min_memo[combination], min_val)

                    if max_memo.get(number, False) is False or min_memo.get(number, False) is False:
                        max_memo[number] = max_memo[combination] + odd_cnt
                        min_memo[number] = min_memo[combination] + odd_cnt

                    max_memo[number] = max(max_memo[number], max_memo[combination] + odd_cnt)
                    min_memo[number] = min(min_memo[number], min_memo[combination] + odd_cnt)

        return min_memo[number], max_memo[number]


if __name__ == '__main__':
    number = sys.stdin.readline().rstrip()

    print(" ".join(map(str, divide(number, dict(), dict()))))
