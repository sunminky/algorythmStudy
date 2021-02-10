# https://programmers.co.kr/learn/courses/30/lessons/17685?language=python3

class Trie:
    def __init__(self, depth=0, end=False):
        self.depth = depth
        if end:
            self.superNodes = []  # 부모 노드들 저장
        else:
            self.superNodes = None  # 부모 노드 저장
        self.childNode = dict()  # 자식 노드들 저장

    def addWord(self, word, endNode):
        if word[0] == '@':  # 단어의 끝인 경우
            self.childNode['@'] = endNode
            endNode.superNodes.append(self)
        else:
            if not self.childNode.get(word[0], False):  # 자식이 없으면 새로 만들고 추가
                self.childNode[word[0]] = Trie(depth=self.depth + 1)
            self.childNode[word[0]].superNodes = self  # 부모 노드 추가
            self.childNode[word[0]].addWord(word[1:], endNode)  # 자식 노드 추가


def solution(words):
    answer = 0
    rootNode = Trie(depth=0)  # 루트 노드
    endNode = Trie(depth=-1, end=True)  # 종료노드

    for _word in words:
        rootNode.addWord(_word + '@', endNode)

    for node in endNode.superNodes:
        eNode = node
        RightInFront = True
        while eNode.superNodes is not None and not len(eNode.childNode) > 1:  # 갈림길이 아니거나 루트노드가 아닌 경우
            eNode = eNode.superNodes
            RightInFront = False

        # print(f"[{eNode.depth}, {RightInFront}] {eNode.superNodes} {eNode.childNode}")

        answer += eNode.depth + 1 - RightInFront

    return answer


if __name__ == '__main__':
    result = solution(["go", "gone", "guild"])  # 7
    print(result)

    result = solution(["abc", "def", "ghi", "jklm"])  # 4
    print(result)

    result = solution(["word", "war", "warrior", "world"])  # 15
    print(result)

    result = solution(["aaaaa", "aaaab", "aaabb", "aabbb", "abbbb"])  # 19
    print(result)

    result = solution(["ab", "abc", "abcd", "abcef", "abcefg"])  # 20
    print(result)
