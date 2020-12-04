from functools import partial

#함수 클로저
def quadratic():
    sum = 0 #함수마다 독립적인 이름 공간 제공
    def add(x, y):
        nonlocal sum
        sum += x + y
        print(sum)
    return add


f1 = quadratic()
f1(1, 1)    #2
f1(10, 10)  #22, 함수에 변수가 저장되어 있음

f1 = quadratic()
f1(1, 1)    #2, 반환된 함수객체가 삭제되면 함수에 저장된 변수도 삭제됨

#partial함수, 기존 함수를 사용해서 일부 인수가 미리 정해진 새로운 함수를 반환
bin2int = partial(int, base = 2)
print(bin2int('1111'))  #15
