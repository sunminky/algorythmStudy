# https://www.acmicpc.net/problem/9935

import sys

if __name__ == '__main__':
    text = sys.stdin.readline().rstrip()
    bomb = list(sys.stdin.readline().rstrip())
    stack = []

    for ch in text:
        stack.append(ch)

        if len(stack) >= len(bomb):
            if stack[-len(bomb):] == bomb:
                for _ in range(len(bomb)):
                    stack.pop()

    if stack:
        print("".join(stack))
    else:
        print("FRULA")