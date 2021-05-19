# https://programmers.co.kr/learn/courses/30/lessons/42883
from collections import deque


def solution(number, k):
    queue = deque()

    for num in number:
        # 현재 숫자가 크다면 앞자리를 차지하도록 해야함
        while queue and queue[-1] < num and k != 0:
            queue.pop()
            k -= 1

        queue.append(num)

    # 숫자를 k번 못뺀 경우 빼주기
    while queue and k != 0:
        queue.pop()
        k -= 1

    return "".join(queue)


if __name__ == '__main__':
    result = solution("1924", 2)
    print(result)

    result = solution("1231234", 3)
    print(result)

    result = solution("4177252841", 4)
    print(result)

    result = solution("989", 2)
    print(result)
