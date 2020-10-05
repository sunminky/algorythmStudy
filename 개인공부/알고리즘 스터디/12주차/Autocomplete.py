#https://programmers.co.kr/learn/courses/30/lessons/17685?language=python3
import sys

class Trie:
    def __init__(self):
        self.childNode = dict()

    def add(self, word):
        if len(word) == 0:
            self.childNode["end"] = True   #종료문자 추가
            return

        if not self.childNode.get(word[0], None):   #없으면 추가
            self.childNode[word[0]] = Trie()

        self.childNode[word[0]].add(word[1:])   #있으면 그 뒤 문자 추가


    def refer(self, word, cnt):
        if len(word) == 0:   #단어가 끝났다면 종료
            if len(self.childNode) > 1: #단어를 전부써야만 구별되는 경우
                return cnt, False
            return cnt, True

        #반환값 확인, 자식노드가 1보다 크면 바로 리턴
        ret_val, flag = self.childNode[word[0]].refer(word[1:], cnt+1)
        if flag and len(self.childNode) > 1: #자식노드가 1보다 큼, 구별되지 않는 경우 생기는 경우
            flag = False
            ret_val = cnt+1

        return ret_val, flag

def solution(words) :
    sys.setrecursionlimit(1000001)  #스택깊이 제한 해제
    answer = 0
    rootNode = Trie()

    #입력된 단어들 트라이에 저장하기
    for element in words:
        rootNode.add(element)

    for element in words:
        answer += rootNode.refer(element, 0)[0]

    return answer

if __name__ == '__main__':
    result = solution(["go","gone","guild"])
    print(result)

    result = solution(["word", "war", "warrior", "world"])
    print(result)