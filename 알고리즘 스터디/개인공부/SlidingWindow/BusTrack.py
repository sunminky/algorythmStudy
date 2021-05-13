# https://www.acmicpc.net/problem/10165
import sys

if __name__ == '__main__':
    n_stop = int(sys.stdin.readline().rstrip())
    track = [[*map(int, sys.stdin.readline().split()), seq]  # (시작점, 도착점, 노선번호)
             for seq in range(int(sys.stdin.readline().rstrip()))]
    valid_track = [True] * len(track)

    # 0번 정류장을 거치는 경우, Ex) (5, 1) -> (5, 11)
    for e in track:
        if e[0] > e[1]:
            e[1] += n_stop

    track.sort(key=lambda x: (x[0], -x[1]))  # 시작점이 빠른 순으로 정렬, 도착점이 느린 순으로 정렬

    ## Search ##
    start_idx = end_idx = 0
    for e in track:
        if valid_track[e[2]]:
            if e[1] <= end_idx:
                valid_track[e[2]] = False
            else:
                end_idx = e[1]

    # 삐져나온 애들 체크
    for e in track:
        if valid_track[e[2]]:
            if e[1] + n_stop <= end_idx:
                valid_track[e[2]] = False
            else:
                break

    ## 정답 출력 ##
    answer = []
    for seq, valid in enumerate(valid_track):
        if valid:
            answer.append(str(seq + 1))

    print(" ".join(answer))
