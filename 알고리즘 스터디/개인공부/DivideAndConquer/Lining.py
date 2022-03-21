# https://programmers.co.kr/learn/courses/30/lessons/12936?language=python3
from math import factorial


def make_array(arr, n):
    visited = [False] * n
    result = []

    for e in arr:
        for i in range(n):
            if visited[i]:
                continue

            if not e:
                visited[i] = True
                result.append(i + 1)

            e -= 1

    return result


def solution(n, k):
    answer = []
    waiting = list(range(1, n + 1))

    k -= 1
    remain_case = factorial(n - 1)

    for i in range(1, n):
        # answer.append(k // remain_case)  # k // (n - i)!
        answer.append(waiting.pop(int(k // remain_case)))
        k %= remain_case
        remain_case //= n - i

    # answer.append(0)
    answer.append(waiting.pop(0))

    #return make_array(answer, n)
    return answer


if __name__ == '__main__':
    result = solution(3, 5)  # [3,1,2]
    print(result)

    result = solution(3, 6)  # [3,2,1]
    print(result)

    result = solution(3, 3)  # [2,1,3]
    print(result)

    result = solution(4, 11)  # [2,4,1,3]
    print(result)

    result = solution(4, 15)  # [3,2,1,4]
    print(result)
