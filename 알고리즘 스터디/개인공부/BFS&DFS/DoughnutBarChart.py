# https://school.programmers.co.kr/learn/courses/30/lessons/258711
from collections import deque


def find_root(path, reverse_path):
    for _rpath in reverse_path:
        if len(reverse_path[_rpath]) == 0 and len(path[_rpath]) > 1:
            return _rpath

    return None


def classify(node, path, reverse_path, visited) -> int:
    # 도넛 : 1, 막대 : 2, 8자 : 3
    queue = deque([node])
    vortex_cnt = 0
    edge_cnt = -1  # root노드에서 들어온 간선 개수 빼줌

    visited[node] = True

    while queue:
        cur_node = queue.popleft()

        vortex_cnt += 1
        edge_cnt += len(path[cur_node]) + len(reverse_path[cur_node])

        for _neigh in path[cur_node]:
            if visited[_neigh]:
                continue
            queue.append(_neigh)
            visited[_neigh] = True

        for _neigh in reverse_path[cur_node]:
            if visited[_neigh]:
                continue
            queue.append(_neigh)
            visited[_neigh] = True

    if vortex_cnt + 1 == edge_cnt // 2:
        return 3

    if vortex_cnt == edge_cnt // 2:
        return 1

    if vortex_cnt - 1 == edge_cnt // 2:
        return 2


def solution(edges):
    answer = [0, 0, 0, 0]
    path = {}
    reverse_path = {}
    visited = {}

    for _src, _dst in edges:
        if _src not in path:
            path[_src] = []

        if _dst not in path:
            path[_dst] = []

        if _src not in reverse_path:
            reverse_path[_src] = []

        if _dst not in reverse_path:
            reverse_path[_dst] = []

        if _src not in visited:
            visited[_src] = True

        if _dst not in visited:
            visited[_dst] = True

        path[_src].append(_dst)
        reverse_path[_dst].append(_src)
        visited[_src] = visited[_dst] = False

    root_node = find_root(path, reverse_path)
    visited[root_node] = True
    answer[0] = root_node

    for _neigh in path[root_node]:
        answer[classify(_neigh, path, reverse_path, visited)] += 1

    return answer


if __name__ == '__main__':
    solution([[2, 3], [4, 3], [1, 1], [2, 1]])  # [2, 1, 1, 0]
    solution(
        [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3],
         [11, 9], [3, 8]])  # [4, 0, 1, 2]
