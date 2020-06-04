import math

class Circle:
    def __init__(self,radius):  #객체를 만들때 반지름을 입력받음
        self.radius = radius   

    def calcPerimeter(self):    #원의 길이를 구함
        return math.pi * 2 * self.radius
    
    def calcArea(self): #원의 넓이를 구함
        return math.pi * self.radius * self.radius

if __name__ == '__main__':
    circleVar = Circle(int(input("반지름 : ")))
    print("원의 면적 : {area:.2f}".format(area=circleVar.calcArea()))
    print("원의 둘레 : {area:.4f}".format(area=circleVar.calcPerimeter()))
