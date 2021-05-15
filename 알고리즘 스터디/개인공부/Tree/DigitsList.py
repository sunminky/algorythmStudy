# https://www.acmicpc.net/problem/5052
import sys


class Trie:
    def __init__(self, value=''):
        self.value = value
        self.child = dict()
        self.end = False    # 현재 노드가 마지막 문자열 존재여부

    def chaining(self, word, idx) -> bool:
        if self.end:
            return True     # 접두사인 문자열이 이전에 등장했던 경우

        # 마지막 문자열까지 트라이에 넣음
        if idx == len(word):
            self.end = True
            # 현재 단어를 접두사로 하는 단어들이 존재하는 경우
            if self.child:
                return True
            return False

        if self.child.get(word[idx], False) is False:
            self.child[word[idx]] = Trie(word[idx])

        # 다음 문자를 넣음
        return self.child[word[idx]].chaining(word, idx + 1)


if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline().rstrip())):
        root = Trie()   # 루트노드
        answer = False
        for _ in range(int(sys.stdin.readline().rstrip())):
            # 겹치는 문자열이 발견되지 않음
            if answer is False:
                answer |= root.chaining(sys.stdin.readline().rstrip(), 0)
            # 이미 겹치는 문자열이 발견됨
            else:
                sys.stdin.readline()

        if answer:
            print("NO")
        else:
            print("YES")
