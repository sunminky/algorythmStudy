# https://www.acmicpc.net/problem/2512
import sys

if __name__ == '__main__':
    sys.stdin.readline()    # 지방의 수, 필요없음
    requirements = tuple(map(int, sys.stdin.readline().split()))
    budget = int(sys.stdin.readline())

    start = 0
    end = max(requirements) + 1
    answer = 0

    while start < end:
        middle = (start + end) // 2
        consumption = 0

        for e in requirements:
            consumption += min(e, middle)

        if consumption > budget:
            end = middle
        else:
            start = middle + 1
            answer = max(answer, middle)

    print(answer)
