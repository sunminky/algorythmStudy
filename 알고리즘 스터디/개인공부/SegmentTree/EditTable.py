# https://programmers.co.kr/learn/courses/30/lessons/81303
from math import ceil, log2


def inflate_tree(n_node) -> list:
    tree_height = ceil(log2(n_node))
    end_layer = 1 << tree_height
    tree = [1] * (2 << tree_height)

    end_layer >>= 1
    while end_layer:
        for i in range(end_layer):
            tree[end_layer + i] = tree[(end_layer + i) * 2] + tree[(end_layer + i) * 2 + 1]

        end_layer >>= 1

    return tree, 1 << tree_height


def update(tree, nth_node, value):
    while nth_node:
        tree[nth_node] += value
        nth_node >>= 1


def query(tree, query_start, query_end, portion_start, portion_end, nth_node):
    # 구간에 속하지 않는 경우
    if query_end < portion_start or query_start > portion_end:
        return 0
    # 구간에 속하는 경우
    if query_start <= portion_start and portion_end <= query_end:
        return tree[nth_node]
    # 구간에 걸쳐있는 경우
    middle = (portion_start + portion_end) // 2
    return query(tree, query_start, query_end, portion_start, middle, nth_node * 2) \
        + query(tree, query_start, query_end, middle + 1, portion_end, nth_node * 2 + 1)


def upper_bound(tree, start, end, target, end_layer) -> int:
    origin_start = start

    while start < end:
        middle = (start + end) // 2
        result = query(tree, origin_start, middle, 1, end_layer, 1)

        if result >= target:
            end = middle
        else:
            start = middle + 1

    return end - 1


def lower_bound(tree, start, end, target, end_layer) -> int:
    target = query(tree, 1, end, 1, end_layer, 1) - target

    while start < end:
        middle = (start + end) // 2
        result = query(tree, 1, middle, 1, end_layer, 1)

        if result > target:
            end = middle
        else:
            start = middle + 1

    return end - 1


def solution(n, k, cmd):
    cur_idx = k
    deleted = []
    tree, end_layer = inflate_tree(n)

    for _cmd in cmd:
        if _cmd[0] == "D":
            jump = int(_cmd.split()[1])
            cur_idx = upper_bound(tree, cur_idx + 2, n, jump, end_layer)

        elif _cmd[0] == "C":
            deleted.append(cur_idx)
            update(tree, end_layer + cur_idx, -1)

            # 밑으로 이동할 수 없음
            if query(tree, cur_idx + 1, n, 1, end_layer, 1) == 0:
                cur_idx = lower_bound(tree, 1, cur_idx, 1, end_layer)
            else:
                cur_idx = upper_bound(tree, cur_idx + 1, n, 1, end_layer)

        elif _cmd[0] == "U":
            jump = int(_cmd.split()[1])
            cur_idx = lower_bound(tree, 1, cur_idx, jump, end_layer)

        elif _cmd[0] == "Z":
            update(tree, deleted.pop() + end_layer, 1)

    return "".join(map(lambda x: "O" if x else "X", tree[end_layer:end_layer + n]))


if __name__ == '__main__':
    # print(solution(9, 3, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))  # OOOOXOOO
    solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"])  # OOXOXOOO
