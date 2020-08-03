#https://programmers.co.kr/learn/courses/30/lessons/12907

def solution(n, money):
    answer = recursive(n, money, 0)
    money.sort()
    return answer

# x + y + z ... 순으로 x <= y <= z이다
#재귀는 n/2 개만 탐색 할거임
def recursive(n, money, prev):
    answer = 0
    if n in money:  # 0 + n인 경우
        answer = answer + 1
    for i in money:    #n = x + y 일때 x <= n//2 까지 탐색할거임
        if i > n//2:
            break
        if prev > i:    # x + y + z ... 순으로 x <= y <= z이다
            continue
        answer = (answer + recursive(n-i, money, i)) % 1000000007
    return answer

if __name__ == '__main__':
    #print(solution(5,[1,2,5]))
    print(solution(6,[1,2,5]))
    #print(solution(1000, [5, 7, 10, 15, 20]))