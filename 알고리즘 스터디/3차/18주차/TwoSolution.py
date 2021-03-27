# https://www.acmicpc.net/problem/2470

import sys
from bisect import bisect_right

if __name__ == '__main__':
    sys.stdin.readline()   # 필요없음
    solution = sorted(map(int, sys.stdin.readline().split()))
    negative_pos = max(bisect_right(solution, -1) - 1, 0)       # 음의 정수 인덱스
    positive_pos = min(negative_pos + 1, len(solution) - 1)     # 양의 정수 인덱스
    answer = [solution[negative_pos], solution[positive_pos], abs(solution[positive_pos] + solution[negative_pos])]

    # 모두 음수인 경우
    if solution[-1] < 0:
        print(solution[-2], solution[-1])
        exit(0)

    while negative_pos != 0 or positive_pos != len(solution):
        gap = solution[positive_pos] + solution[negative_pos]

        # 최소값 갱신
        if answer[2] > abs(gap):
            answer[0] = solution[negative_pos]
            answer[1] = solution[positive_pos]
            answer[2] = abs(gap)

            if gap == 0:
                break

        if gap > 0:
            negative_pos -= 1

            if negative_pos == -1:
                break

        else:
            positive_pos += 1

            if positive_pos == len(solution):
                break

    print(answer[0], answer[1])
