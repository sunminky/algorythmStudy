# https://www.acmicpc.net/problem/14503
import sys
from collections import deque

if __name__ == '__main__':
    height, width = map(int, sys.stdin.readline().split())
    y_pos, x_pos, direction = map(int, sys.stdin.readline().split())
    field = tuple(tuple(map(int, sys.stdin.readline().split())) for _ in range(height))
    visited = [[False] * width for _ in range(height)]
    movement = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 서 남 동 북
    queue = deque([(x_pos, y_pos, -1 - direction)])
    answer = 0

    while queue:
        cur_x, cur_y, cur_dir = queue.popleft()

        answer += not visited[cur_y][cur_x]
        visited[cur_y][cur_x] = True

        # 청소 된 칸 탐색
        for seq in range(1, 5):
            new_dir = (cur_dir + seq) % 4
            new_x = cur_x + movement[new_dir][0]
            new_y = cur_y + movement[new_dir][1]

            # 벽체크
            if field[new_y][new_x] == 1:
                continue

            # 청소 안된 구역 체크
            if visited[new_y][new_x] is False:
                queue.append((new_x, new_y, new_dir))
                break

        # 청소 안된 구역이 없는 경우
        else:
            new_dir = (cur_dir + 2) % 4
            new_x = cur_x + movement[new_dir][0]
            new_y = cur_y + movement[new_dir][1]

            # 벽체크
            if field[new_y][new_x] == 1:
                continue

            queue.append((new_x, new_y, cur_dir))

    print(answer)
