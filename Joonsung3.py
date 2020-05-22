import turtle
import random

## 전역 변수 선언 부분 ##
swidth, sheight, pSize = 300, 300, 3
r, g, b, dist = [0] * 4
colors = ["red","orange","yellow","green","blue","navyblue","purple"]

## 메인 코드 부분 ##
turtle.title('거북이가 소라 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)
turtle.setup(width=swidth + 30, height=sheight + 30)
turtle.screensize(swidth, sheight)

dist = 5
#for로 하기
for i in range(1,80):
    # 색깔 순서대로 그림그리기
    turtle.pencolor(colors[(i-1) % len(colors)]);   #빨주노초파남보 순서대로 색깔 선택

    #무작위 샊깔로 그림 그리기
    '''turtle.pencolor(colors[random.randrange(6)]);   #빨주노초파남보 중 무작위로 색깔 선택'''

    turtle.forward(dist)
    turtle.left(30)
    dist += 1
