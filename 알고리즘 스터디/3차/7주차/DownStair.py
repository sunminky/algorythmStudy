# https://www.acmicpc.net/problem/1520

import sys

sys.setrecursionlimit(10000)


def search(x, y):
    global my_map
    global height
    global width
    global stuck_map

    ret = 0

    if x == width - 1 and y == height - 1:
        return 1

    if num_ways[y][x]:
        num_ways[y][x] += 1
        return 1

    # 위
    if y > 0:
        if not stuck_map[y-1][x] and my_map[y - 1][x] < my_map[y][x]:
            ret += search(x, y - 1)
    # 아래
    if y < height - 1:
        if not stuck_map[y+1][x] and my_map[y + 1][x] < my_map[y][x]:
            ret += search(x, y + 1)
    # 좌
    if x > 0:
        if not stuck_map[y][x-1] and my_map[y][x - 1] < my_map[y][x]:
            ret += search(x - 1, y)
    # 우
    if x < width - 1:
        if not stuck_map[y][x+1] and my_map[y][x + 1] < my_map[y][x]:
            ret += search(x + 1, y)

    num_ways[y][x] = ret

    if not ret:
        stuck_map[y][x] = True

    return ret


if __name__ == '__main__':
    global my_map, height, width, num_ways, stuck_map
    height, width = tuple(map(int, sys.stdin.readline().rstrip().split()))  # 지도 높이, 지도 너비
    my_map = []
    num_ways = [[0 for _ in range(width)] for _ in range(height)]
    stuck_map = [[False for _ in range(width)] for _ in range(height)]

    for _ in range(height):
        my_map.append(list(map(int, sys.stdin.readline().rstrip().split())))

    # 상 하 좌 우 탐색
    search(0, 0)
    print(num_ways[0][0])
