# https://www.acmicpc.net/problem/17825
import sys

pattern = tuple(map(int, sys.stdin.readline().split()))
red_line = {0: 1,
            1: 2,
            2: 3,
            3: 4,
            4: 5,
            5: 6,
            6: 7,
            7: 8,
            8: 9,
            9: 10,
            10: 11,
            11: 12,
            12: 13,
            13: 14,
            14: 15,
            15: 16,
            16: 17,
            17: 18,
            18: 19,
            19: 20,
            20: 32,
            21: 22,
            22: 23,
            23: 29,
            24: 25,
            25: 29,
            26: 27,
            27: 28,
            28: 29,
            29: 30,
            30: 31,
            31: 20,
            32: 32}
blue_line = {5: 21,
             10: 24,
             15: 26}
costs = (0, 2, 4, 6, 8, 10, 12, 14, 16, 18,
         20, 22, 24, 26, 28, 30, 32, 34, 36, 38,
         40, 13, 16, 19, 22, 24, 28, 27, 26, 25,
         30, 35, 0)


# start에서 step 만큼 움직임
def move(start, step):
    if start in blue_line:
        next_spot = blue_line[start]
    else:
        next_spot = red_line[start]

    for _ in range(step - 1):
        next_spot = red_line[next_spot]

    return next_spot


def play(occupied, process_cnt, player):
    answer = 0

    if process_cnt == 10:
        return sum((sum((costs[spot] for spot in _player)) for _player in player))

    # 플레이어 1 ~ 4
    for seq in range(4):
        next_spot = move(player[seq][-1], pattern[process_cnt])

        if occupied[next_spot]:
            continue
        else:
            # 현재 칸 비워줌
            occupied[player[seq][-1]] = False

            # 방문 기록에 추가
            player[seq].append(next_spot)

            # 플레이어가 칸 점유
            occupied[next_spot] = True
            occupied[32] = False

            answer = max(play(occupied, process_cnt + 1, player), answer)

            # 원상 복구
            player[seq].pop()
            occupied[next_spot] = False
            occupied[player[seq][-1]] = True

    return answer


if __name__ == '__main__':
    print(play([False] * 33, 0, [[0] for _ in range(4)]))
