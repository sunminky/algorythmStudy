# https://www.acmicpc.net/problem/2473
import sys
from bisect import bisect_right

sys.stdin.readline()    # 안씀
solutions = sorted(map(int, sys.stdin.readline().split()))
negative_idx = bisect_right(solutions, -1) - 1  # 음의 용액 인덱스
positive_idx = negative_idx + 1


def same_all(start_idx, end_idx):
    sum_value = abs(sum(solutions[start_idx:end_idx + 1]))

    if sum_value < answer[3]:
        for i in range(3):
            answer[i] = solutions[end_idx + -1 * i]

        answer[3] = sum_value


if __name__ == '__main__':
    answer = [1000000000, 1000000000, 1000000001, 3000000001]

    # 음수 용액 3개
    if negative_idx - 2 >= 0:
        same_all(negative_idx - 2, negative_idx)

    # 양수 용액 3개
    if positive_idx + 2 < len(solutions):
        same_all(positive_idx, positive_idx + 2)

    # 음수 용액 2개 양수 용액 1개
    if negative_idx - 1 >= 0 and positive_idx < len(solutions):
        for i in range(positive_idx, len(solutions)):
            target = solutions[i]
            # 투포인터
            start_idx = 0
            end_idx = negative_idx

            while start_idx < end_idx:
                clac = abs(solutions[start_idx] + solutions[end_idx] + target)

                if clac < answer[3]:
                    answer[0] = solutions[start_idx]
                    answer[1] = solutions[end_idx]
                    answer[2] = target
                    answer[3] = clac

                if (solutions[start_idx] + solutions[end_idx]) * -1 <= target:  # -1을 곱한 이유는 절대값을 계산하기 위해서
                    end_idx -= 1
                else:
                    start_idx += 1

    # 음수 용액 1개 양수 용액 2개
    if negative_idx >= 0 and positive_idx + 1 < len(solutions):
        for i in range(negative_idx + 1):
            target = solutions[i]
            # 투포인터
            start_idx = positive_idx
            end_idx = len(solutions) - 1

            while start_idx < end_idx:
                clac = abs(solutions[start_idx] + solutions[end_idx] + target)

                if clac < answer[3]:
                    answer[0] = solutions[start_idx]
                    answer[1] = solutions[end_idx]
                    answer[2] = target
                    answer[3] = clac

                if solutions[start_idx] + solutions[end_idx] <= target * -1:    # -1을 곱한 이유는 절대값을 계산하기 위해서
                    start_idx += 1
                else:
                    end_idx -= 1

    print(" ".join(map(str, sorted(answer[:3]))))
