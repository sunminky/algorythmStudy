# https://www.acmicpc.net/problem/2842
import sys
from collections import deque


# 우체국 위치 반환
def find_postoffice(field):
    for row, line in enumerate(field):
        findidx = line.find('P')

        if findidx != -1:
            return findidx, row


# 중복되는 고도 제거
def remove_duplicate(altitude):
    result = set()
    [result.update(e) for e in altitude]

    return sorted(result)


# 주어진 고도 내에서 모든 도착지점을 갈 수 있는지
def search(field, altitude, limit, postoffice, home_cnt) -> bool:
    queue = deque()
    visited = [[False] * len(field) for _ in range(len(field))]
    remain_home = home_cnt
    movement = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))

    if limit[0] <= altitude[postoffice[1]][postoffice[0]] <= limit[1]:
        queue.append(postoffice)
        visited[postoffice[1]][postoffice[0]] = True

    while queue:
        cur_x, cur_y = queue.popleft()

        if field[cur_y][cur_x] == 'K':
            remain_home -= 1

            if remain_home == 0:
                return True

        for v_x, v_y in movement:
            new_x = cur_x + v_x
            new_y = cur_y + v_y

            if 0 <= new_x < len(field) and 0 <= new_y < len(field):
                if visited[new_y][new_x] is False and limit[0] <= altitude[new_y][new_x] <= limit[1]:
                    queue.append((new_x, new_y))
                    visited[new_y][new_x] = True
    else:
        return False


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    field = [sys.stdin.readline().rstrip() for _ in range(n)]
    altitude = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    postoffice = find_postoffice(field) # 우체국 위치
    home_cnt = sum([field[i].count('K') for i in range(n)])     # 배달해야할 집의 개수 카운트
    altitude_variety = remove_duplicate(altitude)
    answer = 1000000

    ## 투 포인터 ##
    start_idx = end_idx = 0
    while start_idx != len(altitude_variety) and end_idx != len(altitude_variety):

        if search(field, altitude, (altitude_variety[start_idx], altitude_variety[end_idx]), postoffice, home_cnt):
            answer = min(answer, altitude_variety[end_idx] - altitude_variety[start_idx])
            start_idx += 1
            end_idx = max(end_idx, start_idx)
        else:
            end_idx = end_idx + 1

    print(answer)
