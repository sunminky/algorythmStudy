# https://www.acmicpc.net/problem/1806
import sys

if __name__ == '__main__':
    n_element, target = map(int, sys.stdin.readline().split())
    element = tuple(map(int, sys.stdin.readline().split()))
    answer = 100001
    start = end = 0
    acc = element[0]

    while end < n_element:
        if acc >= target:
            answer = min(answer, end - start + 1)
            acc -= element[start]
            start += 1
        else:
            end += 1
            acc += element[end % n_element]

        end = max(start, end)

    print(0 if answer == 100001 else answer)
