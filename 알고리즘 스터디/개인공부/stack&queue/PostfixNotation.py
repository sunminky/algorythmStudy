# https://www.acmicpc.net/problem/1918

import sys
from collections import deque

if __name__ == '__main__':
    expression = list(sys.stdin.readline().rstrip())
    operator = {'+': 1, '-': 1, '*': 0, '/': 0, '(': 99}  # +, -, *, /, (, )
    stack = deque(maxlen=len(expression))
    answer = []

    # 연산자 우선순위가 높거나 같으면 계속 push
    for char in expression:
        # ')'가 입력된 경우
        if char == ')':
            # '(' 만날 때 까지 스택에서 연산자 빼줌
            while stack:
                op = stack.pop()

                if op == '(':
                    break

                answer.append(op)

        # 알파벳임
        elif operator.get(char, False) is False:
            answer.append(char)
        # 기호임
        else:
            # '('가 입력된 경우
            if char == '(':
                stack.append(char)
            # 스택의 맨 위에있는 연산자보다 우선순위가 높음
            elif not stack or operator[stack[-1]] > operator[char]:
                stack.append(char)
            else:
                # 연산자 빼주기
                while stack:
                    # 자기보다 우선순위가 낮은 연산자가 나올 때 까지 pop
                    if operator[stack[-1]] > operator[char]:
                        stack.append(char)
                        break
                    answer.append(stack.pop())
                else:
                    stack.append(char)

    answer.extend(reversed(stack))
    print("".join(answer))
