# https://www.acmicpc.net/problem/6531
import sys


def find_comma(text) -> list:
    result = []

    for i in range(len(text)):
        if text[i] == ",":
            result.append(i)

    return result


def is_set(set_dp, text, comma, start, end) -> bool:
    if set_dp[start][end] is not None:
        return set_dp[start][end]

    if text[start] == "{" and text[end] == "}":
        if start + 1 == end:
            set_dp[start][end] = True
            return True

        if start + 2 == end:
            set_dp[start][end] = True
            return True

        if is_set(set_dp, text, comma, start + 1, end - 1):
            set_dp[start][end] = True
            return True

        set_dp[start][end] = False

        # 콤마단위로 구분
        for e in comma:
            if start + 1 <= e <= end - 1:
                if is_element(set_dp, text, comma, start + 1, e - 1) and is_element(set_dp, text, comma,
                                                                                    e + 1, end - 1):
                    set_dp[start][end] = True
                    break

    return set_dp[start][end]


def is_element(set_dp, text, comma, start, end) -> bool:
    if set_dp[start][end] is not None:
        return set_dp[start][end]

    if start > end:
        set_dp[start][end] = False
        return False

    if start == end:
        set_dp[start][end] = True
        return True

    if is_set(set_dp, text, comma, start, end):
        return True

    set_dp[start][end] = False

    # 콤마단위로 구분
    for e in comma:
        if start <= e <= end:
            if is_element(set_dp, text, comma, start, e - 1) and is_element(set_dp, text, comma,
                                                                            e + 1, end):
                set_dp[start][end] = True
                break

    return set_dp[start][end]


if __name__ == '__main__':
    for seq in range(int(sys.stdin.readline())):
        text = sys.stdin.readline().rstrip()
        comma = find_comma(text)
        set_dp = [[None for _ in range(len(text))] for _ in range(len(text))]

        if is_set(set_dp, text, comma, 0, len(text) - 1):
            print(f"Word #{seq + 1}: Set")
        else:
            print(f"Word #{seq + 1}: No Set")
