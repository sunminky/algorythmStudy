#https://programmers.co.kr/learn/courses/30/lessons/12907

def solution(n, money):
    money.sort()    #동전의 종류를 순서대로 정렬
    cost = [0 for _ in range(n+1)] #각 동전들을 가지고 만들수 있는 경우의 수 저장

    for i in range(n+1):    #첫번째 동전 하나만 가지고 거슬러주는 경우
        if i % money[0] == 0:
            cost[i] = 1

    for i in range(len(money) - 1): #첫번째 동전 ~ i번째 동전을 가지고 거슬러주는 경우
        for j in range(n+1):
            # 새로 추가된 화폐단위보다 거슬러주는 금액이 적을때(새로 추가된 화폐단위 사용 못함)
            if j < money[1+i]:
                continue
            else:
                # 이전 동전들만 가지고 만드는 경우의 수 + (금액-새로추가된 화폐단위를 새로 추가된 화폐단위 가지고 거슬러주는 경우의 수)
                cost[j] = cost[j] + cost[j-money[1+i]]

    return cost[n]

if __name__ == '__main__':
    #print(solution(5,[1,2,5]))
    print(solution(6,[1,2,5]))
    #print(solution(1000, [1, 3, 5, 7, 10, 15, 20]))