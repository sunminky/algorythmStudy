t = ()  #빈 튜플 생성
t = (1,2,3) #튜플 생성
t = 1,2,3   #위와 동일

t = (1,)    #데이터가 하나인 튜플 생성 t=1, 과는 다름

#튜플을 이용해서 변수값 스위치
x,y,z = 1,2,3
(x1,y2),(x2,y2) = (1,2),(3,4)

#패킹, 한 데이터에 여러 개의 데이터를 넣음
t = 1, 2, 'hello'

#언패킹, 한 데이터에서 데이터를 각각 꺼내옴
x,y,z = t

#확장된 언패킹
a, *b = (1,2,3,4)   #a에 1이 저장되고 b에 나머지가 저장됨
*b, a = (1,2,3,4)   #a에 4가 저장되고 b에 나머지가 저장됨

#이름 있는 튜플
from collections import namedtuple

Point = namedtuple('Point','x y')   #namedtuple을 이용해서 Point 클래스를 만듬

pt1 = Point(1,2)
pt2 = Point(10,20)
print(pt1)
print(pt2)
print("pt1.x + pt2.x : ",pt1.x + pt2.x, "\npt1.y + pt2.y : ",pt1.y + pt2.y)
