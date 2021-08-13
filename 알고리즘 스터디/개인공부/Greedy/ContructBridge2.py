# https://www.acmicpc.net/problem/17472
# 프림 or (크루스칼 + 유니언 파인드)
import sys
from collections import deque
from queue import PriorityQueue

if __name__ == '__main__':
    height, width = map(int, sys.stdin.readline().split())    # 높이, 너비
    field = [tuple(map(int, sys.stdin.readline().split())) for _ in range(height)]
    group = [[0] * width for _ in range(height)]  # 그룹 위치 저장
    group_cnt = 0   # 그룹 번호 지정
    visited = [[False] * width for _ in range(height)]  # 방문여부
    answer = 0  # 다리 건설 비용

    ''' 그룹 만들기 '''
    for row in range(height):
        for col in range(width):
            # 섬을 만난경우, 섬의 경계 탐색
            if not visited[row][col] and field[row][col]:
                group_cnt += 1

                ''' BFS '''
                queue = deque()
                queue.append((col, row))

                while queue:
                    cur_x, cur_y = queue.popleft()
                    visited[cur_y][cur_x] = True
                    group[cur_y][cur_x] = group_cnt
                    movement = ((0, 1), (1, 0), (0, -1), (-1, 0))

                    for direction_x, direction_y in movement:
                        new_x = cur_x + direction_x
                        new_y = cur_y + direction_y

                        # 바운더리 체크
                        if -1 < new_x < width and -1 < new_y < height:
                            if not visited[new_y][new_x] and field[new_y][new_x] == field[cur_y][cur_x]:
                                queue.append((new_x, new_y))

            visited[row][col] = True

    ''' 간선 만들기 '''
    edge = [dict() for _ in range(group_cnt)]   # 간선 저장

    # 가로줄 탐색
    for row in range(height):
        prev_idx = 0
        for col in range(width):
            if group[row][prev_idx] == group[row][col]:
                prev_idx = col
            else:
                # 다른 섬을 만난 경우
                if group[row][col] != 0:
                    if group[row][prev_idx] != 0 and col - prev_idx - 1 > 1:
                        edge[group[row][prev_idx] - 1][group[row][col] - 1] = min(edge[group[row][prev_idx] - 1].get(group[row][col] - 1, 100), col - prev_idx - 1)
                        edge[group[row][col] - 1][group[row][prev_idx] - 1] = min(edge[group[row][col] - 1].get(group[row][prev_idx] - 1, 100), col - prev_idx - 1)
                    prev_idx = col

    # 세로줄 탐색
    for col in range(width):
        prev_idx = 0
        for row in range(height):
            if group[prev_idx][col] == group[row][col]:
                prev_idx = row
            else:
                # 다른 섬을 만나는 경우
                if group[row][col] != 0:
                    if group[prev_idx][col] != 0:
                        # 1이하면 안들어가게 하기
                        if row - prev_idx - 1 > 1:
                            edge[group[prev_idx][col] - 1][group[row][col] - 1] = min(edge[group[prev_idx][col] - 1].get(group[row][col] - 1, 100), row - prev_idx - 1)
                            edge[group[row][col] - 1][group[prev_idx][col] - 1] = min(edge[group[row][col] - 1].get(group[prev_idx][col] - 1, 100), row - prev_idx - 1)
                    prev_idx = row

    ''' 프림 알고리즘 '''
    edge_cnt = group_cnt - 1
    edge_visited = [[False] * group_cnt for _ in range(group_cnt)]   # 간선 방문여부
    visited_island = [False] * group_cnt    # 방문한 섬 체크
    queue = PriorityQueue()

    # 1번 그룹이랑 붙어있는 애들 다 큐에 넣음
    for neigh in edge[0].keys():
        queue.put((edge[0][neigh], 0, neigh))   # 건설비용, 출발지, 도착지
        edge_visited[0][neigh] = edge_visited[neigh][0] = True

    while not queue.empty():
        cur_cost, cur_src, cur_dst = queue.get()

        if visited_island[cur_src] and visited_island[cur_dst]:
            continue

        answer += cur_cost
        edge_cnt -= 1
        visited_island[cur_src] = visited_island[cur_dst] = True

        if edge_cnt == 0:
            break
        
        # 목적지와 연결된 간선 추가
        for neigh in edge[cur_dst].keys():
            if not edge_visited[cur_dst][neigh] and not visited_island[neigh]:
                queue.put((edge[cur_dst][neigh], cur_dst, neigh))
                edge_visited[cur_dst][neigh] = edge_visited[neigh][cur_dst] = True

    if edge_cnt:
        print(-1)
    else:
        print(answer)
