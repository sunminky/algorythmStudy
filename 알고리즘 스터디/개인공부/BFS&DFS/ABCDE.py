# https://www.acmicpc.net/problem/13023
import sys
sys.setrecursionlimit(20001)


def dig(people, visited, cur_node, remain):
    # 깊이가 4 이상이 되면 종료
    if remain == 0:
        print(1)
        exit(0)

    visited[cur_node] = True
    for neighbor in people[cur_node]:
        if visited[neighbor] is False:
            dig(people, visited, neighbor, remain - 1)

    visited[cur_node] = False


if __name__ == '__main__':
    n_people, n_line = map(int, sys.stdin.readline().split())
    people = [list() for _ in range(n_people)]
    answer = 0

    for _ in range(n_line):
        src, dst = map(int, sys.stdin.readline().split())
        people[src].append(dst)
        people[dst].append(src)

    for node in range(n_people):
        dig(people, [False] * n_people, node, 4)

    print(0)
