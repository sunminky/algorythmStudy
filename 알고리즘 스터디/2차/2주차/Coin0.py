if __name__ =="__main__":
    inputData = input().split() #동전가지수  목표금액 입력받음
    coins = []  #여러가지 종류의 동전들을 저장할 리스트
    cnt = 0 #동전을 몇개 썼는지 세는데 사용

    coinvar = int(inputData[0]) #동전가지수
    goal = int(inputData[1])    #목표금액

    for i in range(coinvar):    #동전가지수만큼 동전 입력받음
        coins.append(int(input()))

    coins.sort(reverse=True)    #입력받은 동전을 크기가 큰 순서대로 정렬

    for i, coin in enumerate(coins):    
        cnt += goal // coin #현재 동전을 몇개만큼 사용해서 금액을 채웠는지
        goal = goal % coin  #남은 금액

    print(cnt)