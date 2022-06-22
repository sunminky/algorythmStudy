# https://www.acmicpc.net/problem/1941
import sys
from itertools import combinations
from collections import deque

field = [sys.stdin.readline().rstrip() for _ in range(5)]
seperate_field = [[False] * 5 for _ in range(5)]


def prevail(union):
    s_cnt = [field[e // 5][e % 5] for e in union].count('S')

    return s_cnt > 3


def is_seperate(union):
    cnt = 1
    queue = deque()
    movement = ((1, 0), (-1, 0), (0, 1), (0, -1))

    for e in union:
        seperate_field[e // 5][e % 5] = True

    queue.append((union[0] % 5, union[0] // 5))
    seperate_field[union[0] // 5][union[0] % 5] = False

    while queue:
        cur_x, cur_y = queue.popleft()

        for _move in movement:
            new_x = _move[0] + cur_x
            new_y = _move[1] + cur_y

            # 바운더리
            if not 0 <= new_x < 5:
                continue

            if not 0 <= new_y < 5:
                continue

            if seperate_field[new_y][new_x]:
                cnt += 1
                seperate_field[new_y][new_x] = False
                queue.append((new_x, new_y))

    for e in union:
        seperate_field[e // 5][e % 5] = False

    return cnt == 7


if __name__ == '__main__':
    answer = 0

    for e in combinations(range(25), 7):
        if prevail(e) and is_seperate(e):
            answer += 1

    print(answer)
