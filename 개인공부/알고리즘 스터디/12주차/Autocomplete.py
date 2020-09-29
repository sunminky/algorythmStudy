#https://programmers.co.kr/learn/courses/30/lessons/17685?language=python3
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


    def refer(self, word, cnt, mini):
        if len(word) == 0:   #단어가 끝났다면 종료
            return mini

        if self.childNode.get("end", False) and len(self.childNode) == 1:   #종료노드인 경우
            return mini

        # 더이상 매칭되는 문자가 없을 때...

        return self.childNode[word[0]].refer(word[1:], cnt+1, mini)

def solution(words) :
    answer = 0
    rootNode = Trie()

    #입력된 단어들 트라이에 저장하기
    for element in words:
        rootNode.add(element)

    for element in words:
        answer += rootNode.refer(element, 0, 0)

    return answer

if __name__ == '__main__':
    #result = solution(["go","gone","guild"])
    #print(result)

    result = solution(["word", "war", "warrior", "world"])
    print(result)