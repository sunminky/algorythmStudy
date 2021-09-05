# https://www.acmicpc.net/problem/12920
import sys

if __name__ == '__main__':
    n_stock, limit = map(int, sys.stdin.readline().split())
    backpack = {0: 0}

    for _ in range(n_stock):
        _weight, _satisfaction, _cnt = map(int, sys.stdin.readline().split())
        package = 1

        while _cnt > 0:
            prev_backpack = backpack.copy()
            cur_package = min(package, _cnt)

            for weight, satisfaction in prev_backpack.items():
                if weight + cur_package * _weight > limit:
                    continue
                backpack[weight + cur_package * _weight] = max(backpack.get(weight + cur_package * _weight, 0),
                                                               cur_package * _satisfaction + satisfaction)

            _cnt -= cur_package
            package <<= 1

    print(max(backpack.values()))
