import turtle
## 전역 변수 선언 부분 ##
swidth, sheight = 500, 500

## 메인 코드 부분 ##
turtle.title('무지개색 원그리기')
turtle.shape('turtle')
turtle.setup(width = swidth + 50, height = sheight + 50)
turtle.screensize(swidth, sheight)
turtle.penup()
turtle.goto(0, -sheight / 2)
turtle.pendown()
turtle.speed(10)

for radius in range(1, 250) :
    if (radius-1) % 7 == 0 :
        turtle.pencolor('red')
        color = "빨강"
    elif (radius-1) % 7 == 1 :
        turtle.pencolor('orange')
        color = "오렌지"
    elif (radius-1) % 7 == 2 :
        turtle.pencolor('yellow')
        color = "노랑"
    elif (radius-1) % 7 == 3 :
        turtle.pencolor('green')
        color = "초록"
    elif (radius-1) % 7 == 4 :
        turtle.pencolor('blue')
        color = "파랑"
    elif (radius-1) % 7 == 5 :
        turtle.pencolor('navyblue')
        color = "남"
    else :
        turtle.pencolor('purple')
        color = "보라"

    turtle.circle(radius)
    print("Radius : ",radius)
    print("Color :",color)

turtle.done()