# https://www.acmicpc.net/problem/12852
import sys
from collections import deque

if __name__ == '__main__':
    target = int(sys.stdin.readline())
    calc_cnt = [[1000001, None] for _ in range(target + 1)]
    queue = deque([target])  # (계산횟수, 초기숫자)
    answer = [1]

    calc_cnt[target] = [0, None]

    while queue:
        _num = queue.popleft()

        if _num == 1:
            print(calc_cnt[1][0])
            break

        # 3으로 나누기
        if _num % 3 == 0:
            if calc_cnt[_num][0] + 1 < calc_cnt[_num // 3][0]:
                calc_cnt[_num // 3][0] = calc_cnt[_num][0] + 1
                calc_cnt[_num // 3][1] = _num
                queue.append(_num // 3)
        # 2로 나누기
        if _num % 2 == 0:
            if calc_cnt[_num][0] + 1 < calc_cnt[_num // 2][0]:
                calc_cnt[_num // 2][0] = calc_cnt[_num][0] + 1
                calc_cnt[_num // 2][1] = _num
                queue.append(_num // 2)
        # 1 빼기
        if _num - 1 > 0:
            if calc_cnt[_num][0] + 1 < calc_cnt[_num - 1][0]:
                calc_cnt[_num - 1][0] = calc_cnt[_num][0] + 1
                calc_cnt[_num - 1][1] = _num
                queue.append(_num - 1)

    trace = 1

    while calc_cnt[trace][1]:
        answer.append(calc_cnt[trace][1])
        trace = calc_cnt[trace][1]

    print(" ".join(map(str, reversed(answer))))
