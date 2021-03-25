# https://www.acmicpc.net/problem/2339

import sys
field = tuple(tuple(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline())))


def divide(x_start, x_end, y_start, y_end, direction):
    impuriy = []    # 불순물 저장
    jewerly = []    # 보석 저장
    answer = 0

    # 불순물과 보석의 위치를 저장
    for row in range(y_start, y_end+1):
        for col in range(x_start, x_end+1):
            if field[row][col] == 1:
                impuriy.append((col, row))
            elif field[row][col] == 2:
                jewerly.append((col, row))

    # 보석1, 불순물0 이면 1반환 후 종료, 기저조건
    if len(jewerly) == 1 and len(impuriy) == 0:
        return 1
    else:
        # 각 불순물에 대해 가로/세로 나누기
        for _impuriy in impuriy:
            # 가로로 나누기
            if direction == 0:
                # 가로나누기 가능한지 체크
                available = True
                # 나누는 도중 보석이 있으면 나누기 불가능
                for i in range(x_start, x_end+1):
                    if field[_impuriy[1]][i] == 2:
                        available = False
                        break
                if available:
                    v1 = v2 = 0
                    # 현재 줄을 기준으로 자름
                    if y_start <= _impuriy[1]-1:
                        v1 = divide(x_start, x_end, y_start, _impuriy[1]-1, 1)
                    if _impuriy[1] + 1 <= y_end:
                        v2 = divide(x_start, x_end, _impuriy[1] + 1, y_end, 1)
                    answer += v1 * v2
            # 세로로 나누기
            else:
                # 세로 나누기 가능한지 체크
                available = True
                # 나누는 도중 보석이 있으면 나누기 불가능
                for i in range(y_start, y_end + 1):
                    if field[i][_impuriy[0]] == 2:
                        available = False
                        break
                if available:
                    v1 = v2 = 0
                    # 현재 줄칸 기준으로 자름
                    if x_start <= _impuriy[0]-1:
                        v1 = divide(x_start, _impuriy[0]-1, y_start, y_end, 0)
                    if _impuriy[0] + 1 <= x_end:
                        v2 = divide(_impuriy[0]+1, x_end, y_start, y_end, 0)
                    answer += v1 * v2

        return answer


if __name__ == '__main__':
    answer = 0
    answer += divide(0, len(field)-1, 0, len(field)-1, 0)    # 0 : 가로
    answer += divide(0, len(field)-1, 0, len(field)-1, 1)    # 1 : 세로

    # 나눌수 없으면 -1 출력
    if answer == 0:
        print(-1)
    else:
        print(answer)
