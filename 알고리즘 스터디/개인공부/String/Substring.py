# https://www.acmicpc.net/problem/16916
import sys


###KMP###
def maketable(text: str) -> list:
    j = 0
    table = [0] * len(text)

    for i in range(1, len(pattern)):
        while j > 0 and text[i] != text[j]:
            j = table[max(0, j - 1)]

        if text[i] == text[j]:
            table[i] = j + 1
            j += 1

    return table


def kmp(target: str, pattern: str) -> bool:
    table = maketable(pattern)
    j = 0

    for i in range(len(target)):
        while j > 0 and target[i] != pattern[j]:
            j = table[j - 1]

        if target[i] == pattern[j]:
            j += 1

        if j == len(pattern):
            return True

    return False


###보이어 무어###
def make_idxtable(text: str) -> dict:
    word_dict = dict()

    # 알파벳별로 가장 오른쪽에 있는 값을 저장
    for seq, ch in enumerate(text):
        word_dict[ch] = seq

    return word_dict


def boyermoore(target: str, pattern: str) -> bool:
    idx_table = make_idxtable(pattern)
    i = len(pattern) - 1

    while i < len(target):
        # 뒤에서 부터 비교
        for seq in range(len(pattern)):
            # 일치하지 않는 문자 발견
            if target[i - seq] != pattern[-seq - 1]:
                # 패턴 중 일치하는 문자가 없는 경우
                if target[i - seq] not in idx_table:
                    i = i - seq + 1 + len(pattern) - 1
                # 패턴 중 일치하는 문자가 있는 경우
                else:
                    i = max(i - seq + len(pattern) - idx_table[target[i - seq]] - 1, i + 1)

                break
        else:
            return True

    return False


if __name__ == '__main__':
    target = sys.stdin.readline().rstrip()
    pattern = sys.stdin.readline().rstrip()

    # KMP
    result = kmp(target, pattern)

    # print(int(result))

    # 보이어무어
    # result = boyermoore(target, pattern)

    print(int(result))
