# https://www.acmicpc.net/problem/9663
import sys

width = int(sys.stdin.readline())
y_pos = [False] * width
visited = []


def deploy(remain) -> int:
    result = 0

    # 퀸을 다 놓음
    if remain == 0:
        return 1

    for row in range(width):
        # 세로 체크
        if y_pos[row]:
            continue
        # 대각선 체크
        for e in visited:
            if (e[0] - width + remain) ** 2 == (e[1] - row) ** 2:
                break
        else:
            # 놓기
            visited.append((width - remain, row))
            y_pos[row] = True
            result += deploy(remain - 1)
            del visited[-1]
            y_pos[row] = False

    return result


if __name__ == '__main__':
    print(deploy(width))
