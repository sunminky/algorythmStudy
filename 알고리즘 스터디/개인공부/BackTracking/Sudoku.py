# https://www.acmicpc.net/problem/2580
import sys

field = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
candidate = []  # [x, y, 후보군]


def check(field, x, y, new_num):
    candidate_mask = 0

    # 가로줄 체크
    for e in field[y]:
        if e == 0:
            continue

        candidate_mask |= (1 << (e - 1))

    # 세로줄 체크
    for row in range(9):
        if field[row][x] == 0:
            continue

        candidate_mask |= (1 << (field[row][x] - 1))

    # 3 x 3 칸 체크
    for row in range(y // 3 * 3, (y // 3 + 1) * 3):
        for col in range(x // 3 * 3, (x // 3 + 1) * 3):
            if field[row][col] == 0:
                continue

            candidate_mask |= (1 << (field[row][col] - 1))

    return not candidate_mask & (1 << (new_num - 1))


def deploy(candidate_seq):
    if candidate_seq >= len(candidate):
        return True

    for e in candidate[candidate_seq][2]:
        if check(field, candidate[candidate_seq][0], candidate[candidate_seq][1], e):
            # 새로운 숫자 기입
            field[candidate[candidate_seq][1]][candidate[candidate_seq][0]] = e

            # 전체 성공
            if deploy(candidate_seq + 1):
                return True

            # 원상복구
            field[candidate[candidate_seq][1]][candidate[candidate_seq][0]] = 0

    return False


def find_candidate(field, x, y):
    candidate_mask = 0

    # 가로줄 체크
    for e in field[y]:
        if e == 0:
            continue

        candidate_mask |= (1 << (e - 1))

    # 세로줄 체크
    for row in range(9):
        if field[row][x] == 0:
            continue

        candidate_mask |= (1 << (field[row][x] - 1))

    # 3 x 3 칸 체크
    for row in range(y // 3 * 3, (y // 3 + 1) * 3):
        for col in range(x // 3 * 3, (x // 3 + 1) * 3):
            if field[row][col] == 0:
                continue

            candidate_mask |= (1 << (field[row][col] - 1))

    return tuple((i + 1 for i in range(9) if not candidate_mask & (1 << i)))


if __name__ == '__main__':
    for row in range(9):
        for col in range(9):
            if field[row][col] == 0:
                _candidate = find_candidate(field, col, row)

                if len(_candidate) == 1:
                    field[row][col] = _candidate[0]
                else:
                    candidate.append((col, row, _candidate))

    deploy(0)

    for e in field:
        print(" ".join(map(str, e)))
