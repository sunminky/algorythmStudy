# https://www.acmicpc.net/problem/6549
# https://www.acmicpc.net/problem/1725
# https://www.acmicpc.net/blog/view/12

import sys
from collections import deque

if __name__ == '__main__':
    while True:
        _, *blocks = map(int, sys.stdin.readline().split())
        queue = deque()
        answer = 0

        # 0이면 종료
        if not blocks:
            break

        for i in range(len(blocks)):
            # 새로 들어오는 블럭이 더 작은 경우
            while queue and blocks[queue[-1]] > blocks[i]:
                height = blocks[queue.pop()]
                #큐가 비어있는 경우는 자기자신
                if not queue:
                    answer = max(answer, height * i)
                else:
                    answer = max(answer, height * (i - queue[-1] - 1))
            queue.append(i)

        while queue:
            seq = queue.pop()
            height = blocks[seq]

            # (끝 ~ 현재 위치) * 현재 높이
            if queue:
                answer = max(answer, height * (len(blocks) - queue[-1] - 1))
            else:
                answer = max(answer, height * len(blocks))

        print(answer)
