# https://programmers.co.kr/learn/courses/30/lessons/67260?language=python3
from collections import deque


def solution(n_node, path, order):
    neigh = [set() for _ in range(n_node)]
    order_neigh = [set() for _ in range(n_node)]
    inbound = [0] * n_node
    nearby = [False] * n_node

    # 간선 입력
    for src, dst in path:
        neigh[src].add(dst)
        neigh[dst].add(src)

    # 방문 조건 추가
    for src, dst in order:
        order_neigh[src].add(dst)
        inbound[dst] += 1

    # 위상정렬
    topology_queue = deque()
    visited = [False] * n_node
    remain = n_node

    if inbound[0] == 0:
        topology_queue.append(0)
        visited[0] = True
        remain -= 1

    while topology_queue:
        cur_node = topology_queue.popleft()

        for _neigh in neigh[cur_node]:
            nearby[_neigh] = True

            # 이미 방문 했으면 생략
            if visited[_neigh]:
                continue

            if inbound[_neigh] == 0:
                topology_queue.append(_neigh)
                visited[_neigh] = True
                remain -= 1

        for _neigh in order_neigh[cur_node]:
            # 이미 방문 했으면 생략
            if visited[_neigh]:
                continue

            inbound[_neigh] -= 1

            if inbound[_neigh]:
                continue
            
            # 주변에 방문했던 노드가 있는 경우
            if nearby[_neigh]:
                topology_queue.append(_neigh)
                visited[_neigh] = True
                remain -= 1

    return remain == 0


if __name__ == '__main__':
    solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[8, 5], [6, 7], [4, 1]])  # true
    solution(9, [[8, 1], [0, 1], [1, 2], [0, 7], [4, 7], [0, 3], [7, 5], [3, 6]], [[4, 1], [5, 2]])  # true
    solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[4, 1], [8, 7], [6, 5]])  # false
    solution(10, [[0, 1], [0, 7], [1, 2], [2, 5], [3, 4], [3, 5], [4, 6], [5, 7], [6, 9], [7, 8]], [[2, 4], [9, 7]])    # True
    solution(10, [[0, 1], [0, 7], [1, 2], [2, 5], [3, 4], [3, 5], [4, 6], [5, 7], [6, 9], [7, 8]], [[2, 4], [8, 5], [9, 7]])    # False
