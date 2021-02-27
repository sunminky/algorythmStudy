#https://www.acmicpc.net/problem/2156

import sys

if __name__ == '__main__':
    cups = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
    stomach = [[0, 0, 0] for _ in range(len(cups))] #XXF, (TFT | FFT), FTT
    stomach[0] = [0, cups[0], cups[0]]

    for i in range(1, len(stomach)):
        stomach[i][0] = max(stomach[i-1])   #XXF
        stomach[i][1] = stomach[i-1][0] + cups[i]   #TFT | FFT
        stomach[i][2] = stomach[i-1][1] + cups[i]   #FTT

    print(max(stomach[-1]))