#https://www.acmicpc.net/problem/11659

import sys
from math import log2
from math import ceil

tree = None


def inflateTree(numbers, height):
    global tree
    tree = [0 for _ in range(2 << height)]
    end_layer = (1 << height)

    for i in range(len(numbers)):
        tree[end_layer + i] = numbers[i]

    end_layer >>= 1
    while end_layer != 0:
        for i in range(end_layer):
            tree[end_layer + i] = tree[(end_layer + i) * 2 + 1] + tree[(end_layer + i) * 2]
        end_layer >>= 1


def search(src, dst, number_start, number_end, nth_node):   #원하는 구간시작, 원하는 구간끝, 트리의 구간처음, 트리의 구간끝, 노드번호
    global tree
    
    #구간을 벗어난 경우
    if src > number_end or dst < number_start:
        return 0
    #구간에 속하는 경우
    elif src <= number_start and number_end <= dst:
        return tree[nth_node]
    #구간의 경계에 걸쳐있는 경우
    middle = (number_start + number_end) // 2
    return search(src, dst, number_start, middle, nth_node << 1) + search(src, dst, middle+1, number_end, (nth_node << 1) + 1)


if __name__ == '__main__':
    n_number, n_query = tuple(map(int, sys.stdin.readline().split()))
    number = tuple(map(int, sys.stdin.readline().split()))
    ###세그먼트 트리 만들기###
    height = int(ceil(log2(n_number)))
    inflateTree(number, height)
    end_width = 1 << height
    ########################

    for _ in range(n_query):
        src, dst = tuple(map(int, sys.stdin.readline().split()))
        print(search(src, dst, 1, end_width, 1))