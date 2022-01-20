# https://www.acmicpc.net/problem/3425
import sys


def excute(program: list, argument: int):
    stack = [argument]

    for operator in program:
        if operator[0] == "NUM":
            stack.append(int(operator[1]))

        elif operator[0] == "POP":
            if not stack:
                return "ERROR"
            stack.pop()

        elif operator[0] == "INV":
            if not stack:
                return "ERROR"
            stack[-1] *= -1

        elif operator[0] == "DUP":
            if not stack:
                return "ERROR"
            stack.append(stack[-1])

        elif operator[0] == "SWP":
            if len(stack) < 2:
                return "ERROR"

            x = stack.pop()
            y = stack.pop()

            stack.append(x)
            stack.append(y)

        elif operator[0] == "ADD":
            if len(stack) < 2:
                return "ERROR"

            x = stack.pop()
            y = stack.pop()

            stack.append(x + y)

        elif operator[0] == "SUB":
            if len(stack) < 2:
                return "ERROR"

            x = stack.pop()
            y = stack.pop()

            stack.append(y - x)

        elif operator[0] == "MUL":
            if len(stack) < 2:
                return "ERROR"

            x = stack.pop()
            y = stack.pop()

            stack.append(x * y)

        elif operator[0] == "DIV":
            if len(stack) < 2:
                return "ERROR"

            x = stack.pop()
            y = stack.pop()

            if x == 0:
                return "ERROR"

            if (x > 0 and y < 0) or (x < 0 and y > 0):
                stack.append((abs(y) // abs(x)) * -1)
            else:
                stack.append(abs(y) // abs(x))

        elif operator[0] == "MOD":
            if len(stack) < 2:
                return "ERROR"

            x = stack.pop()
            y = stack.pop()

            if x == 0:
                return "ERROR"

            if y < 0:
                stack.append((abs(y) % abs(x)) * -1)
            else:
                stack.append(abs(y) % abs(x))

        else:
            return "ERROR"

        if stack and abs(stack[-1]) > 1000000000:
            return "ERROR"

    if len(stack) != 1:
        return "ERROR"

    return stack[0]


if __name__ == '__main__':
    while True:
        program = []
        while True:
            data = sys.stdin.readline().split()
            if data[0] == "QUIT":
                exit(0)
            if data[0] == "END":
                break
            program.append(data)

        for _ in range(int(sys.stdin.readline())):
            argument = int(sys.stdin.readline())

            # 프로그램 실행
            print(excute(program, argument))

        print()
        sys.stdin.readline()
