#https://programmers.co.kr/learn/courses/30/lessons/12939?language=python3
def solution(s):
    return str(min(list(map(int,s.split())))) + " " + str(max(list(map(int,s.split()))))