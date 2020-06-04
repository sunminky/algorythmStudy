from turtle import *


class MyTurtle(Turtle): #Turtle을 상속 받는다
    def __init__(self, color, shape, x, y):
        self.item = Turtle()
        self.item.shape(shape)      #거북이 모양 지정
        self.item.fillcolor(color)  #거북이를 색칠함
        self.item.pencolor(color)   #펜 색깔 지정

        ###거북이 초기 위치 지정###
        self.item.penup()   
        self.item.goto(x,y) #거북이를 (x,y)에 놓는다
        self.item.pendown()
        ##########################
        
        self.item.speed(10) #거북이 속도 설정
        self.direct = abs(y) / y    #y의 부호를 구함
        
        if y < 0:   #y좌표가 음수이면
            self.item.right(180)    #머리가 왼쪽을 향하게 함

    def move(self):
        self.item.forward(50)
        self.item.left(90 * self.direct)    #머리가 왼쪽을 향한다면 오른쪽으로 이동
        self.item.forward(10)
        self.item.right(90 * self.direct)   #머리가 왼쪽을 향한다면 왼쪽으로 이동
        self.item.forward(50)


if __name__ == '__main__': 
    tt1 = MyTurtle('red', 'turtle', 0, -50) #거북이를 빨간색으로 설정하고 (0,-50) 좌표에 놓는다
    tt1.move()  #빨간색 거북이를 움직이게 함
    tt2 = MyTurtle('blue', 'circle', 0, 50) #거북이를 파란색으로 설정하고 (0,50) 좌표에 놓는다
    tt2.move()  #파란색 거북이를 움직이게 함

    done()  #거북이가 다 움직여도 창이 닫히지 않게 함
