#https://www.acmicpc.net/problem/2798
inputData = list(map(int,input().split()))
num = inputData[0]  #전체 카드의 개수
goal = inputData[1] #목표 점수
total = []  #무슨무슨 카드를 뽑아야 하는지 저아
max = 0     #goal에 가장 가까운 점수중의 최대값 저장

cards = [x for x in map(int,input().split()) if x < goal]   #입력받은 카드의 수가 목표보다 크면 버림
cards.sort(reverse=True)    #내림차순으로 정렬

for i in range(num):    #1번째 카드 고름
    total.append(cards[i])  #1번째 카드 저장
    for j in range(i+1,len(cards)): #2번째 카드 고름
        if sum(total) + cards[j] > goal:    #2개밖에 안골랐는데 목표점수보다 크다
            continue                        #다음 카드(더 작은 숫자가 적힘) 고름
        else:
            total.append(cards[j])  #2번째 카드 저장
            for k in range(j+1,len(cards)): #3번째 카드 고름
                if sum(total) + cards[k] > goal:    #목표점수보다 크다
                    continue                        #다음 카드(더 작은 숫자가 적힘) 고름
                else:
                    total.append(cards[k])  #3번째 카드 저장
                    if max < sum(total):    #지금까지 고른 카드가 최대값이면 저장
                        max = sum(total)
                    total.remove(cards[k])  #3번째 카드 저장한것 지움
            total.remove(cards[j])  #2번째 카드 저장한것 지움
    total.remove(cards[i])  #1번째 카드 저장한것 지움
print(max)  #결과 출력


