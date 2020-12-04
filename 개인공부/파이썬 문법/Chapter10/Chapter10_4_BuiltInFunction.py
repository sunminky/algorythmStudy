#map 내장함수
result = map(lambda x: x*x, (1, 2, 3))
print(list(result))

result = map(lambda x, y: x+y, [1, 3], [2, 4])
print(list(result))

#filter 내장함수
f = filter(lambda x:x>2, [1, 2, 3, 4])  #2이상인 원소만 골라냄
print(list(f))

f = filter(None, [0, 1, True, False, "", "String!"])    #첫번째 인수가 None이면 객체의 입력값이 True인 경우만 골라냄
print(list(f))