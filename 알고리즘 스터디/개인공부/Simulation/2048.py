# https://www.acmicpc.net/problem/12100
import sys
import copy
from collections import deque


def move(field, remain) -> int:
    answer = 0
    width = len(field)

    if remain == 0:
        return 0

    # 상
    new_field = copy.deepcopy(field)
    score = 0
    ''' 위로 밀기 '''
    for col in range(width):
        queue = deque()
        for row in range(width):
            if new_field[row][col] == 0:
                continue
            queue.append(new_field[row][col])
        # 채우기
        store_idx = 0
        while queue:
            if len(queue) >= 2:
                e1 = queue[0]
                e2 = queue[1]

                if e1 == e2:
                    new_field[store_idx][col] = e1 + e2
                    store_idx += 1
                    queue.popleft()
                    queue.popleft()
                    score = max(score, e1 + e2)
                else:
                    new_field[store_idx][col] = e1
                    store_idx += 1
                    queue.popleft()
                    score = max(score, e1)

            elif len(queue) == 1:
                e1 = queue.popleft()
                new_field[store_idx][col] = e1
                store_idx += 1
                score = max(score, e1)

        for row in range(store_idx, width):
            new_field[row][col] = 0

    answer = max(answer, move(new_field, remain - 1), score)

    # 우
    new_field = copy.deepcopy(field)
    score = 0
    ''' 오른쪽으로 밀기 '''
    for row in range(width):
        queue = deque()
        for col in range(width - 1, -1, -1):
            if new_field[row][col] == 0:
                continue
            queue.append(new_field[row][col])
        # 채우기
        store_idx = width - 1
        while queue:
            if len(queue) >= 2:
                e1 = queue[0]
                e2 = queue[1]

                if e1 == e2:
                    new_field[row][store_idx] = e1 + e2
                    store_idx -= 1
                    queue.popleft()
                    queue.popleft()
                    score = max(score, e1 + e2)
                else:
                    new_field[row][store_idx] = e1
                    store_idx -= 1
                    queue.popleft()
                    score = max(score, e1)

            elif len(queue) == 1:
                e1 = queue.popleft()
                new_field[row][store_idx] = e1
                store_idx -= 1
                score = max(score, e1)

        for col in range(store_idx, -1, -1):
            new_field[row][col] = 0

    answer = max(answer, move(new_field, remain - 1), score)

    # 하
    new_field = copy.deepcopy(field)
    score = 0
    ''' 아래로 밀기 '''
    for col in range(width):
        queue = deque()
        for row in range(width - 1, -1, -1):
            if new_field[row][col] == 0:
                continue
            queue.append(new_field[row][col])
        # 채우기
        store_idx = width - 1
        while queue:
            if len(queue) >= 2:
                e1 = queue[0]
                e2 = queue[1]

                if e1 == e2:
                    new_field[store_idx][col] = e1 + e2
                    store_idx -= 1
                    queue.popleft()
                    queue.popleft()
                    score = max(score, e1 + e2)
                else:
                    new_field[store_idx][col] = e1
                    store_idx -= 1
                    queue.popleft()
                    score = max(score, e1, e2)

            elif len(queue) == 1:
                e1 = queue.popleft()
                new_field[store_idx][col] = e1
                store_idx -= 1
                score = max(score, e1)

        for row in range(store_idx, -1, -1):
            new_field[row][col] = 0

    answer = max(answer, move(new_field, remain - 1), score)

    # 좌
    new_field = copy.deepcopy(field)
    score = 0
    ''' 왼족으로 밀기 '''
    for row in range(width):
        queue = deque()
        for col in range(width):
            if new_field[row][col] == 0:
                continue
            queue.append(new_field[row][col])
        # 채우기
        store_idx = 0
        while queue:
            if len(queue) >= 2:
                e1 = queue[0]
                e2 = queue[1]

                if e1 == e2:
                    new_field[row][store_idx] = e1 + e2
                    store_idx += 1
                    queue.popleft()
                    queue.popleft()
                    score = max(score, e1 + e2)
                else:
                    new_field[row][store_idx] = e1
                    store_idx += 1
                    queue.popleft()
                    score = max(score, e1, e2)

            elif len(queue) == 1:
                e1 = queue.popleft()
                new_field[row][store_idx] = e1
                store_idx += 1
                score = max(score, e1)

        for col in range(store_idx, width):
            new_field[row][col] = 0

    answer = max(answer, move(new_field, remain - 1), score)

    return answer


if __name__ == '__main__':
    width = int(sys.stdin.readline())
    field = [list(map(int, sys.stdin.readline().split())) for _ in range(width)]

    print(move(field, 5))
