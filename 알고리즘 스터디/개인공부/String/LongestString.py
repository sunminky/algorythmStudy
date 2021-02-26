#https://www.acmicpc.net/problem/3033

import sys


def rabinkarp(string : str, digit : int) -> bool:
    dup_dict = dict()
    demo2 = 1 << (digit-1)
    demo3 = 3 ** (digit-1)
    value = sum([ord(string[i]) * 1 << i for i in range(digit)])
    value2 = sum([ord(string[i]) * 3**i for i in range(digit)])
    dup_dict[value] = (True, [value2])

    for i in range(1, len(string) - digit + 1):
        value = (value - ord(string[i-1])) // 2 + ord(string[i + digit - 1]) * demo2
        value2 = (value2 - ord(string[i - 1])) // 3 + ord(string[i + digit - 1]) * demo3
        if not dup_dict.get(value, False):
            dup_dict[value] = (True, [value2])
        else:
            if value2 in dup_dict[value][1]:
                return True
            else:
                dup_dict[value][1].append(value2)

    return False


if __name__ == '__main__':
    sys.stdin.readline()    #필요없음
    string = sys.stdin.readline().rstrip()
    min_val = 1
    max_val = len(string) // 2 + 1
    answer = min_val

    while min_val < max_val:
        middle = (min_val + max_val) // 2

        if rabinkarp(string, middle):
            min_val = middle + 1
            answer = middle
        else:
            max_val = middle

    print(answer)