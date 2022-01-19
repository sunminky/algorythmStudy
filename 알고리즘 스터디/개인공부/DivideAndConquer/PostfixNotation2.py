# https://www.acmicpc.net/problem/1935
import sys

n_alpha = int(sys.stdin.readline())
experssion = [e for e in sys.stdin.readline().rstrip()]
cost = [int(sys.stdin.readline()) for _ in range(n_alpha)]
operator_dict = {'*': lambda x, y: x * y, '/': lambda x, y: x / y, '+': lambda x, y: x + y, '-': lambda x, y: x - y}


def divide(expression: list):
    # 더이상 식이 존재하지 않으면 종료
    if not expression:
        return 0

    alpha = expression.pop()

    if alpha in operator_dict.keys():
        y = divide(expression)
        x = divide(expression)

        return operator_dict[alpha](x, y)
    else:
        return cost[ord(alpha) - 65]


if __name__ == '__main__':
    print(f"{divide(experssion):.2f}")
