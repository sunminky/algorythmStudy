#https://www.acmicpc.net/problem/11003
#https://www.youtube.com/watch?v=Tqw4WcmSFfk

import sys
from collections import deque

if __name__ == '__main__':
    n_numbers, width = tuple(map(int, sys.stdin.readline().split()))
    numbers = tuple(map(int, sys.stdin.readline().split()))
    min_queue = deque() #최소값을 저장하는 큐
    number_queue = deque()  #width보다 적은 수의 길이를 가지는 큐

    for seq, n in enumerate(numbers):
        number_queue.append(n)

        #최소큐에 추가
        for i in range(len(min_queue)):
            #최소큐에서 현재 요소보다 큰 원소를 제거
            if min_queue[-1] > n:
                min_queue.pop()
            else:
                break

        min_queue.append(n)

        #큐가 최대 길이를 넘으면 제일 먼저 들어온 원소 제거
        if len(number_queue) == width + 1:
            #제거된 원소가 최소값인 경우 최소값 큐에서 제거
            if number_queue.popleft() == min_queue[0]:
                min_queue.popleft()

        sys.stdout.write(min_queue[0], end=" ")
