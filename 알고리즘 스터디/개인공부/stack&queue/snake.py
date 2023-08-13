# https://www.acmicpc.net/problem/3190
import sys
from collections import deque

if __name__ == '__main__':
    width = int(sys.stdin.readline())
    field = [[0] * width for _ in range(width)]
    direction = ((0, 1), (1, 0), (0, -1), (-1, 0))  # (y, x)
    direction_idx = 0
    alpha_direction = {'L': -1, 'D': 1}
    snake = deque([(0, 0)])  # (y, x)
    live = 1
    field[0][0] = 2

    for _ in range(int(sys.stdin.readline())):
        _y, _x = map(int, sys.stdin.readline().split())
        field[_y - 1][_x - 1] = 1

    movement = deque([tuple(map(lambda x: int(x) if x.isdigit() else x, sys.stdin.readline().split())) for _ in
                      range(int(sys.stdin.readline()))])

    while True:
        head = (snake[-1][0] + direction[direction_idx][0], snake[-1][1] + direction[direction_idx][1])
        snake.append(head)

        # 바운더리 체크
        if not 0 <= head[0] < width or not 0 <= head[1] < width:
            break

        # 자기몸통 체크
        if field[head[0]][head[1]] == 2:
            break

        # 꼬리 줄이기
        if field[head[0]][head[1]] == 1:
            pass
        else:
            field[snake[0][0]][snake[0][1]] = 0
            snake.popleft()

        field[head[0]][head[1]] = 2

        # 방향전환
        if movement and live == movement[0][0]:
            _, _direction = movement.popleft()
            direction_idx = (direction_idx + alpha_direction[_direction] + 4) % 4

        live += 1

    print(live)
