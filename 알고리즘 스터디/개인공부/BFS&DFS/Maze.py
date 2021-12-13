# https://programmers.co.kr/learn/courses/30/lessons/81304
from queue import PriorityQueue


def solution(n, start, end, roads, traps):
    queue = PriorityQueue()
    trap_dict = dict(zip(traps, range(len(traps))))
    table = [[-1] * n for _ in range(n)]
    visited = [[False] * (2 ** len(traps)) for _ in range(n)]

    for row in range(n):
        table[row][row] = 0

    for _src, _dst, _cost in roads:
        if table[_src - 1][_dst - 1] == -1:
            table[_src - 1][_dst - 1] = _cost
        table[_src - 1][_dst - 1] = min(table[_src - 1][_dst - 1], _cost)

    queue.put((0, start - 1, 0))  # 비용, 노드, 방문여부
    while not queue.empty():
        cur_cost, cur_node, visited_bit = queue.get()

        visited[cur_node][visited_bit] = True

        if cur_node + 1 in trap_dict.keys():
            visited_bit = visited_bit ^ (1 << trap_dict[cur_node + 1])

        # 목적지에 도착한 경우
        if cur_node == end - 1:
            return cur_cost

        # 정방향
        for col in range(n):
            if table[cur_node][col] == -1:
                continue
            if col == cur_node:
                continue
            if visited[col][visited_bit]:
                continue
            if cur_node + 1 in trap_dict.keys() and col + 1 in trap_dict.keys():
                if bool(visited_bit & (1 << trap_dict[cur_node + 1])) ^ bool(visited_bit & (1 << trap_dict[col + 1])):
                    continue
                queue.put((cur_cost + table[cur_node][col], col, visited_bit))
            elif bool(cur_node + 1 in trap_dict.keys()) ^ bool(col + 1 in trap_dict.keys()):
                c1 = False if not bool(cur_node + 1 in trap_dict.keys()) else bool(
                    visited_bit & (1 << trap_dict[cur_node + 1]))
                c2 = False if not bool(col + 1 in trap_dict.keys()) else bool(visited_bit & (1 << trap_dict[col + 1]))

                if c1 or c2:
                    continue
                queue.put((cur_cost + table[cur_node][col], col, visited_bit))
            else:
                queue.put((cur_cost + table[cur_node][col], col, visited_bit))

        # 역방향
        for row in range(n):
            if table[row][cur_node] == -1:
                continue
            if row == cur_node:
                continue
            if visited[row][visited_bit]:
                continue
            if cur_node + 1 in trap_dict.keys() and row + 1 in trap_dict.keys():
                if bool(visited_bit & (1 << trap_dict[cur_node + 1])) ^ bool(visited_bit & (1 << trap_dict[row + 1])):
                    queue.put((cur_cost + table[row][cur_node], row, visited_bit))
            elif bool(cur_node + 1 in trap_dict.keys()) ^ bool(row + 1 in trap_dict.keys()):
                c1 = True if not bool(cur_node + 1 in trap_dict.keys()) else bool(
                    visited_bit & (1 << trap_dict[cur_node + 1]))
                c2 = True if not bool(row + 1 in trap_dict.keys()) else bool(visited_bit & (1 << trap_dict[row + 1]))

                if c1 and c2:
                    queue.put((cur_cost + table[row][cur_node], row, visited_bit))


if __name__ == '__main__':
    solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2])  # 5
    solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3])  # 4
    solution(4, 2, 3, [[2, 1, 1], [3, 1, 100], [4, 3, 1], [4, 1, 1]], [1, 3, 4])  # 5
    solution(4, 2, 3, [[2, 1, 1], [3, 1, 100], [4, 2, 1], [4, 3, 1], [4, 1, 1], [2, 4, 2]], [1, 3, 4])  # 5
