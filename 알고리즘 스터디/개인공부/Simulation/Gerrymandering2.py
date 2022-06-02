# https://www.acmicpc.net/problem/17779
import sys

width = int(sys.stdin.readline())
field = [[0] * (width + 1)] + [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(width)]
total = sum((sum(e) for e in field))


def check(x, y, d1, d2):
    area = [0] * 5
    visited = [[False] * (width + 1) for _ in range(width + 1)]

    visited[x][y] = True

    for e in range(d1):
        visited[x + e + 1][y - e - 1] = True

    for e in range(d2):
        visited[x + e + 1][y + e + 1] = True

    for e in range(d2):
        visited[x + d1 + e + 1][y - d1 + e + 1] = True

    for e in range(d1):
        visited[x + d2 + e + 1][y + d2 - e - 1] = True

    # 1번 선거구
    for row in range(1, x + d1):
        for col in range(1, y + 1):
            if visited[row][col]:
                break
            area[0] += field[row][col]
    # 2번 선거구
    for row in range(1, x + d2 + 1):
        for col in range(width, y, -1):
            if visited[row][col]:
                break
            area[1] += field[row][col]
    # 3번 선거구
    for row in range(x + d1, width + 1):
        for col in range(1, y - d1 + d2):
            if visited[row][col]:
                break
            area[2] += field[row][col]
    # 4번 선거구
    for row in range(x + d2 + 1, width + 1):
        for col in range(width, y - d1 + d2 - 1, -1):
            if visited[row][col]:
                break
            area[3] += field[row][col]

    area[4] = total - sum(area[:4])

    return max(area) - min(area)


if __name__ == '__main__':
    answer = 40001

    for row in range(1, width + 1):
        for col in range(1, width + 1):
            for d1 in range(1, width + 1):
                for d2 in range(1, width + 1):
                    if not col + d1 + d2 <= width:
                        break
                    if not 1 <= row - d1:
                        break
                    if not row + d2 <= width:
                        break
                    answer = min(answer, check(col, row, d1, d2))

    print(answer)
