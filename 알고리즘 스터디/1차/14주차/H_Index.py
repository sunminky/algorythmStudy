def solution(citations):
    answer = 0
    citations.sort()
    citations.reverse()
    #인용된 횟수보다 논문이 더 많은 경우
    for i in range(len(citations)):
        #인용된 횟수(i+1) 비교
        if(citations[i] <= i):    #h번 이상 인용된 논문수가 h개 이상
            answer = i
            return answer
    return len(citations)

print(solution([22,42,20,19]))
print(solution([70,70,100,70,70,50,60,5,5,10,30,40,10]))