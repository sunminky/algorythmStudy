# https://www.acmicpc.net/problem/1572
import sys
from math import log2, ceil
from bisect import bisect_left


def inflate_tree(numbers) -> list:
    height = ceil(log2(len(numbers)))
    end_layer = 1 << height
    tree = [list() for _ in range(2 << height)]

    for seq, e in enumerate(numbers):
        tree[end_layer + seq] = [e]

    end_layer >>= 1
    while end_layer:
        for i in range(end_layer):
            e1 = tree[(end_layer + i) << 1]
            e2 = tree[((end_layer + i) << 1) + 1]
            idx1 = 0
            idx2 = 0

            # 병합 정렬 #
            while idx1 < len(e1) and idx2 < len(e2):
                if e1[idx1] < e2[idx2]:
                    tree[end_layer + i].append(e1[idx1])
                    idx1 += 1
                else:
                    tree[end_layer + i].append(e2[idx2])
                    idx2 += 1

            # 남은 요소 합쳐주기 #
            for j in range(idx1, len(e1)):
                tree[end_layer + i].append(e1[j])

            # 남은 요소 합쳐주기 #
            for j in range(idx2, len(e2)):
                tree[end_layer + i].append(e2[j])

        end_layer >>= 1

    return tree


# 범위 내 리스트 요청
def query(tree, end_layer, start, end):
    result = []

    #bottom-up 방식
    start_idx = end_layer + start - 1
    end_idx = end_layer + end

    while start_idx < end_idx:
        if start_idx & 1:
            result.append(tree[start_idx])
            start_idx += 1

        if end_idx & 1:
            result.append(tree[end_idx - 1])
            end_idx -= 1

        start_idx >>= 1
        end_idx >>= 1

    return result


if __name__ == '__main__':
    n_number, width = map(int, sys.stdin.readline().split())
    numbers = tuple(int(sys.stdin.readline()) for _ in range(n_number))
    tree = inflate_tree(numbers)
    end_layer = 1 << ceil(log2(n_number))
    answer = 0

    for i in range(n_number - width + 1):
        result = query(tree, end_layer, i + 1, i + width)

        # 이분 탐색 #
        start = 1
        end = 65536 * 2
        while start < end:
            middle = (start + end) // 2

            if sum(bisect_left(res, middle) for res in result) < (width + 1) // 2:
                start = middle + 1
            else:
                end = middle

        answer += end - 1

    print(answer)
