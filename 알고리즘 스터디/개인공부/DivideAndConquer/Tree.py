# https://www.acmicpc.net/problem/4256

import sys

if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        N = int(sys.stdin.readline())
        pre_ord = tuple(map(lambda x: int(x)-1, sys.stdin.readline().split()))
        in_ord = tuple(map(lambda x: int(x)-1, sys.stdin.readline().split()))
        pointer = [[-1, -1] for _ in range(N + 1)]    # [이전 노드, 다음 노드], 노드들 위치 + 기준점
        visited = dict()    # 방문노드 저장

        p_idx = 0   #전위순위 인덱스
        i_idx = 0   #중위순회 인덱스

        while p_idx != len(pre_ord):
            visited[pre_ord[p_idx]] = True

            #기준점 뒤에 붙이기
            if pointer[-1][1] != -1:
                pointer[pointer[-1][1]][0] = pre_ord[p_idx]
            pointer[pre_ord[p_idx]][1] = pointer[-1][1]
            pointer[-1][1] = pre_ord[p_idx]
            pointer[pre_ord[p_idx]][0] = N

            # 전위순회 값 == 중위순회 값, 맨 왼쪽 노드임
            if pre_ord[p_idx] == in_ord[i_idx]:
                new_criteria = pointer[-1]
                while visited.get(in_ord[i_idx], False):
                    new_criteria = pointer[in_ord[i_idx]]
                    i_idx += 1
                    if i_idx == len(in_ord):
                        break

                #기준점 옮기기
                #원래대로 돌리고 나오기
                if pointer[-1][0] != -1:
                    pointer[pointer[-1][0]][1] = pointer[-1][1]
                pointer[pointer[-1][1]][0] = pointer[-1][0]
                #새로운 연결하기
                pointer[-1][0] = new_criteria[0]
                pointer[-1][1] = in_ord[i_idx - 1]
                pointer[pointer[-1][1]][0] = N

            p_idx += 1

        # 중위탐색
        answer = []
        c_node = pre_ord[0]

        # 제일 마지막 노드(루트노드 = 전위탐색 제일 첫번째 요소)부터 역으로 거슬러 올라감
        while c_node != -1:
            # 기준점인 경우 패스
            if c_node != N:
                answer.append(str(c_node + 1))
            c_node = pointer[c_node][0]

        print(" ".join(reversed(answer)))
