# https://www.acmicpc.net/problem/12865

import sys

if __name__ == '__main__':
    n_element, limit = map(int, sys.stdin.readline().split())
    cur_backpac = {0: 0}

    for _ in range(n_element):
        weight, value = map(int, sys.stdin.readline().split())

        prev_backpack = cur_backpac.copy()

        for _key, _value in prev_backpack.items():
            if _key + weight <= limit:
                cur_backpac[_key + weight] = max(cur_backpac.get(_key + weight, 0), value + _value)

    print(max(cur_backpac.values()))
