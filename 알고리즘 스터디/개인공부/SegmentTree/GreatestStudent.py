# https://www.acmicpc.net/problem/2336
import sys
from math import ceil, log2


def infalte_tree(n_student):
    tree_height = ceil(log2(n_student))
    end_layer = 1 << tree_height

    return [500001] * (2 << tree_height), end_layer


def update(tree, nth_node, value):
    while nth_node:
        tree[nth_node] = min(tree[nth_node], value)
        nth_node >>= 1


def query(tree, query_start, query_end, portion_start, portion_end, nth_node):
    # 구간을 벗어나는 경우
    if query_start > portion_end or query_end < portion_start:
        return 500001
    # 구간에 속하는 경우
    if query_start <= portion_start and portion_end <= query_end:
        return tree[nth_node]
    # 구간에 걸치는 경우
    middle = (portion_start + portion_end) >> 1
    return min(
        query(tree, query_start, query_end, portion_start, middle, nth_node << 1),
        query(tree, query_start, query_end, middle + 1, portion_end, nth_node * 2 + 1)
    )


if __name__ == '__main__':
    n_student = int(sys.stdin.readline())
    grades = tuple(tuple(map(int, sys.stdin.readline().split())) for _ in range(3))
    criteria_dict = dict(zip(grades[0], range(n_student)))
    position_criteria = [0] * n_student
    grade_criteria = [0] * n_student
    tree, end_layer = infalte_tree(n_student)
    answer = 0

    for seq in range(n_student):
        position_criteria[criteria_dict[grades[1][seq]]] = seq + 1
        grade_criteria[criteria_dict[grades[2][seq]]] = seq + 1

    for student_seq in range(n_student):
        if position_criteria[student_seq] == 1 or grade_criteria[student_seq] == 1:
            answer += 1
        else:
            answer += query(tree, 1, position_criteria[student_seq] - 1, 1, end_layer, 1) > grade_criteria[student_seq]

        update(tree, end_layer + position_criteria[student_seq] - 1, grade_criteria[student_seq])

    print(answer)
