#https://level.goorm.io/exam/49060/%EA%B0%9C%EB%AF%B8-%EC%A7%91%ED%95%A9%EC%9D%98-%EC%A7%80%EB%A6%84/quiz/1
import sys

if __name__ == "__main__" :
    _, target = tuple(map(int, sys.stdin.readline().split()))
    ants = sorted(list(map(int, sys.stdin.readline().split())))
    n_members = [i for i in range(1, len(ants)+1)]  #각 개미까지 고려했을 때 지름내에 있는 이웃개미의 수
    min_idx = max_idx = 0

    for i in range(1, len(ants)):
        #최소값 인덱스 갱신
        min_idx = i if ants[min_idx] > ants[i] else min_idx
        #최대값 인덱스 갱신
        max_idx = i if ants[max_idx] < ants[i] else max_idx

        #개미 집합이 원하는 지름을 넘는 경우
        if ants[max_idx] - ants[min_idx] > target:
            for idx in range(min_idx, max_idx+1):
                #개미 집합의 지름이 target보다 작거나 같을 때까지 탐색
                if ants[max_idx] - ants[idx] <= target:
                    min_idx = idx
                    break

        n_members[i] -= min_idx

    print(len(ants) - max(n_members))