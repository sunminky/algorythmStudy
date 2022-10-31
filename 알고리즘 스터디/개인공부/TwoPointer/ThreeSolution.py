# https://www.acmicpc.net/problem/2473
import sys

if __name__ == '__main__':
    n_solution = int(sys.stdin.readline())
    solution = sorted(map(int, sys.stdin.readline().split()))
    answer = [3000000001, -1, -1, -1]  # 최소값, 1번 용액, 2번 용액, 3번 용액

    for seq, e in enumerate(solution):
        start, end = 0, n_solution - 1

        if answer[0] == 0:
            break

        # 수정 필요
        while start < end:
            if start == seq:
                start += 1
                continue

            if end == seq:
                end -= 1
                continue

            if abs(solution[start] + solution[end] + e) < answer[0]:
                answer[0], answer[1], answer[2], answer[3] = abs(solution[start] + solution[end] + e), e, solution[
                    start], solution[end]

            if solution[start] + solution[end] >= -e:
                end -= 1
            else:
                start += 1

    print(" ".join(map(str, sorted(answer[1:]))))