class MyClass:
    __slots__ = ["vvs"]    #이곳에 정의한 이름 이외에는 속성을 만들 수 없음
    value = 10
    def __add__(self, other):   #덧셈 연산자 중복
        return self.value + other

    def __sub__(self, other):   #뺄셈 연산자 중복
        return self.value - other
    
    def __del__(self):  #클래스가 삭제될 때 호출 됨
        print("소멸자 호출")

myclass = MyClass()
print(myclass + 10) #10 + 10 = 20
print(myclass - 10) #10 - 10 = 0

#myclass.freak = 11 #에러!!, __slots__안에 정의된 속성이 아님
myclass.vvs = 11    #slots__안에 정의된 속성이라 문제없음
print(myclass.vvs)  #11
del myclass