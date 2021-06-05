# https://www.acmicpc.net/problem/11873
import sys
from collections import deque


def area(bar):
    stack = deque(maxlen=len(bar))
    max_area = 0
    
    # enumerate보다 range가 더 빠르다
    for seq in range(len(bar)):
        # 스택의 가장 마지막 요소가 현재 요소보다 클 때
        while stack and bar[stack[-1]] > bar[seq]:
            height = bar[stack.pop()]
            width = seq

            if stack:
                width -= stack[-1] + 1

            max_area = max(max_area, height * width)

        stack.append(seq)

    # 스택에 요소가 남은 경우
    while stack:
        height = bar[stack.pop()]
        width = len(bar)

        if stack:
            width -= stack[-1] + 1

        max_area = max(max_area, height * width)

    return max_area


if __name__ == '__main__':
    while True:
        height, width = map(int, sys.stdin.readline().split())
        stack = [0] * height
        answer = 0  # 최대 직사각형 넓이

        if (height | width) == 0:
            break

        field = [tuple(map(int, sys.stdin.readline().split())) for _ in range(height)]

        for col in range(width):
            # 스택에 넣기
            for row in range(height):
                stack[row] = stack[row] * field[row][col] + field[row][col]
                
            # 스택에서 가장 큰 직사각형 구하기
            answer = max(answer, area(stack))

        print(answer)
