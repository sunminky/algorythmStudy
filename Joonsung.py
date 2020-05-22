import turtle
import random

## 전역 변수 선언 부분 ##
swidth, sheight, pSize, exitCount = 300, 300, 3, 0
r, g, b, angle, dist, curX, curY = [0] * 7

cnt=0   #2번 문제를 위해 추가
seqColor = ('red', 'orange', 'yellow', 'green', 'blue', 'navyblue', 'purple')   #2번 문제를 위해 추가, 빨주노초파남보

## 메인 코드 부분 ##
turtle.title('거북이가 맘대로 다니기')
turtle.shape('turtle')
turtle.pensize(pSize)
turtle.setup(width=swidth + 30, height=sheight + 30)
turtle.screensize(swidth, sheight)

while True:
    #1번 문제
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor((r,g,b))

    #2번 문제
    turtle.pencolor(seqColor[cnt % len(seqColor)])  #seqColor에 0번째, 1번째, 2번째 ... 6번째 색깔 대입, cnt를 7(seqColor의 길이)로 나눈 나머지임
    cnt += 1

    angle = random.randrange(0, 360)
    dist = random.randrange(1, 100)
    turtle.left(angle)
    turtle.forward(dist)
    curX = turtle.xcor()
    curY = turtle.ycor()

    if (-swidth / 2 <= curX and curX <= swidth / 2) and (-sheight / 2 <= curY and curY <= sheight / 2):
        pass
    else:
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()

        exitCount += 1
        print("밖으로 {exitCount}번 나감".format(exitCount=exitCount))
        if exitCount >= 10: #밖으로 10번 나가면 종료
            break

    print("터틀의 모양 : {deg}도 회전".format(deg=angle))
    print("좌표 값 : ({x:.3f},{y:.3f})".format(x=curX,y=curY))

turtle.done()