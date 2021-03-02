#https://www.acmicpc.net/problem/11505

import sys
from math import ceil
from math import log2

tree = None
end_layer_width = None

def change(operand, target):
    end_layer = (end_layer_width + operand - 1) >> 1
    tree[end_layer_width + operand - 1] = target

    while end_layer != 0:
        tree[end_layer] = (tree[end_layer << 1] % 1000000007) * (tree[(end_layer << 1) + 1] % 1000000007)
        end_layer >>= 1

def search(src, dst, portion_start, portion_end, nth_node):
    global tree
    
    #구간에 속하지 않는 경우
    if src > portion_end or dst < portion_start:
        return 1
    #구간에 완전히 속하는 경우
    elif src <= portion_start and portion_end <= dst:
        return tree[nth_node] % 1000000007
    #구간의 경계에 걸쳐진 경우
    middle = (portion_start + portion_end) // 2
    return (search(src, dst, portion_start, middle, nth_node << 1) * search(src, dst, middle+1, portion_end, (nth_node << 1) + 1)) % 1000000007

def inflateTree(n_number):
    global tree
    global end_layer_width
    number = [int(sys.stdin.readline()) for _ in range(n_number)]
    height = ceil(log2(n_number))
    tree = [1 for i in range(2 << height)]
    end_layer_width = end_layer = 1 << height

    for i in range(len(number)):
        tree[end_layer + i] = number[i]

    end_layer >>= 1
    while end_layer != 0:
        for i in range(end_layer):
            tree[end_layer + i] = (tree[(end_layer+i) << 1] % 1000000007) * (tree[((end_layer+i) << 1) + 1] % 1000000007)
        end_layer >>= 1


if __name__ == '__main__':
    n_number, n_change, n_query = tuple(map(int, sys.stdin.readline().split()))
    inflateTree(n_number)

    for _ in range(n_change + n_query):
        op_code, src, dst = tuple(map(int, sys.stdin.readline().split()))
        if op_code == 1:
            change(src, dst)
        else:
            print(search(src, dst, 1, end_layer_width, 1))
