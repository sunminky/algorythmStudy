#https://www.acmicpc.net/problem/11651
lst = []
num = int(input())

for i in range(num):    #각 좌표(x,y)를 입력받음
    lst.append(input().split())
lst.sort(key = lambda x : (int(x[1]), int(x[0])))   #y에 대해 오름차순으로 정렬하다가, y가 같으면 x에 대해 오름차순으로 정렬

for i in lst:   #결과출력
    print(i[0],i[1])