### 집합은 슬라이싱 인덱싱 정렬 지원 안함, 예외적으로 for문에서는 사용가능 ###
a = set()   #빈 집합 생성
a1 = {}     #집합이 아니라 딕셔너리가 생성됨
print(type(a) == type(a1))  #set != dictionary
b = {1,2,3} #중괄호를 이용한 집합생성

########## 반복 가능한 객체로부터 집합만들기 ##########
set((1,2,3))    #튜플로부터 집합 만듬
set('abcd')     #문자열로부터 집합 만듬
set([1,2,3])    #리스트로부터 집합 만듬
set((1,1,1,2,3))    #중복된 숫자는 한번만 나타남
set({'one':1,'two':2})  #딕셔너리는 키 값을 반환
{x for x in [1,2,3,4]}  #리스트컴프리헨션으로 집합만들기

#set([1,2,3],[1,2,3,4])  #에러, 변경불가능하면서 해쉬가능한 자료형만 객체의 원소로 사용 가능

c = {1,2,3}
c.add(4)    #한 원소 추가, {1,2,3,4}
c.update([4,5,6])   #c와 [4,5,6]의 합집합, {1,2,3,4,5,6}
c.update([4,5,6],[6,7,8])   #여러개도 가능, {1,2,3,4,5,6,7,8}
c.discard(8)    #원소 한 개 삭제, 해당 원소가 없으면 그냥 통과
c.remove(7)     #원소 한 개 삭제, 해당 원소가 없으면 에러
c.pop()         #원소 한 개를 반환하면서 제거
c.clear()       #모든 원소 삭제

A = {1,2,3}
B = {3,4,5}
C = {1,3,5,7}

A.union(B)  #합집함, {1,2,3,4,5}
#A.update(B) #합집합 결과를 반영
A.intersection(B)   #교집합, {3}
A.intersection(B,C) #인수가 2개인 교집합, {3}
#A.intersection_update(B)    #교집합 결과를 반영
A.difference(B) #차집합, {1,2}
#A.difference_update(B)  #차집합 결과를 반영
A.symmetric_difference(B)   #대칭 차집합, {1,2,4,5}
#A.symmetric_difference_update(B) #대칭 차집합 결과를 반영

A.issuperset(B) #B ⊂ A
A.issubset(B)   #A ⊂ B
A.isdisjoint(B) #교집합의 공집한인가??