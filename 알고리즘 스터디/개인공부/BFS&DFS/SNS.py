# https://www.acmicpc.net/problem/2533

import sys
sys.setrecursionlimit(1000001)


n_node = int(sys.stdin.readline())
tree = [[] for _ in range(n_node)]
visited = [False] * n_node
early_cnt = n_node  # 얼리어댑터여야 하는 사람의 수


def searh(current_node) -> bool:
    global early_cnt

    visited[current_node] = True

    # 기저조건, 엔드 노드인 경우
    if len(tree[current_node]) == 1 and current_node != 0:
        early_cnt -= 1  # 현재 노드를 얼리어댑터에서 제외
        return False

    result = True   # 주변 친구중 얼리어댑터 아닌 사람이 한명이라도 있는 경우 False
    for neigh in tree[current_node]:
        if visited[neigh] is False:
            visited[neigh] = True
            result &= searh(neigh)

    # 모든 친구가 얼리어댑터인 경우
    if result:
        early_cnt -= 1  # 현재 노드를 얼리어댑터에서 제외
        return False

    return True


if __name__ == '__main__':
    for _ in range(n_node - 1):
        src, dst = map(int, sys.stdin.readline().split())

        tree[src - 1].append(dst - 1)
        tree[dst - 1].append(src - 1)

    visited[0] = True
    searh(0)

    print(early_cnt)
