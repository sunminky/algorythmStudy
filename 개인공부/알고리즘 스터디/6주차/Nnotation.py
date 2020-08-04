#https://programmers.co.kr/learn/courses/30/lessons/42895
#dp로 풀어야 하는데 무작위탐색으로 품

def solution(N, number):
    store = [{N}]
    if number in store[0]:
        return 1

    for i in range(2, 9):
        temp = {int("".join(map(str, [N for _ in range(i)])))}

        for j in range(i//2):  # 3개 사용 = 1개사용 (+, - , /, *) 2개 사용
            for n1 in store[j]:
                for n2 in store[i-j-2]:
                    temp.add(n1 + n2)
                    temp.add(n1 - n2)
                    if not n2 == 0:
                        temp.add(n1 // n2)
                    temp.add(n1 * n2)
                    # temp.add(n2 + n1) #n1 + n2 == n2 + n1 계산이 중복됨
                    temp.add(n2 - n1)
                    if not n1 == 0:
                        temp.add(n2 // n1)
                    # temp.add(n2 * n1) #n1 * n2 == n2 * n1 계산이 중복됨
                    
        if number in temp:  #이번 턴에 구한 값 중 타겟이 있을 경우
            return i
        store.append(temp)
        
    return -1

if __name__ == '__main__':
    #print(solution(5,12))
    print(solution(2, 11))
    print(solution(4,17))   #4*4 + 4/4 => 4
    #print(solution(9, 1111111111))