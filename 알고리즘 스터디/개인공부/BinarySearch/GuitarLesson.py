# https://www.acmicpc.net/problem/2343
import sys

if __name__ == '__main__':
    _, n_cd = map(int, sys.stdin.readline().split())
    lessons = tuple(map(int, sys.stdin.readline().split()))

    min_t = max(lessons)    # cd의 크기는 레슨의 크기보다 커야함
    max_t = 2000000001

    # 이분탐색
    while min_t < max_t:
        cd_cnt = 0
        middle_t = (min_t + max_t) // 2
        acc_cnt = 0

        for e in lessons:
            # 레슨이 두개의 cd에 잘려서 들어가는건 불가능함
            if acc_cnt - e < 0:
                acc_cnt = middle_t
                cd_cnt += 1

            acc_cnt -= e

        if cd_cnt <= n_cd:
            max_t = middle_t
        else:
            min_t = middle_t + 1

    print(max_t)
