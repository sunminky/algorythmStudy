#https://programmers.co.kr/learn/courses/30/lessons/64065
def solution(s):
    s = s.replace('{', "").replace('}', "") #"{"와 "}" 제거
    s = list(map(int, s.split(",")))    #,를 기준으로 숫자들 나눔
    diction = dict()    #숫자들이 나온 횟수를 저장할 딕셔너리

    for char in s:
        if diction.get(char, -1) == -1: #현재 숫자가 딕셔너리에 입력된 적이 없을 때
            diction[char] = 1   #출현횟수를 1로 설정
        else:
            diction[char] = diction[char] + 1   #출현횟수 1증가

    answer = [0 for _ in range(len(diction))]   #딕셔너리에 있는 키의 종류길이의 배열만듬

    for i in diction.keys():
        answer[len(diction) - diction[i]] = int(i)  #등장한 숫자가 클수록 앞에 가야함

    return answer

if __name__ == '__main__':
    solution("{{22,1},{22,1,3},{22,1,3,4},{22}}")