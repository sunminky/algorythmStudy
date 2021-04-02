# https://www.acmicpc.net/problem/9466

import sys
from collections import deque

if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        n_student = int(sys.stdin.readline())
        parent = [0] * n_student
        visited = [False] * n_student
        answer = 0

        for seq, p in enumerate(map(int, sys.stdin.readline().split())):
            parent[seq] = p-1

        for node in range(n_student):
            stack = deque()     # 지나온 경로 저장
            cur_node = node
            
            # 방문한 노드 만날때 까지 탐색
            while visited[cur_node] is False:
                visited[cur_node] = True
                stack.append(cur_node)
                cur_node = parent[cur_node]

            cnt = 0
            # 자기자신 발견할 때 까지 스택을 pop, 사이클이 존재하는지 확인하는 과정
            while stack:
                cnt += 1
                # 자기자신이 스택에서 나옴(사이클이 존재)
                if stack.pop() == cur_node:
                    answer += cnt   # 정답에 스택에서 pop 한 개수만큼 더해줌
                    break
        print(n_student - answer)
