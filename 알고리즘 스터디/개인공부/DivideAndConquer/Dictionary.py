# https://www.acmicpc.net/problem/1256

import sys


def dig(a_cnt, z_cnt, sequence):
    # 기저조건
    if a_cnt == 0:
        return 'z' * z_cnt
    elif z_cnt == 0:
        return 'a' * a_cnt

    cases = 1   # (z_cnt-1)! / (z_cnt-1)!
    # 앞에 a가 오는 경우
    for a in range(a_cnt):
        if a != 0:
            cases = cases * (z_cnt - 1 + a) // a
            
        if sequence <= cases:
            # 조합 출력
            return 'a' * (a_cnt - a) + 'z' + dig(a, z_cnt-1, sequence)

        sequence -= cases

    # cases == (a_cnt-1 + z_cnt-1)! / ((a_cnt-1)! (z_cnt-1)!)
    # 앞에 z가 오는 경우
    for z in range(1, z_cnt + 1):
        if z != 1:
            cases = cases * (z_cnt - z + 1) // (a_cnt - 1 + z_cnt - z + 1)

        if sequence <= cases:
            # 조합 출력
            return 'z' * z + 'a' + dig(a_cnt-1, z_cnt-z, sequence)

        sequence -= cases


if __name__ == '__main__':
    n_a, n_z, sequence = map(int, sys.stdin.readline().split())
    result = dig(n_a, n_z, sequence)

    if result:
        print(result)
    else:
        print(-1)
