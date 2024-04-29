# https://school.programmers.co.kr/learn/courses/30/lessons/250136
from collections import deque


def find(land, field, x, y, group_num) -> int:
    queue = deque([(x, y)])
    result = 0
    movement = ((0, -1), (0, 1), (-1, 0), (1, 0))
    field[y][x] = group_num

    while queue:
        cur_x, cur_y = queue.popleft()
        result += 1

        for _move in movement:
            _x = cur_x + _move[0]
            _y = cur_y + _move[1]

            # 바운더리 체크
            if not 0 <= _y < len(land):
                continue

            if not 0 <= _x < len(land[_y]):
                continue

            if field[_y][_x] == -1 and land[_y][_x] == 1:
                field[_y][_x] = group_num
                queue.append((_x, _y))

    return result


def solution(land):
    field = [[-1] * len(land[row]) for row in range(len(land))]
    group_num = 0
    benefit = {}
    visited = [False] * 250001
    answer = 0

    for row in range(len(land)):
        for col in range(len(land[row])):
            if field[row][col] == -1 and land[row][col] == 1:
                benefit[group_num] = find(land, field, col, row, group_num)
                group_num += 1

    for col in range(len(land[0])):
        result = 0
        restore_queue = deque()

        for row in range(len(land)):
            if visited[field[row][col]]:
                continue

            visited[field[row][col]] = True
            restore_queue.append(field[row][col])
            result += benefit.get(field[row][col], 0)

        answer = max(answer, result)

        for e in restore_queue:
            visited[e] = False

    return answer


if __name__ == '__main__':
    print(solution(
        [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 0, 1, 1]]))  # 9
    print(solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1],
                    [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]))  # 16
    print(solution([[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 0, 1], [1, 0, 1, 0, 1, 0]]))  # 2
    print(solution([[0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0]]))  # 4
