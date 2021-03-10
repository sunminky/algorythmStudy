# https://www.acmicpc.net/problem/1806

import sys

if __name__ == '__main__':
    n_number, target = map(int, sys.stdin.readline().split())
    numbers = tuple(map(int, sys.stdin.readline().split()))
    answer = 100001 #최악의 경우
    pointer1 = pointer2 = 0

    while True:
        if sum(numbers[pointer1:pointer2+1]) >= target:
            answer = min(answer, pointer2 - pointer1 + 1)
            pointer1 += 1
            if pointer1 == n_number:
                break
            pointer2 = max(pointer1, pointer2)
        else:
            pointer2 += 1
            if pointer2 == n_number:
                break

    if answer == 100001:
        print(0)
    else:
        print(answer)
