# https://www.acmicpc.net/problem/10868
import sys

n_number, n_query = map(int, sys.stdin.readline().split())
nums = [int(sys.stdin.readline()) for _ in range(n_number)]


def forward_update(tree, nthnode, value):
    while nthnode <= n_number:
        tree[nthnode] = min(tree[nthnode], value)
        nthnode += nthnode & -nthnode


def backward_update(tree, nthnode, value):
    while nthnode:
        tree[nthnode] = min(tree[nthnode], value)
        nthnode -= nthnode & -nthnode


def query(forward_tree, backward_tree, start, end):
    result = 1000000000

    cur = end - (end & -end)
    prev = end

    while cur >= start:
        result = min(result, forward_tree[prev])
        prev = cur
        cur -= cur & -cur

    cur = start + (start & -start)
    prev = start

    while cur <= end:
        result = min(result, backward_tree[prev])
        prev = cur
        cur += cur & -cur

    return min(result, nums[prev - 1])


if __name__ == '__main__':
    forward_tree = [1000000000] * (n_number + 1)
    backward_tree = [1000000000] * (n_number + 1)

    for seq, number in enumerate(nums):
        forward_update(forward_tree, seq + 1, number)
        backward_update(backward_tree, seq + 1, number)

    for _ in range(n_query):
        start, end = map(int, sys.stdin.readline().split())
        print(query(forward_tree, backward_tree, start, end))
