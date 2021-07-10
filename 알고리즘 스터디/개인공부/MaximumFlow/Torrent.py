# https://www.acmicpc.net/problem/9577
import sys


time_table = None     # 조각이 다운로드 되는 시간
visited = None
piece = None    # 조각별 다운로드 가능한 시간에 링크


def time_occupant(cur_piece):
    for wish in piece[cur_piece]:
        # 이미 처리한 시간은 패스
        if visited[wish]:
            continue

        visited[wish] = True
        # 시간이 비어있거나 다른 조각이 양보한 경우
        if time_table[wish] == -1 or time_occupant(time_table[wish]):
            time_table[wish] = cur_piece
            return True

    # 결국 양보받지 못한 경우
    return False


if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        n_piece, n_peer = map(int, sys.stdin.readline().split())
        piece = [set() for _ in range(n_piece)]    # 조각별 다운로드 가능한 시간에 링크
        answer = -1

        for _ in range(n_peer):
            start, end, count, *pieces = map(int, sys.stdin.readline().split())

            for p in pieces:
                piece[p - 1].update(range(start, end))

        # 이분 매칭에 필요한 변수 초기화 #
        time_table = [-1] * 100     # 조각이 다운로드 되는 시간
        piece = [sorted(e) for e in piece]  # 조각이 다운로드 될 수 있는 시간들을 오름차순으로 정렬

        ## 이분 매칭 ##
        '모든 조각들에 대해 다운가능한 시간 구함'
        for p in range(n_piece):
            visited = [False] * 100  # 시간의 계산 여부 저장

            # 다운 받을 수 없는 조각이 있는 경우
            if time_occupant(p) is False:
                answer = -1
                break
        # 모든 조각을 다운로드 받은 경우
        else:
            for i in range(99, 0, -1):
                if time_table[i] != -1:
                    answer = i + 1
                    break

        print(answer)
