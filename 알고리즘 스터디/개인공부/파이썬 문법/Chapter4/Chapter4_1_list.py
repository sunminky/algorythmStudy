lst = [1,2,2,3,3,3]

lst.append(4)   #리스트의 맨 마지막에 4를 추가, 스택에서 push와 같은 역할
print(lst)

lst.insert(0,0) #0번째 자리에 0 추가
print(lst)

print(lst.index(2)) #2의 인덱스를 알아냄, 여러개면 제일 처음것 인덱스 반환

print(lst.count(4)) #4가 몇번나오는지 세어봄

lst.extend([4,4,4]) #리스트에 리스트를 추가
print(lst)

lst.pop()   #스택의 pop과 같은 역할, 맨마지막 요소 하나 읽고 삭제
print(lst)

lst.remove(4)   #리스트에서 4의 값을 가지는 요소 하나 삭제, 값이 여러개면 앞에서 부터 삭제
print(lst)

lst = [('one',1),('two',2),('three',3)]    #요소가 튜플인 경우

for i in lst:
    print("{:5}, {}".format(i[0],i[1])) #방법 1
    print("{0[0]:5}, {0[1]}".format(i))  # 방법 2

for name,age in lst:
    print("{:5}, {}".format(name,age))  # 방법 3