# https://www.acmicpc.net/problem/9663
import sys

width = int(sys.stdin.readline())
field = [[True] * width for _ in range(width)]
visited = [[False] * width for _ in range(width)]
x_visited = [False] * width
y_visited = [False] * width


def deploy(remain):
    result = 0

    # 모든 queen을 다 놓음
    if remain == 0:
        return 1

    # n 번째 퀸, n 번째 칸
    for row in range(width):
        is_fail = False
        x_plus_y = row + remain - 1
        x_minus_y = remain - 1 - row

        # 가로 체크
        if y_visited[row]:
            continue
        # 대각선 체크
        for row2 in range(max(0, x_plus_y - width + 1), min(x_plus_y + 1, width)):
            if visited[row2][x_plus_y - row2]:
                is_fail = True
                break
        else:
            # 대각선 체크
            for row2 in range(row - min(row, remain - 1), min(width - x_minus_y, width)):
                if visited[row2][row2 + x_minus_y]:
                    is_fail = True
                    break

        if not is_fail:
            # 놓기
            x_visited[remain - 1] = y_visited[row] = visited[row][remain - 1] = True
            # 다음 퀸 배치
            result += deploy(remain - 1)
            # 복구하기
            x_visited[remain - 1] = y_visited[row] = visited[row][remain - 1] = False

    return result


if __name__ == '__main__':
    print(deploy(width))
