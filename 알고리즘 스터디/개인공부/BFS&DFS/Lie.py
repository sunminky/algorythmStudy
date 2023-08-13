# https://www.acmicpc.net/problem/1043
import sys
from collections import deque

if __name__ == '__main__':
    n_participant, n_party = map(int, sys.stdin.readline().split())
    n_discriminator, *discriminator = map(int, sys.stdin.readline().split())
    neigh = [set() for _ in range(n_participant)]
    discriminators = [False] * n_participant  # 진실을 아는 사람
    parties = [True] * n_party  # 거짓말치면 안되는 파티 표시
    attended = [[] for _ in range(n_participant)]  # 참가자별로 참석한 파티 기록
    visited = [False] * n_participant

    # 간선 연결
    for seq in range(n_party):
        _, *_participant = map(lambda x: int(x) - 1, sys.stdin.readline().split())

        for e in _participant:
            neigh[e].update(_participant)
            attended[e].append(seq)

    # 진실을 아는 사람끼리 네트워크 구축
    for e in discriminator:
        queue = deque([e - 1])
        visited[e - 1] = True

        while queue:
            cur_participant = queue.popleft()

            discriminators[cur_participant] = True

            for _neight in neigh[cur_participant]:
                if visited[_neight]:
                    continue

                queue.append(_neight)
                visited[_neight] = True

    # 진실을 아는  사람이 참가한 파티 컷
    for seq, lie in enumerate(discriminators):
        if not lie:
            continue

        for e in attended[seq]:
            parties[e] = False

    print(sum(parties))
