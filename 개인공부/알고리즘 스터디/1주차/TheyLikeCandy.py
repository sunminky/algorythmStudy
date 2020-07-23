#https://www.acmicpc.net/problem/9550
num = int(input())  #테스트케이스 개수 입력받음
lst = []

for i in range(num):
    cnt = 0
    div = int(input().split()[1])   #사탕의 개수(버림), 한 사람당 먹어야하는 사탕개수 입력받음
    lst = (input().split())         #보유중인 사탕의 종류와 개수 입력받음
    for j in lst:   #전체 사탕 종류에 대해서
        cnt = cnt + int(j) // div   #사탕을 몇명에게 나눠줄수 있는지 계산
    print(cnt)