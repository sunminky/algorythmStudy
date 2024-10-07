# https://www.acmicpc.net/problem/9250
import sys
from collections import deque


class Trie:
    def __init__(self, alpah):
        self.alpahbet = alpah
        self.terminal = False
        self.child = dict()
        self.fail = None

    def insert(self, word, idx):
        if len(word) - 1 == idx:
            self.terminal = True
            return

        if word[idx + 1] not in self.child:
            self.child[word[idx + 1]] = Trie(word[idx + 1])

        self.child[word[idx + 1]].insert(word, idx + 1)

    def print(self, stack):

        print(self)

        if self.alpahbet:
            stack.append(str(self.alpahbet))

        if self.terminal:
            print("".join(stack))
            del stack[-1]
            return

        for neigh in self.child:
            self.child[neigh].print(stack)

        if self.alpahbet:
            del stack[-1]


if __name__ == '__main__':
    pattern = tuple(sys.stdin.readline().rstrip() for _ in range(int(sys.stdin.readline().rstrip())))
    target = tuple(sys.stdin.readline().rstrip() for _ in range(int(sys.stdin.readline().rstrip())))
    root_node = Trie(None)
    queue = deque()

    for txt in pattern:
        root_node.insert(txt, -1)

    # 실패함수 만들기
    root_node.fail = root_node

    # 각 패턴의 첫글자의 실패함수는 root노드
    for neigh in root_node.child:
        root_node.child[neigh].fail = root_node
        queue.append(root_node.child[neigh])

    while queue:
        cur_node = queue.popleft()

        for neigh_key, neigh_value in cur_node.child.items():
            fail_node = cur_node.fail
            dropbyterminal = cur_node.fail.terminal

            while fail_node.alpahbet is not None and neigh_key not in fail_node.child:
                fail_node = fail_node.fail
                dropbyterminal = dropbyterminal or fail_node.terminal

            if neigh_key in fail_node.child:
                neigh_value.fail = fail_node.child[neigh_key]
                neigh_value.terminal = neigh_value.terminal or fail_node.child[neigh_key].terminal
            else:
                neigh_value.fail = root_node

            # print(f"{cur_node.alpahbet} - {neigh_key}({neigh_value.terminal}) : {neigh_value.fail.alpahbet}")

            queue.append(neigh_value)

    # 트라이 순회
    for txt in target:
        cur_node = root_node

        for ch in txt:
            # print(f"{cur_node.alpahbet} : {ch}")

            while cur_node.alpahbet is not None and ch not in cur_node.child:
                cur_node = cur_node.fail

            if ch in cur_node.child:
                cur_node = cur_node.child[ch]

            if cur_node.terminal:
                print("YES")
                break
        else:
            print("NO")
