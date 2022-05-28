# https://www.acmicpc.net/problem/2357
import sys

n_number, n_query = map(int, sys.stdin.readline().split())
nums = [int(sys.stdin.readline()) for _ in range(n_number)]
functions = {False: min, True: max}
init_value = {False: 1000000000, True: 0}


def forward_update(tree, nthnode, value, flag):
    while nthnode <= n_number:
        tree[nthnode] = functions[flag](tree[nthnode], value)
        nthnode += nthnode & -nthnode


def backward_update(tree, nthnode, value, flag):
    while nthnode:
        tree[nthnode] = functions[flag](tree[nthnode], value)
        nthnode -= nthnode & -nthnode


def query(forward_tree, backward_tree, start, end, flag):
    result = init_value[flag]

    cur = end - (end & -end)
    prev = end
    while cur >= start:
        result = functions[flag](result, forward_tree[prev])
        prev = cur
        cur -= cur & -cur

    cur = start + (start & -start)
    prev = start
    while cur <= end:
        result = functions[flag](result, backward_tree[prev])
        prev = cur
        cur += cur & -cur

    return functions[flag](result, nums[prev - 1])


if __name__ == '__main__':
    min_forward_tree = [1000000000] * (n_number + 1)
    min_backward_tree = [1000000000] * (n_number + 1)
    max_forward_tree = [0] * (n_number + 1)
    max_backward_tree = [0] * (n_number + 1)

    for seq, e in enumerate(nums):
        forward_update(min_forward_tree, seq + 1, e, False)
        backward_update(min_backward_tree, seq + 1, e, False)
        forward_update(max_forward_tree, seq + 1, e, True)
        backward_update(max_backward_tree, seq + 1, e, True)

    for _ in range(n_query):
        start, end = map(int, sys.stdin.readline().split())
        print(query(min_forward_tree, min_backward_tree, start, end, False),
              query(max_forward_tree, max_backward_tree, start, end, True))
