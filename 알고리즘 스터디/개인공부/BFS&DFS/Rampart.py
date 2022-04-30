# https://www.acmicpc.net/problem/2234
import sys
from collections import deque

width, height = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(height)]
visited = [[False] * width for _ in range(height)]
area = [[0] * width for _ in range(height)]
area_flag = 0
area_per_castle = []


def travel(x, y):
    queue = deque([(x, y)])
    movement = ((1, 0, 1), (-1, 0, 4), (0, 1, 2), (0, -1, 8))  # 동 서 남 북
    visited[y][x] = True
    cnt = 0
    '''west = 1  # 서
    north = 2  # 북
    east = 4  # 동
    south = 8  # 남'''

    while queue:
        cur_x, cur_y = queue.popleft()
        area[cur_y][cur_x] = area_flag
        cnt += 1

        for _move in movement:
            new_x = cur_x + _move[0]
            new_y = cur_y + _move[1]

            # 바운더리 체크
            if not 0 <= new_x < width:
                continue
            if not 0 <= new_y < height:
                continue

            # 벽 체크
            if field[new_y][new_x] & _move[2]:
                continue
                
            # 방문여부 체크
            if visited[new_y][new_x]:
                continue

            visited[new_y][new_x] = True
            queue.append((new_x, new_y))

    return cnt


if __name__ == '__main__':
    n_castle = 0
    max_area = 0

    # 성의 개수 카운트
    for row in range(height):
        for col in range(width):
            if visited[row][col] is False:
                _area = travel(col, row)
                max_area = max(max_area, _area)
                area_per_castle.append(_area)
                area_flag += 1
                n_castle += 1

    neighbor = [set() for _ in range(n_castle)]

    max_merge_area = 0
    
    # 이웃 찾기
    movement = ((1, 0, 1), (-1, 0, 4), (0, 1, 2), (0, -1, 8))  # 동 서 남 북
    for row in range(height):
        for col in range(width):
            for _movement in movement:
                new_x = col + _movement[0]
                new_y = row + _movement[1]

                # 바운더리 체크
                if not 0 <= new_x < width:
                    continue
                if not 0 <= new_y < height:
                    continue

                if area[row][col] >= area[new_y][new_x]:
                    continue

                neighbor[area[row][col]].add(area[new_y][new_x])

    # 이웃과 합치기
    for i in range(n_castle):
        for neigh in neighbor[i]:
            max_merge_area = max(max_merge_area, area_per_castle[i] + area_per_castle[neigh])

    print(n_castle)
    print(max_area)
    print(max_merge_area)
