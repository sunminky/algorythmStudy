# https://www.acmicpc.net/problem/17136
import sys
sys.setrecursionlimit(1000000000)

field = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
remain = [5] * 5
answer = 100


def validate(x, y, limit):
    if y + limit >= 10:
        return False
    if x + limit >= 10:
        return False

    for row in range(y, y + limit + 1):
        for col in range(x, x + limit + 1):
            if field[row][col] == 0:
                return False
    return True


def deploy(y, x, used):
    global answer

    if y >= 10:
        answer = min(answer, used)
        return

    if field[y][x] == 1:
        for limit in range(5):
            if remain[limit] == 0:
                continue

            if validate(x, y, limit):
                remain[limit] -= 1
                for row in range(y, y + limit + 1):
                    for col in range(x, x + limit + 1):
                        field[row][col] = 0

                if x + limit + 1 >= 10:
                    deploy(y + 1, 0, used + 1)
                else:
                    deploy(y, x + limit + 1, used + 1)

                remain[limit] += 1
                for row in range(y, y + limit + 1):
                    for col in range(x, x + limit + 1):
                        field[row][col] = 1
            else:
                break
    else:
        for col in range(x + 1, 10):
            if field[y][col] == 1:
                deploy(y, col, used)
                break
        else:
            deploy(y + 1, 0, used)


if __name__ == '__main__':
    deploy(0, 0, 0)
    print(-1 if answer == 100 else answer)
