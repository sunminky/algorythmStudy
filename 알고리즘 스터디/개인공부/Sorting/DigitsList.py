# https://www.acmicpc.net/problem/5052
import sys

if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        digits = sorted((sys.stdin.readline().rstrip() for _ in range(int(sys.stdin.readline()))),
                        key=lambda x: (len(x), x))
        emergence = set()
        fail = False

        for e in digits:
            for idx in range(len(e)):
                if e[:idx + 1] in emergence:
                    fail = True
                    break

            if fail:
                print("NO")
                break

            emergence.add(e)
        else:
            print("YES")
