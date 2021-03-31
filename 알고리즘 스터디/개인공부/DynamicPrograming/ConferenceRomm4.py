# https://www.acmicpc.net/problem/19623
# 좌표압축 굳이 안해도 됨, 오히려 안하는게 이득임

import sys


# 좌표 압축
def compress():
    meetings = [[*map(int, sys.stdin.readline().split())] for _ in range(int(sys.stdin.readline()))]
    unify = set()

    for m in meetings:
        unify.add(m[0])
        unify.add(m[1])

    unify_dict = dict(zip(sorted(unify), range(len(unify))))

    # 좌표 크기 순으로 번호 부여
    for i in range(len(meetings)):
        meetings[i][0] = unify_dict[meetings[i][0]]
        meetings[i][1] = unify_dict[meetings[i][1]]

    return meetings, len(unify)


if __name__ == '__main__':
    conference, pos_variety = compress()
    cost = [0] * pos_variety    # 현재 시간까지 고려했을 때 최대 회의가능 인원

    conference.sort(key=lambda x: x[1])

    prev_idx = -1
    for src, dst, participant in conference:
        # 이전 시간의 최대값을 현재시간 까지 대입
        while prev_idx < dst:
            cost[prev_idx + 1] = cost[max(0, prev_idx)]
            prev_idx += 1

        # 새로 들어온 회의를 하는 것이 더 이득인 경우 갱신
        cost[dst] = max(cost[dst], cost[src] + participant)

    print(cost[-1])
