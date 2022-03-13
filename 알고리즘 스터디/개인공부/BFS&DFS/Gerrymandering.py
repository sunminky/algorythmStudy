# https://www.acmicpc.net/problem/17471
import sys
from collections import deque

n_city = int(sys.stdin.readline())
costs = tuple(map(int, sys.stdin.readline().split()))
neighbor = []
answer = sum(costs)

for _ in range(n_city):
    _, *neigh = map(lambda x: int(x) - 1, sys.stdin.readline().split())
    neighbor.append(neigh)


def tracking(bitmask, flag) -> tuple:
    grp = set()
    grp_sum = 0
    visited = set()
    queue = deque()

    for i in range(n_city):
        if bitmask & (1 << i) == (flag << i):
            grp.add(i)

    if not grp:
        return 0, False

    tmp = tuple(grp)[0]
    queue.append(tmp)
    visited.add(tmp)
    grp_sum += costs[tmp]

    while queue:
        cur_node = queue.popleft()

        for _neigh in neighbor[cur_node]:
            if _neigh not in grp:
                continue
            if _neigh in visited:
                continue
            queue.append(_neigh)
            visited.add(_neigh)
            grp_sum += costs[_neigh]

    # print(f"{('00000000' + bin(bitmask)[2:])[-8:]}", flag, grp, visited)
    return grp_sum, len(grp) == len(visited)


def cases(bitmask, remain):
    if not remain:
        Agrp_sum, Asuccess = tracking(bitmask, 0)
        Bgrp_sum, Bsuccess = tracking(bitmask, 1)

        if Asuccess and Bsuccess:
            return abs(Agrp_sum - Bgrp_sum)

        return answer

    return min(cases(bitmask << 1 | 1, remain - 1), cases(bitmask << 1, remain - 1))


if __name__ == '__main__':
    answer = cases(0, n_city)

    if answer == sum(costs):
        print(-1)
    else:
        print(answer)
