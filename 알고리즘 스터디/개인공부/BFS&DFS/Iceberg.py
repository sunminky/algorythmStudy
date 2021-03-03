#https://www.acmicpc.net/problem/2573

import sys
from _collections import deque
sys.setrecursionlimit(10000)

def melt(field, x, y):
    cnt = 0

    if x-1 >= 0 and field[y][x - 1] == 0:
        cnt += 1
    if x+1 < len(field[y]) and field[y][x+1] == 0:
        cnt += 1
    if y-1 >= 0 and field[y - 1][x] == 0:
        cnt += 1
    if y+1 < len(field) and field[y+1][x] == 0:
        cnt += 1

    return cnt


def checkIce(field, x, y):
    global visited
    visited[y][x] = True
    cnt = 1

    if field[y][x] == 0:
        return 0
    if 0 <= x-1 and visited[y][x-1] is False:
        cnt += checkIce(field, x-1, y)
    if x+1 < len(field[y]) and visited[y][x+1] is False:
        cnt += checkIce(field, x+1, y)
    if 0 <= y-1 and visited[y-1][x] is False:
        cnt += checkIce(field, x, y-1)
    if y+1 < len(field) and visited[y+1][x] is False:
        cnt += checkIce(field, x, y+1)

    return cnt


if __name__ == '__main__':
    height, width = tuple(map(int, sys.stdin.readline().split()))
    field = [list(map(int, sys.stdin.readline().split())) for _ in range(height)]
    queue = deque()
    answer = 0
    removed = True

    for row in range(height):
        for col in range(width):
            if field[row][col]:
                queue.append((col, row))

    while queue:
        dqueue = deque()
        commit_queue = deque()
        
        #빙산 개수 체크
        if removed:
            global visited
            visited = [[False for _ in range(width)] for _ in range(height)]
            if checkIce(field, queue[0][0], queue[0][1]) != len(queue):
                print(answer)
                exit(0)
            removed = False

        while queue:
            ice_x, ice_y = queue.popleft()
            commit_queue.append((ice_x, ice_y, melt(field, ice_x, ice_y)))

        while commit_queue:
            ice_x, ice_y, melt_cnt = commit_queue.popleft()

            if melt_cnt < field[ice_y][ice_x]:
                dqueue.append((ice_x, ice_y))
            else:
                removed = True
            field[ice_y][ice_x] = max(0, field[ice_y][ice_x] - melt_cnt)

        queue = dqueue
        answer += 1

    print(0)    #완전히 녹을 때 까지 빙하가 한 덩어리인 경우