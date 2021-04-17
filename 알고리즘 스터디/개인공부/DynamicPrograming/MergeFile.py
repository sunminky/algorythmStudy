# https://www.acmicpc.net/problem/11066
# 크누스 알고리즘 사용

import sys


def search(start, end, memo, div_point, acc_sum):
    result = int(sys.maxsize)   #memo[start][end] 값

    # 2개의 부분합으로 나눠서 최소값을 구함
    for i in range(div_point[start][end-1], min(div_point[start+1][end] + 1, end)):
        # 최소값 갱신
        if result > memo[start][i] + memo[i + 1][end]:
            result = memo[start][i] + memo[i + 1][end]
            div_point[start][end] = i   # 최소비용 그룹의 종료 인덱스 저장

    # start ~ end 까지의 누적합을 더함(start ~ end 까지의 모든 원소를 더하기 때문에)
    if start == 0:
        return result + acc_sum[end]
    else:
        return result + acc_sum[end] - acc_sum[start-1]


if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        sys.stdin.readline()
        files = [*map(int, sys.stdin.readline().split())]
        memo = [[-1 for _ in range(len(files))] for _ in range(len(files))] #memo[i][j] : i번째 부터 j번째 파일들을 가지고 만들수 있는 최소비용
        div_point = [[-1 for _ in range(len(files))] for _ in range(len(files))]    # div_point[i][j] : i ~ j 까지 행렬 중 최소비용을 가지는 그룹의 끝 인덱스
        acc_sum = [0] * len(files)  # 누적합

        # 누적합 계산
        acc_sum[0] = files[0]
        for i in range(1, len(files)):
            acc_sum[i] = acc_sum[i-1] + files[i]

        for i in range(len(files)):
            memo[i][i] = 0  # 자기 자신만 있는 경우는 비용이 0
            div_point[i][i] = i     # 시작 ~ 자기자신 까지 범위를 가짐

        for i in range(1, len(files)):
            for j in range(len(files) - i):
                memo[j][j+i] = search(j, j+i, memo, div_point, acc_sum)

        print(memo[0][-1])
