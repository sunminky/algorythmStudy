# https://www.acmicpc.net/problem/16566
import sys
from bisect import bisect_right


def union_find(idx, next_edge, vacancy, cards) -> int:
    if vacancy[idx]:
        next_edge[idx] = next_edge[idx + 1]
        vacancy[idx] = False
        print(cards[idx])

        return next_edge[idx]

    next_edge[idx] = union_find(next_edge[idx], next_edge, vacancy, cards)

    return next_edge[idx]


if __name__ == '__main__':
    _, n_picked, n_turn = map(int, sys.stdin.readline().split())
    cards = sorted(list(map(int, sys.stdin.readline().split())))
    vacancy = [True] * n_picked
    next_edge = list(range(n_picked + 1))

    for e in tuple(map(int, sys.stdin.readline().split())):
        bin_idx = bisect_right(cards, e)
        uni_idx = union_find(bin_idx, next_edge, vacancy, cards)
        next_edge[bin_idx] = uni_idx
