# https://www.acmicpc.net/problem/2188
import sys
n_cow, n_barn = map(int, sys.stdin.readline().split())
wish_list = [list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))[1:] for _ in range(n_cow)]  # 소들의 희망 축사 저장
occupant = [-1] * n_barn  # 축사를 점령한 소의 번호 저장
visited = [False] * n_barn


def yield_avail(cur_cow) -> bool:
    for wish in wish_list[cur_cow]:
        # 이미 방문했던 축사는 계산이 끝났기때문에 pass
        if visited[wish]:
            continue
        visited[wish] = True    # 현재 축사 방문

        # 아직 아무도 축사에 들어오지 않은 경우 또는 먼저 축사에 온 소가 자리 양보한 경우
        if occupant[wish] == -1 or yield_avail(occupant[wish]):
            occupant[wish] = cur_cow
            return True

    # 결국 양보받지 못함
    return False


if __name__ == '__main__':
    answer = 0

    # 모든 소들의 취향 조사
    for c_cow in range(n_cow):
        visited = [False] * n_barn  # 현재 소에 대해서 방문한 축사정보 초기화
        if yield_avail(c_cow):
            answer += 1

    print(answer)
