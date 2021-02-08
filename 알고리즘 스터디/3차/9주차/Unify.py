#https://www.acmicpc.net/problem/10867
import sys

if __name__ == '__main__':
    sys.stdin.readline()
    nums = set(map(int, sys.stdin.readline().split()))
    for i in sorted(nums):
        print(i, end=" ")
    print()