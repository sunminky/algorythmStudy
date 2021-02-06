#https://programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations  #중복제외 순열
#from itertools import permutations  #중복포함 순열

def solution(orders, course):

    dictionary = [dict() for _ in range(11)]
    maxValue = [-1 for _ in range(11)]
    answer = []

    for c in course:
        for o in orders:
            if len(o) >= c: #n개이상의 코스는 n개 이상의 주문을 한 사람한테서만 조사
                for s in combinations(sorted(o), c):    #오더가 항상 오름차순으로 오는것은 아님
                    combi = "".join(s)  #조합
                    if not dictionary[c].get(combi, False):
                        dictionary[c][combi] = 1
                    else:
                        dictionary[c][combi] += 1
                    if dictionary[c][combi] > maxValue[c]: #가장많이 주문된 코스 저장
                        maxValue[c] = dictionary[c][combi]

    for c in course:
        if maxValue[c] < 2: #가장 많이 시킨 코스가 2보다 작으면 패스
            continue
        for item in dictionary[c].keys():
            if maxValue[c] == dictionary[c][item]:
                answer.append(item) #가장 많이 시킨 코스들 저장

    answer.sort()   #정렬
    return answer

if __name__ == '__main__':
    solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])
    solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5])
    solution(["XYZ", "XWY", "WXA"], [2,3,4])