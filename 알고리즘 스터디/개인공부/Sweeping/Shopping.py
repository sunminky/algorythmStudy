# https://www.acmicpc.net/problem/10332

import sys

if __name__ == '__main__':
    n_city, n_restrict = map(int, sys.stdin.readline().split())
    restrict = sorted([[*map(int, sys.stdin.readline().split())] for _ in range(n_restrict)],
                      key=lambda x: (x[0], -x[1]))
    answer = 1
    cur_loc = 1  # 현재 위치
    end = 0  # 먼저 들러야 하는 가게의 위치
    idx = 0

    while idx < n_restrict:
        src, dst = restrict[idx]
        end = dst
        answer += src - cur_loc  # 오는데 걸리는 비용

        idx += 1
        # end 보다 작은 시작점이 나오면 없애줌
        while idx < n_restrict:
            if restrict[idx][0] <= end:
                end = max(end, restrict[idx][1])
                idx += 1
            else:
                break

        answer += (end - src) * 2  # 먼저 들러야 하는 샵까지 가는 비용 + 이후에 들러야 하는 샵으로 돌아오는 비용
        cur_loc = src  # 현재 위치 이동

    answer += n_city + 1 - cur_loc  # 출구로 나가는 비용

    print(answer)
