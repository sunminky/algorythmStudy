# https://www.acmicpc.net/problem/16236
import sys
from collections import deque

width = int(sys.stdin.readline())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(width)]
cur_size = 2
capacity = 0
answer = 0
shark_x = shark_y = 0


def find_shark():
    global shark_x, shark_y
    for row in range(width):
        for col in range(width):
            if field[row][col] == 9:
                shark_x = col
                shark_y = row
                field[row][col] = 0
                return


def travel():
    global answer
    global cur_size
    global capacity
    global shark_x
    global shark_y

    visited = [[False] * width for _ in range(width)]
    queue = deque([(shark_x, shark_y, 0)])  # 상어x, 상어y, 움직인 거리
    cur_least_move = 401
    candidate = [20, 20]  # x, y 좌표
    movement = ((0, 1), (0, -1), (1, 0), (-1, 0))

    visited[shark_y][shark_x] = True

    while queue:
        cur_x, cur_y, cur_move = queue.popleft()

        # 너무 많이 움직임
        if cur_least_move < cur_move + 1:
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
            # 나보다 큰 물고기
            if field[new_y][new_x] > cur_size:
                continue
            # 먹을 수 있음
            if 0 < field[new_y][new_x] < cur_size:
                cur_least_move = min(cur_least_move, cur_move + 1)

                if new_y <= candidate[1]:
                    candidate[0] = new_x
                    candidate[1] = min(new_y, candidate[1])

            visited[new_y][new_x] = True
            queue.append((new_x, new_y, cur_move + 1))

    if candidate[0] == 20 and candidate[1] == 20:
        return False

    answer += cur_least_move
    capacity += 1
    field[candidate[1]][candidate[0]] = 0
    cur_size, capacity = cur_size + capacity // cur_size, capacity % cur_size
    shark_x = candidate[0]
    shark_y = candidate[1]

    return True


if __name__ == '__main__':
    find_shark()

    while True:
        # 움직이기
        if not travel():
            break

    print(answer)
