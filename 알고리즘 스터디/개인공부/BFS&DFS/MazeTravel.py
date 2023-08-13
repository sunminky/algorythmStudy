# https://www.acmicpc.net/problem/2178
import sys
import heapq

if __name__ == '__main__':
    height, width = map(int, sys.stdin.readline().split())
    field = tuple(tuple(int(e) for e in sys.stdin.readline().rstrip()) for _ in range(height))
    visited = [[False] * width for _ in range(height)]
    queue = []
    movement = ((1, 0), (-1, 0), (0, 1), (0, -1))

    heapq.heappush(queue, (1, 0, 0))  # 비용, x, y
    visited[0][0] = True

    while queue:
        _cost, _x, _y = heapq.heappop(queue)

        if _x == width - 1 and _y == height -1:
            print(_cost)
            break

        for _move in movement:
            new_x = _x + _move[0]
            new_y = _y + _move[1]

            # 바운더리
            if not 0 <= new_x < width:
                continue
            if not 0 <= new_y < height:
                continue

            # 방문여부
            if visited[new_y][new_x]:
                continue

            # 벽이 아님
            if field[new_y][new_x] != 1:
                continue

            visited[new_y][new_x] = True
            heapq.heappush(queue, (_cost + 1, new_x, new_y))
