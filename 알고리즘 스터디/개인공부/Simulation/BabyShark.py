# https://www.acmicpc.net/problem/16236
import sys
from collections import deque
import heapq

movement = ((0, 1), (0, -1), (1, 0), (-1, 0))
width = int(sys.stdin.readline())
field = [[*map(int, sys.stdin.readline().split())] for _ in range(width)]
shark_size = 2  # 상어크기
eat_cnt = 0  # 먹은 물고기 개수


def find_shark(field: list, width: int) -> tuple:
    for row in range(width):
        for col in range(width):
            if field[row][col] == 9:
                return row, col

    return None


def hunt(shark_position) -> list:
    queue = deque([(0, *shark_position)])  # 이동거리, y좌표, x좌표
    fish = []
    fish_distance = 401
    visited = [[False] * width for _ in range(width)]

    visited[shark_position[0]][shark_position[1]] = True

    while queue:
        cur_distance, cur_y, cur_x = queue.popleft()

        if cur_distance >= fish_distance:
            continue

        for _move in movement:
            new_x = cur_x + _move[0]
            new_y = cur_y + _move[1]

            # 바운더리 체크
            if not 0 <= new_x < width:
                continue
            if not 0 <= new_y < width:
                continue

            # 방문여부 체크
            if visited[new_y][new_x]:
                continue

            # 물고기 체급 체크
            if 0 <= field[new_y][new_x] <= shark_size:
                # 물고기가 있음
                if field[new_y][new_x] != 0:
                    if field[new_y][new_x] < shark_size:
                        heapq.heappush(fish, (cur_distance + 1, new_y, new_x))
                        fish_distance = min(fish_distance, cur_distance + 1)

                queue.append((cur_distance + 1, new_y, new_x))
                visited[new_y][new_x] = True

    return fish


if __name__ == '__main__':
    shark_position = find_shark(field, width)
    answer = 0
    field[shark_position[0]][shark_position[1]] = 0

    while True:
        fish = hunt(shark_position)

        if len(fish) == 0:
            break

        answer += fish[0][0]
        field[fish[0][1]][fish[0][2]] = 0
        shark_position = fish[0][1], fish[0][2]
        eat_cnt += 1

        if eat_cnt == shark_size:
            eat_cnt = 0
            shark_size += 1

    print(answer)
