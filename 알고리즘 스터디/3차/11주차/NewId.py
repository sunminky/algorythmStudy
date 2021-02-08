#https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3

import re

def solution(new_id):
    #1단계
    answer = new_id.lower()
    #2단계
    answer = re.sub('[^a-z0-9-_.]', '', answer) #알파벳, 숫자, - , _ , .을 제외(^)하고는 모두 ''로 만듬
    #3단계
    answer = re.sub('[.]{1,}', '.', answer) #.이 1번이상 반복됬으면 .로 바꿈
    #4단계
    answer = re.sub('^[.]|[.]$',"", answer) #.으로 시작(^)하거나 .으로 끝나($)면 .을 제거
    #5단계
    if not answer:
        answer = "a"
    #6단계
    answer = answer[:15]
    answer = re.sub('^[.]|[.]$', "", answer)
    #7단계
    while len(answer) < 3:
        answer += answer[-1]
    return answer

if __name__ == '__main__':
    solution("...!@BaT#*..y.abcdefghijklm")