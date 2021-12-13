# https://programmers.co.kr/learn/courses/30/lessons/86971
class node:
    def __init__(self):
        self.child_cnt = 1
        self.done = False


def dig(cur_node: int, nodes: list, path: list):
    nodes[cur_node].done = True

    for _neigh in path[cur_node]:
        if nodes[_neigh].done:
            continue
        nodes[cur_node].child_cnt += dig(_neigh, nodes, path)

    return nodes[cur_node].child_cnt


def solution(n, wires):
    answer = n
    nodes = [node() for _ in range(n)]
    path = [list() for _ in range(n)]

    for _src, _dst in wires:
        path[_src - 1].append(_dst - 1)
        path[_dst - 1].append(_src - 1)

    dig(0, nodes, path)

    for e in nodes:
        answer = min(answer, abs(n - e.child_cnt - e.child_cnt))

    return answer


if __name__ == '__main__':
    solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]])  # 3
    solution(4, [[1, 2], [2, 3], [3, 4]])  # 0
    solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]])  # 1
