# https://www.acmicpc.net/problem/11812
import sys

if __name__ == '__main__':
    n_node, n_child, n_query = map(int, sys.stdin.readline().split())

    for _ in range(n_query):
        node1, node2 = map(int, sys.stdin.readline().split())
        distance = 0

        if n_child == 1:
            print(abs(node1 - node2))
            continue

        while node1 != node2:
            if node1 > node2:
                node1 = (node1 + n_child - 2) // n_child
            else:
                node2 = (node2 + n_child - 2) // n_child

            distance += 1

        print(distance)
