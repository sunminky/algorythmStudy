# https://programmers.co.kr/learn/courses/30/lessons/67257
import re
from itertools import permutations
from collections import deque


def run(nums, expressions, prior):
    queue = deque([nums[0]])

    for i in range(len(expressions)):
        queue.append(expressions[i])
        queue.append(nums[1 + i])

    for _prior in prior:
        new_queue = deque([queue.popleft()])

        while queue:
            _exp = queue.popleft()
            _num = queue.popleft()

            if _exp == _prior:
                new_queue.append(eval(f"{new_queue.pop()}{_exp}{_num}"))
            else:
                new_queue.append(_exp)
                new_queue.append(_num)

        queue = new_queue

    return abs(int(queue.popleft()))


def solution(expression):
    answer = 0
    prior = tuple(permutations(['-', '*', '+'], 3))
    nums = re.split(r"[-+*]+", expression)
    expressions = re.split(r"[0-9]+", expression)[1:-1]

    for _prior in prior:
        answer = max(answer, run(nums, expressions, _prior))

    return answer


if __name__ == '__main__':
    solution("100-200*300-500+20")  # 60420
    solution("50*6-3*2")  # 300
    solution("50*2")  # 100
