# https://www.acmicpc.net/problem/20366
import sys
from bisect import bisect_right

if __name__ == '__main__':
    n_snowball = int(sys.stdin.readline())
    snowballs = list(map(int, sys.stdin.readline().split()))
    snowman = []
    answer = 10000000000

    snowballs.sort()

    for i in range(n_snowball):
        for j in range(bisect_right(snowballs, snowballs[i] - 1) + 1, n_snowball):
            if i == j:
                continue
            snowman.append((snowballs[i] + snowballs[j], i, j))

    snowman.sort(key=lambda x: x[0])

    for _snowman, _ball1, _ball2 in snowman:
        start = 0
        end = n_snowball - 1

        while start < end:
            if start == _ball1 or start == _ball2:
                start += 1
                continue

            if end == _ball1 or end == _ball2:
                end -= 1
                continue

            height = snowballs[start] + snowballs[end]

            if height > _snowman:
                end -= 1
            else:
                start += 1

            answer = min(answer, abs(height - _snowman))

    print(answer)
