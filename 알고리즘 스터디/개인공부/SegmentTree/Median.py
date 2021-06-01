# https://www.acmicpc.net/problem/1572
# https://www.acmicpc.net/problem/9426
import sys


class PenwikTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def update(self, nth_node, value):
        while nth_node < len(self.tree):
            self.tree[nth_node] += value
            nth_node += nth_node & -nth_node

    def search(self, nth_node):
        result = 0

        while nth_node > 0:
            result += self.tree[nth_node]
            nth_node -= nth_node & -nth_node

        return result


if __name__ == '__main__':
    n_number, width = map(int, sys.stdin.readline().split())
    numbers = tuple(int(sys.stdin.readline()) for _ in range(n_number))
    tree = PenwikTree(65536)
    answer = 0

    for i in range(width - 1):
        tree.update(numbers[i], 1)

    for i in range(n_number - width + 1):
        tree.update(numbers[i + width - 1], 1)
        # 이분 탐색 #
        start = 1
        end = 131072    # 65536 * 2
        while start < end:
            middle = (start + end) // 2

            if tree.search(middle) < (width + 1) // 2:
                start = middle + 1
            else:
                end = middle

        answer += end

        tree.update(numbers[i], -1)

    print(answer)
