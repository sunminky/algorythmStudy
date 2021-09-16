# https://www.acmicpc.net/problem/1194
import sys
from collections import deque


def staring_point(field):
    for row in range(len(field)):
        for col in range(len(field[row])):
            if field[row][col] == '0':
                return col, row


if __name__ == '__main__':
    height, width = map(int, sys.stdin.readline().split())
    field = [sys.stdin.readline().rstrip() for _ in range(height)]
    cost = [[[125001] * 64 for _ in range(width)] for _ in range(height)]
    starting = staring_point(field)
    queue = deque([(starting[0], starting[1], 0, 0)])  # 시작좌표 x, 시작좌표 y, 방문비트, 비용
    movement = ((0, 1), (1, 0), (0, -1), (-1, 0))
    key_dict = {'a': 1, 'b': 2, 'c': 4, 'd': 8, 'e': 16, 'f': 32,
                'A': 1, 'B': 2, 'C': 4, 'D': 8, 'E': 16, 'F': 32}
    locks = {'A', 'B', 'C', 'D', 'E', 'F'}
    keys = {'a', 'b', 'c', 'd', 'e', 'f'}
    answer = -1

    while queue:
        cur_x, cur_y, visited, distance = queue.popleft()

        if field[cur_y][cur_x] == '1':
            answer = distance
            break

        for move in movement:
            new_x = cur_x + move[0]
            new_y = cur_y + move[1]

            # 바운더리 체크
            if new_x < 0 or new_x >= width or new_y < 0 or new_y >= height:
                continue

            # 벽인 경우
            elif field[new_y][new_x] == '#':
                continue

            # 자물쇠인 경우
            elif field[new_y][new_x] in locks:
                # 열쇠가 없는 경우
                if not visited & key_dict[field[new_y][new_x]]:
                    continue
                # 최소값이 갱신되는 경우
                if cost[new_y][new_x][visited] > distance + 1:
                    cost[new_y][new_x][visited] = distance + 1
                    queue.append((new_x, new_y, visited, distance + 1))

            # 키인 경우
            elif field[new_y][new_x] in keys:
                # 최소값이 갱신되는 경우
                if cost[new_y][new_x][visited | key_dict[field[new_y][new_x]]] > distance + 1:
                    cost[new_y][new_x][visited | key_dict[field[new_y][new_x]]] = distance + 1
                    queue.append((new_x, new_y, visited | key_dict[field[new_y][new_x]], distance + 1))

            # 그냥 벽인 경우
            else:
                # 최소값이 갱신되는 경우
                if cost[new_y][new_x][visited] > distance + 1:
                    cost[new_y][new_x][visited] = distance + 1
                    queue.append((new_x, new_y, visited, distance + 1))

    print(answer)
