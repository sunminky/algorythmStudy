# https://www.acmicpc.net/problem/5419
# 스위핑, 세그먼트 트리(x), 펜윅트리, 좌표압축
# lazy propagaion 사용해보기

import sys


# 펜위트리 생성
def inflate(cnt) -> list:
    return [0] * cnt    # 원소의 개수 + 1개 만큼의 트리 필요(인덱스가 1부터 시작하기 때문에)


def search(tree, nth_node):
    result = 0

    while nth_node > 0:
        result += tree[nth_node]
        nth_node -= nth_node & -nth_node

    return result


def update(tree, nth_node):
    while nth_node < len(tree):
        tree[nth_node] += 1
        nth_node += nth_node & -nth_node


# 좌표 압축
def compress() -> list:
    pos = sorted([[*map(int, sys.stdin.readline().split())] for _ in range(int(sys.stdin.readline()))],
                 key=lambda x: -x[1])    # y가 큰 순서대로 정렬

    # 좌표 압축
    seq = 0
    prev = -1000000001
    for i in range(len(pos)):
        if pos[i][1] != prev:
            seq += 1
            prev = pos[i][1]

        pos[i][1] = seq

    return pos, seq


if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        pos, y_len = compress()
        tree = inflate(y_len + 1)
        pos.sort(key=lambda x: (x[0], x[1]))    #x가 작은 순서대로 정렬, x가 같으면 y가 큰 순서대로 정렬
        answer = 0

        for p in pos:
            answer += search(tree, p[1])
            update(tree, p[1])

        print(answer)
