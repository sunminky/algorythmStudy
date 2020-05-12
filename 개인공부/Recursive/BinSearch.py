#https://level.goorm.io/exam/43064/binary-search/quiz/1
from pip._vendor.distlib.compat import raw_input

def binsearch(arr,goal,loc):
    if len(arr) == 1:
        if arr[0] == goal:
            print(loc+1)
        else:
            print('X')
        return

    if arr[len(arr)//2] <= goal:
        binsearch(arr[len(arr)//2:],goal,loc+len(arr)//2)
    elif arr[len(arr)//2] > goal:
        binsearch(arr[:len(arr)//2],goal,loc)

if __name__ == "__main__":
    input()
    lst = list(map(int,raw_input().split()))
    binsearch(lst,int(input()),0)