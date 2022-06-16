# https://www.acmicpc.net/problem/12920
import sys

if __name__ == '__main__':
    n_element, limit = map(int, sys.stdin.readline().split())
    elements = []
    knapsack = {0: 0}

    for _ in range(n_element):
        _weight, _happiness, _count = map(int, sys.stdin.readline().split())

        pow_count = 1

        while _count >= pow_count:
            elements.append((_weight * pow_count, _happiness * pow_count))
            _count -= pow_count
            pow_count <<= 1

        if _count:
            elements.append((_weight * _count, _happiness * _count))

    for e in elements:
        prev_knapsack = knapsack.copy()
        _weight, _happiness = e

        for key, value in prev_knapsack.items():
            if key + _weight > limit:
                continue
            knapsack[key + _weight] = max(value + _happiness, knapsack.get(key + _weight, 0))

    print(max(knapsack.values()))
