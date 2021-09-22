# https://programmers.co.kr/learn/courses/30/lessons/17685?language=python3
import sys
sys.setrecursionlimit(1000001)


class Trie:
    def __init__(self, char='', root=False):
        self.char = char
        self.root = root
        self.passing = 0
        self.end = False
        self.child = dict()

    def add_node(self, new_node, idx):
        self.passing += 1

        if len(new_node) == idx:
            self.end = True
            return

        if new_node[idx] not in self.child:
            self.child[new_node[idx]] = Trie(char=new_node[idx], root=False)

        self.child[new_node[idx]].add_node(new_node, idx + 1)

    def search(self, depth: int):
        result = 0

        if self.passing == 1 and not self.root:
            return depth

        if self.end:
            result += depth

        for _child in self.child.keys():
            result += self.child[_child].search(depth+1)

        return result


def solution(words):
    root_node = Trie(root=True)

    for word in words:
        root_node.add_node(word, 0)
        
    # 탐색

    return root_node.search(0)


if __name__ == '__main__':
    result = solution(["go", "gone"])  # 5
    print(result)

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
