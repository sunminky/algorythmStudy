#반지름 r이 주어졌을때 부피구하기

import math

if __name__ == '__main__':
    radius = 4  #구의 반지름
    volume = 4/3 * math.pi * radius**3   #구의 부피, V = 4/3 * pi * r**3
    volume = round(volume, 2)   #소수점 2째자리까지 반올림
    print("반지름 : {radius}\n부피 : {volume}".format(radius=radius, volume=volume))