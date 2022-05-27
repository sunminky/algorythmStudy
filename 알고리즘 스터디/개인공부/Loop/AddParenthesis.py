# https://www.acmicpc.net/problem/16637
import sys

formula_len = int(sys.stdin.readline())
formula = sys.stdin.readline().rstrip()


def calc(x, op, y):
    if op == '+':
        return int(x) + int(y)
    if op == '-':
        return int(x) - int(y)
    if op == '*':
        return int(x) * int(y)


def dig(idx, tied, acc, prev_acc):
    result = -1000000000

    if idx >= formula_len:
        return acc

    # 이전 것과 합치기
    if idx >= 2 and not tied:
        if idx < 4:
            result = max(result, dig(idx + 2, True, calc(formula[idx - 2], formula[idx - 1], formula[idx]), acc))
        else:
            result = max(result, dig(idx + 2, True,
                                     calc(prev_acc, formula[idx - 3],
                                          calc(formula[idx - 2], formula[idx - 1], formula[idx])), acc))

    # 합치치 않기
    if idx >= 2:
        result = max(result, dig(idx + 2, False, calc(acc, formula[idx - 1], formula[idx]), acc))
    else:
        result = max(result, dig(idx + 2, False, calc(acc, '+', formula[idx]), acc))

    return result


if __name__ == '__main__':
    print(dig(0, False, 0, 0))
