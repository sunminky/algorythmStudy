#https://programmers.co.kr/learn/courses/30/lessons/17685?language=python3

class Trie:
    def __init__(self, depth=0):
        self.depth = depth
        self.superNodes = set() #부모 노드들 저장
        self.childNode = dict() #자식 노드들 저장

    def addWord(self, word, endNode):
        if word[0] == '@':  #단어의 끝인 경우
            endNode.superNodes.add(self)
        else:
            if not self.childNode.get(word[0], False):  #자식이 없으면 새로 만들고 추가
                self.childNode[word[0]] = Trie(depth=self.depth+1)
            self.childNode[word[0]].superNodes.add(self)    #부모 노드 추가
            self.childNode[word[0]].addWord(word[1:], endNode)  #자식 노드 추가

def solution(words):
    answer = 0
    rootNode = Trie(depth=0)   #루트 노드
    endNode = Trie(depth=-1)    #종료노드

    for _word in words:
        rootNode.addWord(_word + '@', endNode)

    return answer

if __name__ == '__main__':
    result = solution(["go","gone","guild"])
    print(result)

    result = solution(["word", "war", "warrior", "world"])
    print(result)