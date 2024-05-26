# https://school.programmers.co.kr/learn/courses/30/lessons/42861

import sys
import heapq


def get_parent(node, parent) -> int:
    if parent[node] == node:
        return parent[node]

    return get_parent(parent[node], parent)


def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]
    path = [dict() for _ in range(n)]
    queue = []

    for _src, _dst, _cost in costs:
        path[_src][_dst] = min(path[_src].get(_dst, sys.maxsize), _cost)
        path[_dst][_src] = min(path[_dst].get(_src, sys.maxsize), _cost)

        heapq.heappush(queue, (_cost, _src, _dst))

    while queue:
        _cost, _src, _dst = heapq.heappop(queue)

        p1, p2 = get_parent(_src, parent), get_parent(_dst, parent)

        # 부모노드 체크
        if p1 == p2:
            continue

        parent[p1] = parent[p2]

        answer += _cost

    return answer


if __name__ == '__main__':
    solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]])  # 4
