# https://www.acmicpc.net/problem/17822
import sys
from collections import deque


def check(disc, layer, seq) -> bool:
    # 값이 삭제된 경우
    if disc[layer][seq] is None:
        return False

    # 옆 체크
    if disc[layer][seq] == disc[layer][seq - 1]:
        return True
    if disc[layer][seq] == disc[layer][(seq + 1) % len(disc[layer])]:
        return True
    # 위 아래 체크
    if layer > 0 and disc[layer][seq] == disc[layer - 1][seq]:
        return True
    if layer + 1 < len(disc) and disc[layer][seq] == disc[layer + 1][seq]:
        return True

    return False


if __name__ == '__main__':
    n_disc, n_num, n_rotate = map(int, sys.stdin.readline().split())
    disc = [None] * n_disc
    delete_flag = False  # 삭제여부 체크
    delete_map = [[False] * n_num for _ in range(n_disc)]
    total = 0
    remain = n_disc * n_num

    for layer in range(n_disc):
        disc[layer] = deque(map(int, sys.stdin.readline().split()))
        total += sum(disc[layer])

    for _ in range(n_rotate):
        multiple, direction, n_drag = map(int, sys.stdin.readline().split())
        delete_flag = False

        # 원판 돌리기
        for layer in range(multiple, n_disc + 1, multiple):
            for _ in range(n_drag):
                # 시계 방향
                if direction == 0:
                    disc[layer - 1].appendleft(disc[layer - 1].pop())
                # 반시계 방향
                else:
                    disc[layer - 1].append(disc[layer - 1].popleft())

        # 체크하기
        for layer in range(n_disc):
            for seq in range(n_num):
                if check(disc, delete_map, layer, seq):
                    delete_flag = True
                    delete_map[layer][seq] = True

        # 바꾸기
        for layer in range(n_disc):
            for seq in range(n_num):
                if delete_map[layer][seq]:
                    total -= disc[layer][seq]
                    remain -= 1
                    disc[layer][seq] = None
                    delete_map[layer][seq] = False

        # 디스크 원소 증감하기
        if delete_flag is False and remain != 0:
            criteria = total / remain

            for layer in range(n_disc):
                for seq in range(n_num):
                    if disc[layer][seq] is not None:
                        if disc[layer][seq] > criteria:
                            disc[layer][seq] -= 1
                            total -= 1
                        elif disc[layer][seq] < criteria:
                            disc[layer][seq] += 1
                            total += 1

    print(total)
