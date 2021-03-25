# https://www.acmicpc.net/problem/2374

import sys
from math import log2, ceil
sys.setrecursionlimit(10000)
numbers = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
tree = None


# 최대값 인덱스 저장트리
def inflate_tree():
    height = ceil(log2(len(numbers)))
    new_tree = [-1] * (2 << height)
    end_layer = 1 << height

    for i in range(len(numbers)):
        new_tree[end_layer + i] = i

    end_layer >>= 1
    while end_layer != 0:
        for i in range(end_layer):
            if new_tree[(end_layer + i) << 1] == -1:
                new_tree[end_layer + i] = new_tree[((end_layer + i) << 1) + 1]
            elif new_tree[((end_layer + i) << 1) + 1] == -1:
                new_tree[end_layer + i] = new_tree[(end_layer + i) << 1]
            else:
                if numbers[new_tree[(end_layer + i) << 1]] < numbers[new_tree[((end_layer + i) << 1) + 1]]:
                    new_tree[end_layer + i] = new_tree[((end_layer + i) << 1) + 1]
                else:
                    new_tree[end_layer + i] = new_tree[(end_layer + i) << 1]

        end_layer >>= 1

    return new_tree


def search(query_start, query_end, nth_node, portion_start, portion_end):
    # 구간에서 벗어난 경우
    if portion_end < query_start or query_end < portion_start:
        return -1
    # 구간에 속하는 경우
    if query_start <= portion_start and portion_end <= query_end:
        return tree[nth_node]
    # 경계에 걸쳐있는 경우
    middle = (portion_start + portion_end) // 2
    idx1 = search(query_start, query_end, nth_node << 1, portion_start, middle)
    idx2 = search(query_start, query_end, (nth_node << 1) + 1, middle+1, portion_end)

    if idx1 == -1:
        return idx2
    elif idx2 == -1:
        return idx1
    elif numbers[idx1] < numbers[idx2]:
        return idx2
    else:
        return idx1


def divide(start, end, target):
    answer = 0

    # 모든 구간의 값이 같으면 종료
    same_all = True
    for i in range(start, end+1):
        if numbers[start] != numbers[i]:
            same_all = False
    
    # 모든 구간의 값이 같으면 덧셈횟수 반환
    if same_all:
        return target - numbers[start]

    # 큰 수 기준으로 나누기
    idx_start = search(start+1, end+1, 1, 1, len(tree) >> 1)
    idx_end = idx_start
    for i in range(idx_start, end+1):
        if numbers[idx_start] != numbers[i]:
            break
        idx_end = i

    # 앞 나누기
    if start <= idx_start-1:
        answer += divide(start, idx_start-1, numbers[idx_start])
    # 뒤 나누기
    if idx_end + 1 <= end:
        answer += divide(idx_end+1, end, numbers[idx_start])

    return answer + target - numbers[idx_start]


if __name__ == '__main__':
    tree = inflate_tree()
    print(divide(0, len(numbers)-1, max(numbers)))
