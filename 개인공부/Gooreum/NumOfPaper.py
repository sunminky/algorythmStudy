#https://www.acmicpc.net/problem/1780
contents = []
count = [0, 0, 0]

def divide(x,y,unit):
    for i in range(3):  #9구역으로 쪼개서 체크
        for j in range(3):
            checkPaper(x + unit * i, y + unit * j, unit)

def checkPaper(x,y,unit):   #시작좌표 x, 시작좌표 y, 변의 길이 unit
    head = contents[x][y]

    for i in range(unit):
        for j in range(unit):
            if head != contents[x + i][y + j]:
                divide(x,y,unit//3) #한번에 쓸수 없는 종이였다, 9개로 쪼개서 확인해라
                return
    count[head + 1] += 1    #값이 -1인 원소 때문에 인덱스 오류나서 1더함

if __name__ == '__main__':
    size = int(input())
    for i in range(size):
        contents.append(list(map(int,input().split())))

    checkPaper(0,0,size)

    for e in count:
        print(e)