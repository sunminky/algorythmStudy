# https://www.acmicpc.net/problem/10775
import sys

sys.setrecursionlimit(1000000)


def find(vacancy, current) -> int:
    if vacancy[current] == 0 or vacancy[current] == current:
        result = vacancy[current]

        # 바로 앞에 있는 게이트웨이가 가리키는 빈 게이트웨이를 가리키게 함
        vacancy[current] = vacancy[max(current - 1, 0)]

        return result
    else:
        result = find(vacancy, vacancy[vacancy[current]])
        vacancy[current] = result

        return result


if __name__ == '__main__':
    n_gate = int(sys.stdin.readline())
    n_airplane = int(sys.stdin.readline())
    vacancy = [i for i in range(n_gate + 1)]
    answer = 0

    for _ in range(n_airplane):
        arrival = int(sys.stdin.readline())
        gate = find(vacancy, arrival)

        if gate == 0:
            break

        answer += 1

    print(answer)
