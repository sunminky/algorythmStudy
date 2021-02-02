# https://www.acmicpc.net/problem/5670
# 트라이 자료구조

import sys


class Trie:
    def __init__(self, charactor):
        self.child = dict()
        self.n_child = 0
        self.charactor = charactor  # root : ^, end : @

    def insert(self, word : str):
        if not self.child.get(word[0], False):
            self.child[word[0]] = Trie(word[0])
            self.n_child += 1

        if not word[0] == '@':
            self.child[word[0]].insert(word[1:])

    def search(self, crossroad, word):
        if self.charactor == '@':   #end
            if crossroad:
                return -1
            return 0
        if self.n_child > 1:    #갈림길
            return self.child[word[0]].search(True, word[1:]) + 1
        if self.n_child == 1:
            return self.child[word[0]].search(False, word[1:])


def makeTrie(words : list) -> Trie:
    root = Trie('^')

    #트라이 만들기
    for e in words:
        root.insert(e)

    return root

def typingCnt(root : Trie, word : str):
    if root.n_child == 1:
        return root.search(False, word)+1
    else:
        return root.search(False, word)

if __name__ == '__main__':
    while True:
        n_word = sys.stdin.readline().rstrip()
        words = []
        answer = 0
        if not n_word.isdecimal():
            break

        for _ in range(int(n_word)):
            words.append(sys.stdin.readline().rstrip() + '@')

        # 트라이 만들기
        root = makeTrie(words)

        # 단어 별로 트라이 계산하기
        for e in words:
            answer += typingCnt(root, e)

        print(f"{(answer / int(n_word)):.2f}")