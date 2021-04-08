# https://www.acmicpc.net/problem/4991

import sys
from collections import deque


def search(distance, visited, cost, cur_node):
    # 이미 방문한 노드인 경우
    if cost[cur_node][visited] != -1:
        return cost[cur_node][visited]
    else:
        cost[cur_node][visited] = 40001
        for i in range(len(distance)):
            # 이미 방문한 노드인 경우
            if visited & (1 << i):
                continue
            cost[cur_node][visited] = \
                min(cost[cur_node][visited], search(distance, visited | (1 << i), cost, i) + distance[cur_node][i])

        return cost[cur_node][visited]


# 외판원 순회
def tsp(distance, stain, start):
    cost = [[-1 for _ in range(1 << len(stain))] for _ in range(len(stain))]
    starting = 1 << stain[start]  # 청소기 위치 방문
    all_visited = (1 << len(stain)) - 1

    # 모든 노드를 방문한 경우에는 0으로 세팅(다시 출발지로 돌아갈 필요가 없기때문에)
    for i in range(len(cost)):
        cost[i][all_visited] = 0

    return search(distance, starting, cost, stain[start])


if __name__ == '__main__':
    while True:
        width, height = map(int, sys.stdin.readline().split())
        field = [sys.stdin.readline().rstrip() for _ in range(height)]
        stain = dict()  # 청소기, 쓰레기 좌표 저장
        start = None    # 청소기 위치 저장
        answer = -1

        if not (width and height):  # 둘 다 0 이면 종료
            break

        # 청소기, 쓰레기 좌표 탐색
        for row in range(height):
            for col in range(width):
                if field[row][col] == '*' or field[row][col] == 'o':
                    stain[(col, row)] = len(stain)
                if field[row][col] == 'o':
                    start = (col, row)

        distance = [[0 for _ in range(len(stain))] for _ in range(len(stain))]  # 쓰레기들의 거리 저장

        unreachable = False
        # 0(청소기) ~ 마지막 먼지 까지 거리 구하기
        for col, row in stain:
            visited = [[False for _ in range(width)] for _ in range(height)]
            queue = deque()
            queue.append((col, row, 0))
            visited[row][col] = True
            stain_cnt = len(stain)  # 도달한 먼지의 개수 카운트

            # 먼지 간 거리 구하기
            while queue:
                c_col, c_row, c_dis = queue.popleft()

                if field[c_row][c_col] == '*' or field[c_row][c_col] == 'o':
                    distance[stain[(col, row)]][stain[(c_col, c_row)]] = \
                        distance[stain[(c_col, c_row)]][stain[(col, row)]] = c_dis
                    stain_cnt -= 1

                if c_col - 1 >= 0 and field[c_row][c_col - 1] != 'x':
                    if visited[c_row][c_col - 1] is False:
                        visited[c_row][c_col - 1] = True
                        queue.append((c_col - 1, c_row, c_dis + 1))
                if c_col + 1 < width and field[c_row][c_col + 1] != 'x':
                    if visited[c_row][c_col + 1] is False:
                        visited[c_row][c_col + 1] = True
                        queue.append((c_col + 1, c_row, c_dis + 1))
                if c_row - 1 >= 0 and field[c_row - 1][c_col] != 'x':
                    if visited[c_row - 1][c_col] is False:
                        visited[c_row - 1][c_col] = True
                        queue.append((c_col, c_row - 1, c_dis + 1))
                if c_row + 1 < height and field[c_row + 1][c_col] != 'x':
                    if visited[c_row + 1][c_col] is False:
                        visited[c_row + 1][c_col] = True
                        queue.append((c_col, c_row + 1, c_dis + 1))

            # 도달할 수 없는 먼지가 있는 경우
            if stain_cnt != 0:
                unreachable = True
                break

        # 닿을 수 없는 먼지가 존재하지 않음
        if not unreachable:
            # 외판원 순회 실행
            answer = tsp(distance, stain, start)

        print(answer)
