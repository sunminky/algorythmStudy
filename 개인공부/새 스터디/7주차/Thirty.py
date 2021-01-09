#https://www.acmicpc.net/problem/10610

import sys

if __name__ == '__main__':
    num = sys.stdin.readline().rstrip()
    sorted_num = sorted(map(int, num), reverse=True)

    if sum(sorted_num) % 3 or 0 not in sorted_num:
        print(-1)
    else:
        print("".join(map(str, sorted_num)))