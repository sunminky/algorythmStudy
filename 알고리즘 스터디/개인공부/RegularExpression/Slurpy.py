# https://www.acmicpc.net/problem/14906
import sys
import re


def is_slump(text) -> bool:
    if re.fullmatch("[D|E]F+G", text):
        return True

    match_result = re.match("[D|E]F+", text)

    if match_result:
        if is_slump(text[match_result.end():]):  # 최적화 필요
            return True

    return False


def is_slimp(text) -> bool:
    if re.fullmatch("AH", text):
        return True

    if re.fullmatch("AB.*C", text):
        if len(text) >= 3 and is_slimp(text[2:-1]):
            return True

    if re.fullmatch("A.*C", text):
        if len(text) >= 2 and is_slump(text[1:-1]):
            return True

    return False


if __name__ == '__main__':
    print("SLURPYS OUTPUT")

    for _ in range(int(sys.stdin.readline())):
        text = sys.stdin.readline().rstrip()
        result = False

        for i in range(2, len(text)):
            txt1 = text[:i]
            txt2 = text[i:]
            result = result or (is_slimp(txt1) and is_slump(txt2))

        print("YES" if result else "NO")

    print("END OF OUTPUT")
