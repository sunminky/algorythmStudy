lst = [i*i for i in range(10)]  #0~9까지 제곱을 리스트에 담아서 반환
print(lst)

lst = [(i,j,i*j) for i in range(5) for j in range(5) if i%2 != 1 and j%2!=1]  #0~4까지 짝수들의 쌍을 튜플에 담아서 반환
print(lst)

#제너레이터
(i for i in range(10))  #호출할때 계산해서 결과 반환
