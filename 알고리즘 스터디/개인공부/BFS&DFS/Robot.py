# http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=285&sca=99&sfl=wr_subject&stx=%EB%A1%9C%EB%B4%87
import sys
from collections import deque

if __name__ == '__main__':
    h, w = map(int, sys.stdin.readline().split())   # 필드 높이,  필드 너비
    cost = [[[9999] * 4 for _ in range(w)] for _ in range(h)]   # 필드[행][열][방향] 일때 최소 비용
    field = [tuple(map(int, sys.stdin.readline().split())) for _ in range(h)]   # 필드저장
    robot_pos = tuple(map(int, sys.stdin.readline().split()))   # 로봇의 x좌표, y좌표, 방향
    target_pos = tuple(map(int, sys.stdin.readline().split()))  # 목적지의 x좌표, y좌표, 방향
    queue = deque()     # BFS에서 사용하는 큐
    dir_convert = [1, 3, 2, 0]  # 동서남북 -> 북서남북 으로 변환
    movement = ((0, -1), (1, 0), (0, 1), (-1, 0))  # 방향(북서남북)별 단위벡터

    queue.append((robot_pos[1] - 1, robot_pos[0] - 1, dir_convert[robot_pos[2] - 1], 0))    # 좌표x, 좌표y, 방향, 비용
    cost[robot_pos[0] - 1][robot_pos[1] - 1][dir_convert[robot_pos[2] - 1]] = 0     # 맨 처음 상태는 0의 비용으로 변화 가능

    while queue:
        c_x, c_y, c_dir, c_cost = queue.popleft()   # 현재 x좌표, 현재 y좌표, 현재 방향, 현재 위치&방향의 비용
        
        # 회전하는 경우 추가
        if field[c_y][c_x] != 1:    # 필드가 벽이 아닌 경우
            if cost[c_y][c_x][(c_dir - 1 + 4) % 4] > c_cost + 1:    # 왼쪽으로 회전
                cost[c_y][c_x][(c_dir - 1 + 4) % 4] = c_cost + 1
                queue.append((c_x, c_y, (c_dir - 1 + 4) % 4, c_cost + 1))

        if field[c_y][c_x] != 1:    # 필드가 벽이 아닌 경우
            if cost[c_y][c_x][(c_dir + 1) % 4] > c_cost + 1:    # 오른쪽으로 회전
                cost[c_y][c_x][(c_dir + 1) % 4] = c_cost + 1
                queue.append((c_x, c_y, (c_dir + 1) % 4, c_cost + 1))

        # 앞으로 가는 경우 추가
        for tok in range(1, 4):
            # 현재 방향 단위벡터에 스칼라 값을 곱해줌
            new_x = min(max(c_x + movement[c_dir][0] * tok, 0), w - 1)
            new_y = min(max(c_y + movement[c_dir][1] * tok, 0), h - 1)

            if field[new_y][new_x] != 1:
                if cost[new_y][new_x][c_dir] > c_cost + 1:
                    cost[new_y][new_x][c_dir] = c_cost + 1
                    queue.append((new_x, new_y, c_dir, c_cost + 1))
            else:
                # 벽때문에 가로막히는 경우 더 멀리 갈 수 없으므로 break
                break

    # 목적지의 x좌표, y좌표, 방향 일때 비용 출력
    print(cost[target_pos[0] - 1][target_pos[1] - 1][dir_convert[target_pos[2] - 1]])
