# https://programmers.co.kr/learn/courses/30/lessons/17685?language=python3

class Trie():
    def __init__(self):
        self.childNodes = dict()
        self.passingCnt = 0  #거쳐간 단어의 수

    def search(self, word : str):
        subTree = self
        for i, char in enumerate(word):
            #거쳐간 단어가 한개 일 때
            if subTree.passingCnt == 1:
                return i
            else:
                subTree = subTree.childNodes[char]  #다음 자식노드 탐색

        return i + 1    #단어를 전부 다 쳐야하는 경우


def makeTree(words : list) -> Trie:
    rootNode = Trie()

    for word in words:
        subTree = rootNode
        for i, char in enumerate(word):
            subTree.passingCnt += 1
            if not subTree.childNodes.get(char, False):
                subTree.childNodes[char] = Trie()
            subTree = subTree.childNodes[char]
            if i == len(word) - 1:
                subTree.passingCnt += 1

    return rootNode


def solution(words):
    answer = 0
    rootNode = makeTree(words)

    for _word in words:
        answer += rootNode.search(_word)

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
