# https://www.acmicpc.net/problem/2473
import sys

if __name__ == '__main__':
    _, solution = sys.stdin.readline(), sorted(map(int, sys.stdin.readline().split()))
    answer = [3000000001, -1, -1, -1]

    for seq in range(len(solution)):
        pick, start, end = solution[seq], seq + 1, len(solution) - 1

        if answer[0] == 0:
            break

        while start < end:
            if answer[0] > abs(pick + solution[start] + solution[end]):
                answer[0], answer[1], answer[2], answer[3] = abs(pick + solution[start] + solution[end]), pick, \
                                                             solution[start], solution[end]

            if pick + solution[start] + solution[end] < 0:
                start += 1
            else:
                end -= 1

    print(" ".join(map(str, answer[1:])))