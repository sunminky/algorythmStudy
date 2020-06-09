import math

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def calcPerimeter(self):
        return math.pi * 2 * self.radius

    def calcArea(self):
        return math.pi * self.radius * self.radius

if __name__ == '__main__':
    circleVar = Circle(int(input("반지름 : ")))
    print("원의 면적 : {area:.2f}".format(area=circleVar.calcArea()))
    print("원의 둘레 : {area:.4f}".format(area=circleVar.calcPerimeter()))
