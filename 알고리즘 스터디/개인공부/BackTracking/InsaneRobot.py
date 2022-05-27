# https://www.acmicpc.net/problem/1405
import sys

count, *potential = map(int, sys.stdin.readline().split())
case_cnt = sum(map(lambda x: 1 if x else 0, potential))


def travel(remain, cur_x, cur_y, visited, acc) -> int:
    result = 0
    movement = ((1, 0), (-1, 0), (0, 1), (0, -1))

    if visited[cur_y][cur_x]:
        return acc

    if remain == 0:
        return 0

    visited[cur_y][cur_x] = True

    for i in range(4):
        if potential[i]:
            result += travel(remain - 1, cur_x + movement[i][0], cur_y + movement[i][1], visited, acc * (potential[i] / 100))

    visited[cur_y][cur_x] = False

    return result


if __name__ == '__main__':
    print(1.0 - travel(count, 14, 14, [[False] * 29 for _ in range(29)], 1))
