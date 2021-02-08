a = 1.2
print(a.is_integer())  #a가 정수로 오차없이 표현가능한가?, False

a = 1.0
print(a.is_integer())  #a가 정수로 오차없이 표현가능한가?, True

import math as mm
print(mm.ceil(1.2))    #1.2보다 크거나 같은 정수
print(mm.floor(1.2))    #1.2보다 작거나 같은 정수

from fractions import Fraction  #분수형태의 연산을 가능하게 해주는 모듈
print(Fraction('5/7') * Fraction('14/15'))  # 5/7 * 14/15

from decimal import *   #실수를 오차없이 계산하게 해주는 모듈
temp = 0
for i in range(100):
    temp += Decimal('0.01')     #0.01을 100번더함
print(temp)
del temp

x = y  = 10
x1 = y1 = 11

print(x is y)   #x와 y가 같은 객체인지, True
print(x is y1)   #x와 y1가 같은 객체인지, False