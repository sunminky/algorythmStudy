# https://www.acmicpc.net/problem/17827

import sys

if __name__ == '__main__':
    n_node, n_query, final_dst = map(int, sys.stdin.readline().split())
    nodes = [*map(int, sys.stdin.readline().split())]
    tail = n_node - final_dst + 1
    head = n_node - tail

    for _ in range(n_query):
        nth_node = int(sys.stdin.readline())

        if nth_node < head:
            print(nodes[nth_node])
        else:
            print(nodes[(nth_node - head) % tail + head])
