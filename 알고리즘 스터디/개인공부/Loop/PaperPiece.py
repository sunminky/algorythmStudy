# https://www.acmicpc.net/problem/14391
import sys

height, width = map(int, sys.stdin.readline().split())
field = [sys.stdin.readline().rstrip() for _ in range(height)]


def row_check(row, start, end, visited):
    for col in range(start, end + 1):
        if visited[row][col]:
            return False
    return True


def col_check(col, start, end, visited):
    for row in range(start, end + 1):
        if visited[row][col]:
            return False
    return True


def row_calc(row, start, end):
    result = 0

    for col in range(start, end + 1):
        result = result * 10 + int(field[row][col])

    return result


def col_calc(col, start, end):
    result = 0

    for row in range(start, end + 1):
        result = result * 10 + int(field[row][col])

    return result


def split(cur_x, cur_y, visited, acc, remain):
    result = -1

    # 바운더리
    if cur_x >= width:
        return split(0, cur_y + 1, visited, acc, remain)

    # 끝까지 옴
    if remain == 0:
        return acc

    # 이미 점유 되었음
    if visited[cur_y][cur_x]:
        return split(cur_x + 1, cur_y, visited, acc, remain)

    # 가로 1 ~ width
    for col in range(cur_x, width):
        if row_check(cur_y, cur_x, col, visited):
            # 방문체크
            for _col in range(cur_x, col + 1):
                visited[cur_y][_col] = True
                remain -= 1

            result = max(result, split(col + 1, cur_y, visited, acc + row_calc(cur_y, cur_x, col), remain))

            # 방문해제
            for _col in range(cur_x, col + 1):
                visited[cur_y][_col] = False
                remain += 1

    # 세로 2 ~ height
    for row in range(cur_y + 1, height):
        if col_check(cur_x, cur_y, row, visited):
            # 방문체크
            for _row in range(cur_y, row + 1):
                visited[_row][cur_x] = True
                remain -= 1

            result = max(result, split(cur_x + 1, cur_y, visited, acc + col_calc(cur_x, cur_y, row), remain))

            # 방문해제
            for _row in range(cur_y, row + 1):
                visited[_row][cur_x] = False
                remain += 1

    return result


if __name__ == '__main__':
    print(split(0, 0, [[False] * width for _ in range(height)], 0, width * height))
