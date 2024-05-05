# https://www.acmicpc.net/problem/16234
import sys
from collections import deque
from itertools import product

answer = -1
width, low_bound, up_bound = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(width)]
visited = [[False] * width for _ in range(width)]
queue = deque(list(product([0], range(width), range(width))))  # 단계, x좌표, y좌표
movement = ((0, 1), (1, 0), (0, -1), (-1, 0))


def grouping(x, y):
    if not visited[y][x]:
        union_queue = deque([(x, y)])
        migration_queue = deque([(x, y)])
        population_sum = field[y][x]
        union_cnt = 1

        visited[y][x] = True

        while union_queue:
            cur_x, cur_y = union_queue.popleft()

            for _move in movement:
                new_x = _move[0] + cur_x
                new_y = _move[1] + cur_y

                # 바운더리 체크
                if not 0 <= new_x < width:
                    continue

                if not 0 <= new_y < width:
                    continue

                # 방문여부 체크
                if visited[new_y][new_x]:
                    continue

                # 이민조건 체크
                if not low_bound <= abs(field[new_y][new_x] - field[cur_y][cur_x]) <= up_bound:
                    continue

                union_queue.append((new_x, new_y))
                queue.append((answer + 1, new_x, new_y))
                migration_queue.append((new_x, new_y))
                visited[new_y][new_x] = True
                population_sum += field[new_y][new_x]
                union_cnt += 1

        if union_cnt > 1:
            queue.append((answer + 1, x, y))
            migration_queue.append((x, y))

            while migration_queue:
                cur_x, cur_y = migration_queue.popleft()

                field[cur_y][cur_x] = population_sum // union_cnt


if __name__ == '__main__':
    while queue:
        cur_stage, cur_x, cur_y = queue.popleft()

        # 스테이지가 바뀐 경우
        if cur_stage != answer:
            answer += 1

            # visited 초기화
            visited = [[False] * width for _ in range(width)]

        # 연합 조사
        grouping(cur_x, cur_y)

    print(answer)
