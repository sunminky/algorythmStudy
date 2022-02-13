# https://www.acmicpc.net/problem/2110
import sys

if __name__ == '__main__':
    n_home, n_router = map(int, sys.stdin.readline().split())
    routers = sorted([int(sys.stdin.readline()) for _ in range(n_home)])
    answer = 0

    start = 0
    end = 1000000001

    while start < end:
        middle = (start + end) // 2     # 최소 거리
        remain_router = n_router - 1    # 남은 공유기 개수, 제일 처음 자리에 있는 공유기 제외
        prev_idx = 0                    # 제일 처음 자리에 공유기 설치

        for idx in range(len(routers)):
            if routers[idx] - routers[prev_idx] < middle:
                continue
            prev_idx = idx
            remain_router -= 1

        if remain_router > 0:
            end = middle
        else:
            start = middle + 1
            answer = max(answer, middle)

    print(answer)
