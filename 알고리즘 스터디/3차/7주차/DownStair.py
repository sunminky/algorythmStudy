# https://www.acmicpc.net/problem/1520

import sys
from collections import deque

if __name__ == '__main__':
    height, width = tuple(map(int, sys.stdin.readline().rstrip().split()))  # 지도 높이, 지도 너비
    my_map = []
    count_map = [[0 for _ in range(width)] for _ in range(height)]
    movement = ((1, 0), (-1, 0), (0, 1), (0, -1))
    queue = deque()

    for _ in range(height):
        my_map.append(list(map(int, sys.stdin.readline().rstrip().split())))

    #큐에 출발지 넣음
    queue.append((0, 0))
    count_map[0][0] = 1

    while queue:
        cur_loc = queue.popleft()

        for _move in movement:
            x = cur_loc[0] + _move[0]
            y = cur_loc[1] + _move[1]

            #바운더리 체크
            if 0 <= x < width and 0 <= y < height:
                #내리막인지 체크
                if my_map[y][x] < my_map[cur_loc[1]][cur_loc[0]]:
                    count_map[y][x] += 1
                    queue.append((x, y))

    print(count_map[-1][-1])