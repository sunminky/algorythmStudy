#https://www.acmicpc.net/problem/1786

import sys

###KMP###
def makeTable(pattern : str) ->list:
    table = [0 for _ in pattern]    #일치하는 접두사와 접미사 길이 저장
    j = 0   #접두사 위치
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            table[i] = j + 1
            j += 1
    return table

def kmp(text, pattern, table) -> list:
    find_index = []
    j = 0   #패턴 탐색 위치
    #전체 텍스트와 하나씩 비교해 나가기
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = table[j - 1]
        if text[i] == pattern[j]:
            j += 1
            if j == len(pattern):
                find_index.append(str(i - j + 1 + 1))
                j = table[-1]

    return find_index

###보이어 무어###
def makeIndexTable(pattern : str) -> dict:
    idx_dict = dict()

    #알파벳별로 가장 오른쪽에 있는 값을 저장
    for i, char in enumerate(pattern):
        idx_dict[char] = i

    return idx_dict

def boyerMoore(text, pattern, table) -> list:
    find_index = []
    i = len(pattern) - 1
    
    while i < len(text):
        success = True
        #뒤에서 부터 비교
        for j in range(len(pattern)):
            #일치하지 않는 문자 발견
            if not text[i - j] == pattern[-j-1]:
                success = False
                #패턴 중 일치하는 문자가 없는 경우
                if not table.get(pattern[-j-1], False):
                    i = i + len(pattern)
                #패턴 중 일치하는 문자가 있는 경우
                else:
                    i = max(i+1, i + len(pattern) - table[pattern[-j-1]] - 1)   #탐색 인덱스가 앞으로 역행하는 것 방지
                break
        if success:
            find_index.append(str(i - len(pattern) + 1 + 1))
            i += 1


    return find_index

if __name__ == '__main__':
    text = sys.stdin.readline().rstrip()
    pattern = sys.stdin.readline().rstrip()

    ###kmp###
    table = makeTable(pattern)
    find_index = kmp(text, pattern, table)

    ###boyer moore###
    '''table = makeIndexTable(pattern)
    find_index = boyerMoore(text, pattern, table)'''

    print(len(find_index))
    print(" ".join(find_index))
