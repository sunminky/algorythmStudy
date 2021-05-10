# https://www.acmicpc.net/problem/1300
# https://kyu9341.github.io/algorithm/2020/03/13/algorithm1300/


import sys


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    k = int(sys.stdin.readline())
    start = 1
    end = n ** 2

    # end - 1 내에 존재
    while start < end:
        middle = (start + end) // 2

        # i행에서 middle 보다 작거나 같은 수의 개수 : min(middle을 i로 나눈 값, n)
        less_cnt = sum([min(middle // i, n) for i in range(1, n + 1)])

        if less_cnt < k:
            start = middle + 1
        else:
            end = middle

    print(start)
