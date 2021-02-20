#https://www.acmicpc.net/problem/13397

import sys

if __name__ == '__main__':
    n_numbers, n_groups = tuple(map(int, sys.stdin.readline().split()))
    numbers = tuple(map(int, sys.stdin.readline().split()))

    low = 0
    high = 10000
    answer = 0

    while low < high:
        center = (low + high) // 2

        #구간 값 계산
        min_val = max_val = numbers[0]
        cnt = 1
        success = True

        for num in numbers:
            min_val = min(min_val, num)
            max_val = max(max_val, num)

            if max_val - min_val > center:
                cnt += 1
                min_val = max_val = num
                if cnt > n_groups:
                    success = False
                    break

        if success:
            high = center
            answer = center
        else:
            low = center+1

    print(answer)