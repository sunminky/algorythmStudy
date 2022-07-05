# https://www.acmicpc.net/problem/2110
import sys

if __name__ == '__main__':
    n_home, n_router = map(int, sys.stdin.readline().split())
    routers = sorted([int(sys.stdin.readline()) for _ in range(n_home)])
    worst, best = 0, 1000000001

    while worst < best:
        middle = (worst + best) // 2
        cnt = n_router
        prev = -1000000001  # 무조건 첫 번째 집에 공유기가 놓일 수 있게 무한의 값 세팅

        for e in routers:
            if e - prev >= middle:
                cnt -= 1
                prev = e

        if cnt > 0:
            best = middle
        else:
            worst = middle + 1

    print(best - 1)
