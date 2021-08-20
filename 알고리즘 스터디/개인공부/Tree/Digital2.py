# https://www.acmicpc.net/problem/8112
import sys
from collections import deque

if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        base = int(sys.stdin.readline())
        memo = dict()
        queue = deque()
        answer = []

        queue.append(1)
        memo[1] = (-1, -1)  # 이전 나머지, 더해진 값

        while queue:
            remain = queue.popleft()

            if remain % base == 0:
                break

            if (remain * 10 + 0) % base not in memo:
                memo[(remain * 10 + 0) % base] = (remain, '0')
                queue.append((remain * 10 + 0) % base)

            if (remain * 10 + 1) % base not in memo:
                memo[(remain * 10 + 1) % base] = (remain, '1')
                queue.append((remain * 10 + 1) % base)

        # 출력
        if 0 in memo:
            print_remain = 0

            while print_remain != 1:
                answer.append(memo[print_remain][1])
                print_remain = memo[print_remain][0]

        answer.append('1')

        print("".join(reversed(answer)))
