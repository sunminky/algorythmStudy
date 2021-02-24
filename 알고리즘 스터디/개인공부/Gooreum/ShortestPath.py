#https://level.goorm.io/exam/43082/%EC%B5%9C%EB%8B%A8-%EA%B1%B0%EB%A6%AC-%EA%B5%AC%ED%95%98%EA%B8%B0/quiz/1

import sys
from queue import PriorityQueue

if __name__ == '__main__':
    area = int(sys.stdin.readline())
    field_map = []
    visited = [[False for _ in range(area)] for _ in range(area)]
    movement = ((1, 0), (-1, 0), (0, 1), (0, -1))
    queue = PriorityQueue()

    for _ in range(area):
        field_map.append(sys.stdin.readline().split())

    queue.put((1, 0, 0))    #비용, x좌표, y좌표

    while not queue.empty():
        c_cost, c_x, c_y = queue.get()

        if c_x == area-1 and c_y == area-1:
            print(c_cost)
            break

        #탐색
        for _movement in movement:
            next_x = _movement[0] + c_x
            next_y = _movement[1] + c_y

            if 0 <= next_x < area and 0 <= next_y < area:
                if not visited[next_y][next_x] and field_map[next_y][next_x] == '1':
                    visited[next_y][next_x] = True
                    queue.put((c_cost+1, next_x, next_y))
