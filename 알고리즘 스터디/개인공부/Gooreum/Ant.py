#https://level.goorm.io/exam/49060/%EA%B0%9C%EB%AF%B8-%EC%A7%91%ED%95%A9%EC%9D%98-%EC%A7%80%EB%A6%84/quiz/1

import sys

if __name__ == "__main__" :
    _, target = map(int, sys.stdin.readline().split())
    ants = sorted(map(int, sys.stdin.readline().split()))
    n_members = [*range(1, len(ants)+1)]  #각 개미까지 고려했을 때 지름내에 있는 이웃개미의 수
    min_idx = 0

    for i in range(1, len(ants)):
        #개미 집합이 원하는 지름을 넘는 경우
        if ants[i] - ants[min_idx] > target:
            for idx in range(min_idx, i+1):
                #개미 집합의 지름이 target보다 작거나 같을 때까지 탐색
                if ants[i] - ants[idx] <= target:
                    min_idx = idx
                    break

        n_members[i] -= min_idx

    print(len(ants) - max(n_members))
