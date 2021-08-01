# https://www.acmicpc.net/problem/1728
import sys

if __name__ == '__main__':
    n_marvel = int(sys.stdin.readline())
    positions = [set(map(int, sys.stdin.readline().split())) for _ in range(n_marvel + 1)]
    positions[0] = sorted(positions[0]) # 출발지의 위치를 오름차순으로 정렬
    speed = set()   # 가능한 속도 저장
    answer = [0] * n_marvel

    # (도착점 - 시작점)  / 움직인 간격은 속도
    # 속도가 정수인 경우에만 저장
    '''
    for src in positions[0]:
        for dst in positions[-1]:
            if (dst - src) % n_marvel == 0:
                speed.add((dst - src) // n_marvel)
    '''
    [speed.add((dst - src) // n_marvel) for src in positions[0] for dst in positions[-1] if (dst-src) % n_marvel == 0]

    # 모든 출발지에 대해 가능한 속도들로 모든 사진을 만족할 수 있는지 체크
    for seq, src in enumerate(positions[0]):
        for velocity in speed:
            for i in range(len(positions)):
                if src + velocity * i in positions[i]:
                    continue
                break
            # 현재 속도로 모든 사진을 만족하는 경우
            else:
                answer[seq] = velocity
                break

    for i in range(n_marvel):
        print(positions[0][i], answer[i])
