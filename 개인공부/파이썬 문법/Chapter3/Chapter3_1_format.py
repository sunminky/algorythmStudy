print(format(10,'3d'),"-----",format(1.123,'5.2f'))     #10을 3자리로 표현, 소수점 2째 자리까지 표현
print(format(10000000000,',d'))         #1000단위마다 쉼표찍어줌

print("{0:3d} ----- {1:5.2f}".format(10,1.123))  #위의 문장과 동일, 0번째 인자를 3자리로 표현, 1번째 인자를 소수점 2깨 자리까지 표현
print("리스트 표현{0[1]} and {0[2]}".format([0,1,2]))    #매개변수로 리스트가 들어오면 인덱스로 접근가능
print("이름으로 접근{name} and {age}".format(name="Myname",age=123))  #매개변수를 이름으로 접근하기
print("딕셔너리 접근하기 {name} and {age}".format_map({"name":"Myname","age":123})) #딕셔너리는 format_map 써서 접근해야 함

import sys
print("{0.version}".format(sys))    #0번째 인수로 sys를 줌, 그냥 치환시켜버리는 듯
print(sys.version)  #위의 문장과 동일

print("10진수 : {0:d}\n2진수 : {0:b}\n8진수 : {0:o}\n16진수 : {0:x}\n10진수(현재 로캘적용) : {0:n}".format(15))
print("부동소수점 : {0:e}\n 고정소수점 : {0:f}\n 적절한것 골라줌 : {0:g}\n 퍼센트 : {0:%}".format(1.2345))