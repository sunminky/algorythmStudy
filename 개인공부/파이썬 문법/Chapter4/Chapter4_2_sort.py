lst = ['1','3','4','2','5']

lst.sort(reverse=True,key=int)  #역순으로 정렬하기, 각 요소는 key키워드로 전달된 함수를 통과후 전달
lst.sort(reverse=True,key=lambda a:int(a))  #위와 동일
print(lst)

#튜플 정렬하기
lst = [('one',1),('two',2),('three',3)]
sorted_lst = sorted(lst,key=lambda a:lst[1])    #sorted함수는 원본은 변경하지 않고 정렬한 리스트를 반환
print(sorted_lst)

#리스트를 역순으로 참조
for i in reversed(lst):     #sorted는 리스트를 역순으로 "참조"(제너레이터)해서 반환
    print(i)
