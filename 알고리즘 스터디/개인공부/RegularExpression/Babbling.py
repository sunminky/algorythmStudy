# https://school.programmers.co.kr/learn/courses/30/lessons/120956#
import re


def check(txt):
    if not txt:
        return 1

    if re.match("aya", txt):
        return check(txt[3:])

    if re.match("ye", txt):
        return check(txt[2:])

    if re.match("woo", txt):
        return check(txt[3:])

    if re.match("ma", txt):
        return check(txt[2:])

    return 0


def solution(babbling):
    answer = 0

    for word in babbling:
        answer += check(word)

    return answer
