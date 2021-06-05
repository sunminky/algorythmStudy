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
            width = seq - stack[-1] - 1 if stack else seq
            max_area = max(max_area, height * width)

        stack.append(seq)

    # 스택에 요소가 남은 경우
    while stack:
        height = bar[stack.pop()]
        width = len(bar) - stack[-1] - 1 if stack else len(bar)
        max_area = max(max_area, height * width)

    return max_area


if __name__ == '__main__':
    while True:
        height, width = map(int, sys.stdin.readline().split())
        stack = [0] * width
        answer = 0  # 최대 직사각형 넓이

        # height 와 width가 모두 0인 경우
        if not (height | width):
            break
        
        for _ in range(height):
            field = tuple(map(int, sys.stdin.readline().split()))
            
            # 스택에 넣기
            for i in range(width):
                stack[i] = stack[i] * field[i] + field[i]

            # 스택에서 가장 큰 직사각형 구하기
            answer = max(answer, area(stack))

        print(answer)
