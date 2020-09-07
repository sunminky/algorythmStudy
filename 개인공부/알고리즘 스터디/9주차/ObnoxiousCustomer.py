#https://programmers.co.kr/learn/courses/30/lessons/64064

import re
from itertools import product

def solution(user_id, banned_id):
    ban_probability = []
    
    for obnoxious in banned_id:
        ret = matching(user_id, obnoxious)
        ban_probability.append(ret)    #아이디 체크

    answer = list(product(*ban_probability))    #매칭되는 아이디의 모든 조합의 수를 구함
    answer2 = []

    for i in answer:
        setv = set(i)   #중복되는 아이디 제거
        if len(setv) == len(banned_id): #조합했을때 중복이 있으면 정규표현식의 개수만큼의 원소가 없을 것
            if not setv in answer2: #이미 조합이 존재하는 경우가 아니라면
                answer2.append(setv)
    
    return len(answer2)

def matching(user_id, obnoxious):
    result = []
    obnoxious = obnoxious.replace("*", ".") #정규표현식 .은 한글자에 대응함
    for user in user_id:
        ret = re.fullmatch(obnoxious, user) #정규표현식에 맞는 사용자 찾기
        if ret:
            result.append(ret.group())  #정규표현식에 맞는 사용자 추가

    return result


if __name__ == '__main__':
    solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])
    print("-------------------")
    solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]	)