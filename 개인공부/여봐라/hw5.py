from turtle import *

class MyTurtle(Turtle):
    def draw(self,shape):
        tt = Turtle()

        ###거북이 초기 위치 지정###
        tt.penup()
        tt.goto(0, 0)  # 거북이를 (x,y)에 놓는다
        tt.pendown()
        ##########################

        for i in range(shape):
            tt.forward(50)
            tt.left(360/shape)

if __name__ == '__main__':
    mytt = MyTurtle()
    mytt.draw(4)
    done()
