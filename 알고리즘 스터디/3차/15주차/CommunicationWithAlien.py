# https://www.acmicpc.net/problem/1774
# 크루스칼


import sys
from math import sqrt
import itertools


# 최상위 부모 노드를 찾는 함수 
def get_root(node: int, root: list):
    if root[node] == node:
        return root[node]

    root[node] = get_root(root[node], root)
    return root[node]


if __name__ == '__main__':
    n_node, n_edge = tuple(map(int, sys.stdin.readline().split()))
    position = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n_node)]  # 신들의 위치 저장
    cost = [
        [
            [sqrt((position[i][0] - position[j][0]) ** 2 + (position[i][1] - position[j][1]) ** 2), i, j]
            for j in range(i + 1, n_node)
        ]
        for i in range(n_node)]  # 신 들의 거리 저장
    root = [i for i in range(n_node)]  # 루트노드 저장
    edge_cnt = n_node - 1  # 간선의 개수
    answer = 0

    for _ in range(n_edge):
        src, dst = tuple(map(int, sys.stdin.readline().split()))

        p1 = get_root(src - 1, root)  # src의 부모
        p2 = get_root(dst - 1, root)  # dst의 부모

        root[p1] = root[p2] = min(p1, p2)  # 더 작은 부모값으로 갱신

        cost[min(src, dst) - 1][abs(src - dst) - 1][0] = 0  # 이미 연결된 노드는 0으로 만들어서 제일 먼저 선택되게 하고 비용에 추가되지 않게함

    cost = sorted(list(itertools.chain.from_iterable(cost)), key=lambda x: x[0])    #거리가 가까운 순으로 정렬

    # 제일 작은 간선부터 연결함
    for _cost, src, dst in cost:
        if edge_cnt == 0:
            break
        p1 = get_root(src, root)
        p2 = get_root(dst, root)

        # 사이클인 경우
        if p1 == p2:
            continue

        root[p1] = root[p2] = min(p1, p2)
        edge_cnt -= 1
        answer += _cost

    print(f"{answer:.2f}")
