# https://www.acmicpc.net/problem/3190

import sys
from collections import deque

N = int(sys.stdin.readline())
field = [[0 for _ in range(N)] for _ in range(N)]
direction = 0  # 기본적으로 오른쪽으로 이동
queue = deque([[0, 0]])  # 뱀 몸통 좌표 저장
movement = ((1, 0), (0, 1), (-1, 0), (0, -1))
drct_dict = {'D': 1, 'L': -1}


# 벽에 부딫히거나 몸에 부딫히면 True 반환
def collision_check() -> bool:
    head_x = queue[-1][0] + movement[direction][0]
    head_y = queue[-1][1] + movement[direction][1]

    # 벽에 부딫힘
    if head_y == N or head_y == -1 or head_x == N or head_x == -1:
        return True

    # 자기 몸에 부딫히거나
    if field[head_y][head_x] == -1:
        return True

    # 이동
    queue.append([head_x, head_y])

    # 사과인 경우
    if field[head_y][head_x] == 1:
        pass
    else:
        x, y = queue.popleft()  # 몸을 치움
        field[y][x] = 0     # 몸을 치움

    field[head_y][head_x] = -1  # 몸이 있다는 표시

    return False


if __name__ == '__main__':
    answer = 0
    field[0][0] = -1

    # 사과 위치 저장
    for _ in range(int(sys.stdin.readline())):
        row, col = map(int, sys.stdin.readline().split())
        field[row - 1][col - 1] = 1

    # 움직임 저장
    for _ in range(int(sys.stdin.readline())):
        cnt, drct = sys.stdin.readline().split()

        for _ in range(int(cnt) - answer):
            answer += 1

            # 충돌 체크
            if collision_check():
                print(answer)
                exit(0)

        # 방향 전환
        direction = (direction + drct_dict[drct]) % len(movement) if direction + drct_dict[drct] >= 0 else len(movement) - 1

    # 부딫힐 때 까지 진행
    while True:
        answer += 1

        # 충돌 체크
        if collision_check():
            print(answer)
            break
