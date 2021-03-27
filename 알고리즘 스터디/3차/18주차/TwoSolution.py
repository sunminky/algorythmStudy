# https://www.acmicpc.net/problem/2470

import sys
from bisect import bisect_right

if __name__ == '__main__':
    sys.stdin.readline()   # 필요없음
    solution = sorted(map(int, sys.stdin.readline().split()))
    negative_pos = max(bisect_right(solution, -1) - 1, 0)       # 음의 정수 인덱스
    positive_pos = min(negative_pos + 1, len(solution) - 1)     # 양의 정수 인덱스
    answer = [0, 0, 2000000000]

    # 모든 용액이 음수인 경우
    if negative_pos - 1 >= 0:
        if answer[2] > abs(solution[negative_pos - 1] + solution[negative_pos]):
            answer[0] = solution[negative_pos - 1]
            answer[1] = solution[negative_pos]
            answer[2] = abs(solution[negative_pos - 1] + solution[negative_pos])

    # 모든 용액이 양수인 경우
    if positive_pos + 1 < len(solution):
        if answer[2] > abs(solution[positive_pos] + solution[positive_pos + 1]):
            answer[0] = solution[positive_pos]
            answer[1] = solution[positive_pos + 1]
            answer[2] = abs(solution[positive_pos] + solution[positive_pos + 1])

    while negative_pos < positive_pos:
        gap = solution[positive_pos] + solution[negative_pos]

        # 최소값 갱신
        if answer[2] > abs(gap):
            answer[0] = solution[negative_pos]
            answer[1] = solution[positive_pos]
            answer[2] = abs(gap)

            if gap == 0:
                break

        # 용액의 합이 양수이면 음수값을 줄임
        if gap > 0:
            negative_pos -= 1

            if negative_pos == -1:
                break

        # 용액의 합이 음수이면 양수값을 줄임
        else:
            positive_pos += 1

            if positive_pos == len(solution):
                break

    print(answer[0], answer[1])