#https://www.acmicpc.net/problem/1135

import sys

class node:
    def __init__(self):
        self.under = [] #후임
        self.time = -1   #최적의 전파시간

def search(staff : node):   #하향식 접근법
    global boss
    if not staff.under: #후임이 없음, 쫄따구임
        staff.time = 0
        return staff.time
    else:
        #자기 부하들중 가장 전파시간이 오래걸리는 놈을 찾음
        lst = [search(boss[u]) for u in staff.under]    #부하들의 전파시간을 저장
        lst.sort(reverse=True)
        staff.time = max([lst[x] + 1 + x for x in range(len(lst))])
        return staff.time

if __name__ == '__main__':
    global boss
    n_staff = int(sys.stdin.readline())    #직원 수
    boss = [node() for _ in range(n_staff)]
    structure = tuple(map(int, sys.stdin.readline().split()))

    #트리 만들기
    for i in range(1, len(structure)):
        boss[structure[i]].under.append(i)

    search(boss[0])

    print(boss[0].time)