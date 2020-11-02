#https://programmers.co.kr/learn/courses/30/lessons/12939?language=python3
def solution(s):
    lst = list(map(int,s.split()))
    lst.sort()
    return "{} {}".format(lst[0], lst[-1])