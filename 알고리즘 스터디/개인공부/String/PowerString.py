# https://www.acmicpc.net/problem/4354
import sys


def kmp_table(text):
    table = [0] * len(text)
    j = 0

    for i in range(1, len(table)):
        while j > 0 and text[i] != text[j]:
            j = table[j - 1]
        if text[i] == text[j]:
            j += 1
            table[i] = j

    return table


if __name__ == '__main__':
    # text를 정의할 수 있는 가장 작은 문자열을 찾기
    while True:
        text = sys.stdin.readline().rstrip()

        if text == ".":
            break

        result = len(text) / (len(text) - kmp_table(text)[-1])

        if result - result // 1 == 0:
            print(int(result))
        else:
            print(1)
