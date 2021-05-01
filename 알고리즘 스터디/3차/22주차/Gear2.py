# https://www.acmicpc.net/problem/15662

import sys


gear = [list(sys.stdin.readline().rstrip()) for _ in range(int(sys.stdin.readline()))]


def rotate(gear, direction) -> list:
    if direction == 1:
        return [gear[-1]] + gear[:-1]
    return gear[1:] + [gear[0]]


def compare(flag, nth_gear, direction):
    cmp_range = ((nth_gear - 2, -1, -1), (nth_gear, len(gear), 1))
    cmp_gear = ((6, 2), (2, 6))
    cmp_idx = (1, -1)
    gear_copy = gear.copy()

    cur_direction = 0 if direction == 1 else 1
    for seq in range(*cmp_range[flag]):
        # seq + 1의 7번째 톱니와 seq의 3번째 톱니 비교
        if gear_copy[seq + cmp_idx[flag]][cmp_gear[flag][0]] == gear_copy[seq][cmp_gear[flag][1]]:
            break

        gear[seq] = rotate(gear[seq], cur_direction)
        cur_direction = 0 if cur_direction == 1 else 1


if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        nth_gear, direction = map(int, sys.stdin.readline().split())
        
        # nth 기어보다 앞에 있는 바퀴
        compare(0, nth_gear, direction)

        # nth 기어보다 뒤에 있는 바퀴
        compare(1, nth_gear, direction)
            
        # nth 기어 돌리기
        gear[nth_gear-1] = rotate(gear[nth_gear-1], direction)

    # 12시 방향이 s극인 바퀴 카운드
    print([e[0] for e in gear].count('1'))
