#https://www.acmicpc.net/problem/2573

import sys
from queue import PriorityQueue

if __name__ == '__main__':
    height, width = tuple(map(int, sys.stdin.readline().split()))
    field = [list(map(int, sys.stdin.readline().split())) for _ in range(height)]
    queue = PriorityQueue()

    for row in range(height):
        for col in range(width):
            if field[row][col]:
                queue.put((col, row))

    while not queue.empty():
        print(queue.get())