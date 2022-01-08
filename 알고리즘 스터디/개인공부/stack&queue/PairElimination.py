# https://programmers.co.kr/learn/courses/30/lessons/12973
def solution(s):
    stack = []

    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    return 0 if stack else 1


if __name__ == '__main__':
    solution('baabaa')  # 1
    solution('cdcd')  # 0
