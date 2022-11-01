# https://www.acmicpc.net/problem/1931
import sys

if __name__ == '__main__':
    conference = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))],
                        key=lambda x: (x[1], x[0]))
    end = 0
    answer = 0

    for e in conference:
        if e[0] >= end:
            answer += 1
            end = e[1]

    print(answer)
