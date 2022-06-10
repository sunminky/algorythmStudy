# https://www.acmicpc.net/problem/4991

import sys
from collections import deque


# 먼지 위치 구하기
def get_stain(width, height, field):
    stain_dict = dict()
    start = None

    for row in range(height):
        for col in range(width):
            if field[row][col] == "*":
                stain_dict[(col, row)] = len(stain_dict)
            elif field[row][col] == "o":
                start = (col, row)

    stain_dict[start] = len(stain_dict)

    return stain_dict


# 먼지간 거리 구하기
def get_distance(width, height, field, stain):
    distance = [dict() for _ in range(len(stain))]
    movement = ((1, 0), (-1, 0), (0, 1), (0, -1))

    for seq, node in enumerate(stain.keys()):
        queue = deque([(*node, 0)])
        visited = [[False] * width for _ in range(height)]

        visited[node[1]][node[0]] = True

        while queue:
            cur_x, cur_y, cur_dist = queue.popleft()

            for _move in movement:
                new_x = cur_x + _move[0]
                new_y = cur_y + _move[1]

                # 바운더리
                if not 0 <= new_x < width:
                    continue
                if not 0 <= new_y < height:
                    continue
                if visited[new_y][new_x]:
                    continue
                if field[new_y][new_x] == "x":
                    continue

                queue.append((new_x, new_y, cur_dist + 1))
                visited[new_y][new_x] = True

                if field[new_y][new_x] == "*":
                    distance[seq][stain[(new_x, new_y)]] = cur_dist + 1

        # 먼지에서 시작지점으로 가는 비용은 0
        distance[seq][len(stain) - 1] = 0

    return distance


def tsp(cur_visited, cur_node, dp, distance):
    # 이미 계산한 적이 있다면 계산한 값 리턴
    if dp[cur_node][cur_visited] is not None:
        return dp[cur_node][cur_visited]

    # 방문 안한 지점 탐색
    dp[cur_node][cur_visited] = 401
    for i in range(len(distance) - 1):
        if cur_visited & (1 << i):
            continue
        else:
            dp[cur_node][cur_visited] = min(dp[cur_node][cur_visited],
                                            tsp(cur_visited | (1 << i), i, dp, distance) + distance[cur_node][i])

    return dp[cur_node][cur_visited]


if __name__ == '__main__':
    while True:
        width, height = map(int, sys.stdin.readline().split())

        if width == 0 and height == 0:
            break

        field = [sys.stdin.readline().rstrip() for _ in range(height)]
        stain = get_stain(width, height, field) # 먼지 위치
        distance = get_distance(width, height, field, stain)    # 먼지간 거리
        all_visited = (1 << (len(stain) - 1)) - 1   # 모든 먼지를 방문했을 때 비트마스킹
        dp = [[None] * (1 << (len(stain) - 1)) for _ in range(len(stain))]

        for row in range(len(stain)):
            dp[row][all_visited] = 0

        # 시작지점에서 도달할 수 없는 먼지가 존재하는 경우
        if len(distance[-1]) != len(stain):
            answer = -1
        else:
            answer = tsp(0, len(stain) - 1, dp, distance)

        print(answer)
