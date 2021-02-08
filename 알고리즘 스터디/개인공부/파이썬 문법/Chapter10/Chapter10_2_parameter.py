# 가변 변수 리스트
def varg(a, *arg):  # 가변인수는 인수목록 맨 마지막에 하나만 나타남
    print(f"a : {a}")
    print(f"arg : {arg}")  # 가변 인수는 튜플형식으로 받아짐


varg(1, 2, 3, 4, 5)


def f(a, *arg, **kw):
    print(f"a : {a}")
    print(f"arg : {arg}")  # 가변 인수는 튜플형식으로 받아짐
    print(f"kw : {kw}")     #정의되지 않은 가변인수를 딕셔너리 형식으로 받음


f(1, 2, 3, 4, 5, t1=1, t2=2)


def h(a, b, c):
    print(f"a : {a}\nb : {b}\nc : {c}")


tuple_pack = (1, 2, 3)
h(*tuple_pack)  #튜플을 풀어서 매개변수에 하나씩 넣음

dic_pack = {'a': 1, 'b': 2, 'c': 3}
h(**dic_pack)   #딕셔너리를 풀어서 해당하는 매개변수의 이름에 넣음
