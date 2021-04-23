# https://www.acmicpc.net/problem/2230

import sys

if __name__ == '__main__':
    n_numbers, target = map(int, sys.stdin.readline().split())
    numbers = sorted((int(sys.stdin.readline()) for _ in range(n_numbers)))
    front_pointer = 0
    rear_pointer = 1
    answer = 2000000001

    while rear_pointer < n_numbers:
        # target 보다 차이가 큰 경우
        if numbers[rear_pointer] - numbers[front_pointer] >= target:
            answer = min(answer, numbers[rear_pointer] - numbers[front_pointer])
            front_pointer += 1

            # 둘이 만난 경우
            if front_pointer == rear_pointer:
                rear_pointer += 1

        # target 보다 차이가 작은 경우
        else:
            rear_pointer += 1

    print(answer)
