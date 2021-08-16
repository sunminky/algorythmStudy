# https://www.acmicpc.net/problem/1305
import sys


# KMP에서 불일치시 되 돌아가는 테이블 만드는 함수
def makeTable(ad_screen) -> list:
    table = [0] * len(ad_screen)    # 0 ~ table[i]의 문자열(접두사)과 현재 접미사가 일치
    j = 0

    for i in range(1, len(ad_screen)):
        # j의 문자와 i의 문자가 일치하지 않는다면
        # j와 i가 일치하거나 j가 0번 인덱스를 가리킬 때 까지 리턴
        while j > 0 and ad_screen[j] != ad_screen[i]:
            j = table[j - 1]
        # 둘이 일치한다면 j를 1증가시켜 다음번 i와 비교할수 있도록 함
        if ad_screen[i] == ad_screen[j]:
            j += 1
            table[i] = j

    return table


if __name__ == '__main__':
    sys.stdin.readline()    # 광고판 크기, 버림
    ad = sys.stdin.readline().rstrip()

    print(len(ad) - makeTable(ad)[-1])
