# https://www.acmicpc.net/problem/2671
import sys
import re

if __name__ == '__main__':
    sound = sys.stdin.readline().rstrip()
    
    if re.fullmatch("((100+1+)|01)+", sound):
        print("SUBMARINE")
    else:
        print("NOISE")

'''
match : target이 해당 패턴으로 시작하는지를 검사
fullmatch : 문자열 전체가 해당 패턴인지를 검사
'''
