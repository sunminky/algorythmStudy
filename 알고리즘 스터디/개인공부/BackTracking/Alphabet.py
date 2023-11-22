# https://www.acmicpc.net/problem/1987
import sys

height, width = map(int, sys.stdin.readline().split())
field = [sys.stdin.readline().rstrip() for _ in range(height)]
movement = ((0, 1), (1, 0), (0, -1), (-1, 0))


def travel(stage: int, bitmask: int, x_pos: int, y_pos: int) -> int:
    answer = stage

    for _movement in movement:
        new_x = x_pos + _movement[0]
        new_y = y_pos + _movement[1]

        # 바운더리 체크
        if not 0 <= new_x < width:
            continue

        if not 0 <= new_y < height:
            continue

        # 방문확인
        if bitmask & (1 << (ord(field[new_y][new_x]) - 65)):
            continue

        answer = max(travel(stage + 1, bitmask | (1 << (ord(field[new_y][new_x]) - 65)), new_x, new_y), answer)

    return answer


if __name__ == '__main__':
    print(travel(1, 1 << (ord(field[0][0]) - 65), 0, 0))
