# https://www.acmicpc.net/problem/16571
import sys

field = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
player = 0 if sum((e.count(1) for e in field)) == sum((e.count(2) for e in field)) else 1
remain = sum((e.count(0) for e in field))


def check(cur_player) -> bool:
    game_result = False  # True : 승, False : 무승부

    # 가로 체크
    for row in range(3):
        game_result |= field[row][0] == cur_player and field[row][1] == cur_player and field[row][2] == cur_player

    # 세로 체크
    for col in range(3):
        game_result |= field[0][col] == cur_player and field[1][col] == cur_player and field[2][col] == cur_player

    # 대각선 체크
    game_result |= (field[0][0] == cur_player and field[1][1] == cur_player and field[2][2] == cur_player) or (
                field[0][2] == cur_player and field[1][1] == cur_player and field[2][0] == cur_player)

    return game_result


def play(remain, cur_player):
    # 패 : 0, 무승부 : 1, 승 : 2
    minmax_func = max if cur_player == player else min
    init_value = -1 if cur_player == player else 100

    # 남은 칸 없음
    if remain == 0:
        return 1

    # 말 놓기
    for row in range(3):
        for col in range(3):
            if field[row][col] != 0:
                continue

            # 말 놓기
            field[row][col] = cur_player + 1
            game_result = check(cur_player + 1)

            # 승패가 난 경우
            if game_result:
                init_value = minmax_func(init_value, 2 if cur_player == player else 0)
            else:
                init_value = minmax_func(init_value, play(remain - 1, (cur_player + 1) & 1))

            # 되돌리기
            field[row][col] = 0

    return init_value


if __name__ == '__main__':
    result_dict = {0: 'L', 1: 'D', 2: 'W'}

    print(result_dict[play(remain, player)])
