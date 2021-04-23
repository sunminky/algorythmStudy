# https://www.acmicpc.net/problem/1043

import sys
from collections import deque


if __name__ == '__main__':
    n_participant, n_party = map(int, sys.stdin.readline().split())
    _, *discriminator = map(int, sys.stdin.readline().split())
    neighbor = [[] for _ in range(n_participant + n_party)]
    visited = [False] * (n_participant + n_party)
    distort_cnt = n_party  # 뻥 칠수 있는 파티의 수

    # 파티에 참가한 사람과 파티를 연결지음
    for seq in range(n_party):
        party_sequence = seq + n_participant
        _, *party = map(lambda x: int(x) - 1, sys.stdin.readline().split())

        neighbor[party_sequence].extend(party)  # 파티에 참여한 사람 추가
        
        # 사람별로 참여한 파티 추가
        for p in party:
            neighbor[p].append(party_sequence)

    # 진실을 아는 사람이 참여한 파티 체크
    for dis in discriminator:
        queue = deque()

        if visited[dis - 1] is False:
            queue.append(dis - 1)

        while queue:
            c_node = queue.popleft()

            visited[c_node] = True

            # 파티인 경우 1감소
            if c_node >= n_participant:
                distort_cnt -= 1

            for neigh in neighbor[c_node]:
                if visited[neigh] is False:
                    visited[neigh] = True
                    queue.append(neigh)

    print(distort_cnt)
