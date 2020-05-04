num = {'one':1,'two':2,'three':3}
num = dict(one = 1,two = 2,three = 3)
num = dict([('one',1),('two',2),('three',3)])
key = ['one','two','three']
value = (1,2,3)
num = dict(zip(key,value))
print(num['two'])   #원소에 키를 이용해 접근
### 키는 해시가능이고 변경불가능 해야함 ###

def func1():
    print("func1")

def func2():
    print("func2")

fdict = {'func1':func1,'func2':func2}   #함수를 딕셔너리에 넣을수도 있음

num.keys()  #딕셔너리의 키 받기
num.values()    #딕셔너리의 값 받기
num.items() #딕셔너리의 아이템 받기, (키,값)으로 받아짐

num.clear() #모든 항목 삭제
num.get('four',4)   #값이 존재하면 값을 반환, 없으면 4를 반환
num.setdefault('four',4)    #위와 동일, 키가 없으면 4로 세팅
num.update({'five':5,'six':6})  #키와 값 추가
num.popitem()   #아이템 반환하고 삭제
num.pop('five')  #키 반환하고 삭제, 키가 없으면 에러
num = num.fromkeys(['one','two','three','four','five'],[]) #새로 만든 사전을 반환
num['one'].append(1)    #fromkey로 만든 사전의 값의 수정은 전체에 영향을 미침

### 딕셔너리 컴프리헨션 ###
{w:1 for w in 'abc'} #{'a': 1, 'b': 1, 'c': 1}
{x:y for x,y in zip('abcd',(1,2,3,4))}  #{'a': 1, 'b': 2, 'c': 3, 'd': 4}
{w:k for k,w in [(1,'one'),(2,'two'),(3,'three')]}  #{'one': 1, 'two': 2, 'three': 3}
