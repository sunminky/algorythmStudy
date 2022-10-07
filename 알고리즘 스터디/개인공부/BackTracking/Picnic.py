# https://www.acmicpc.net/problem/2026
import sys

n_participant, n_alumni, n_relation = map(int, sys.stdin.readline().split())
relationship = [set() for _ in range(n_alumni)]
ordered_relationship = [None] * n_alumni


def chaining(participant: list, vacancy: int, captain: int, invite_idx: int):
    if vacancy == 0:
        return participant.copy()

    # 우두머리 친구들 중 탐색
    for new_crew_idx in range(invite_idx, len(ordered_relationship[captain])):
        new_crew = ordered_relationship[captain][new_crew_idx]

        for crew in participant:
            # 참가자 중 친구가 아닌 사람이 있음
            if new_crew not in relationship[crew]:
                break
        # 기존 멤버와 모두 친구임
        else:
            participant.append(new_crew)

            result = chaining(participant, vacancy - 1, captain, new_crew_idx + 1)

            if result is not None:
                return result

            participant.pop()

    return None


if __name__ == '__main__':
    answer = None

    for _ in range(n_relation):
        p1, p2 = sorted(map(int, sys.stdin.readline().split()))
        relationship[p1 - 1].add(p2 - 1)

    for seq in range(n_alumni):
        ordered_relationship[seq] = sorted(relationship[seq])

    for seq in range(n_alumni):
        if len(relationship) < n_participant:
            continue

        answer = chaining([seq], n_participant - 1, seq, 0)

        if answer is not None:
            for e in answer:
                print(e + 1)
            break
    else:
        print(-1)
