#https://www.acmicpc.net/problem/2902

import sys

if __name__ == '__main__':
    shortExpress = [word[0] for word in sys.stdin.readline().split('-')]
    print("".join(shortExpress))