# https://www.acmicpc.net/problem/1208
import sys

if __name__ == '__main__':
    _, target = map(int, sys.stdin.readline().split())
    subsequence = tuple(map(int, sys.stdin.readline().split()))
    knapsack = [dict() for _ in range(2)]   # 앞 순열에서 담기, 뒤 순열에서 담기
    answer = 0

    subsequence = (subsequence[:len(subsequence) // 2], subsequence[len(subsequence) // 2:])  # 순열 쪼개기

    for i in range(2):
        knapsack[i][0] = 1

        for e in subsequence[i]:
            prev_knapsack = knapsack[i].copy()

            for key in prev_knapsack.keys():
                knapsack[i][key + e] = knapsack[i].get(key + e, 0) + prev_knapsack[key]

    for k1 in knapsack[0].keys():
        answer += knapsack[1].get(target - k1, 0) * knapsack[0][k1]

    # 부분수열의 길이가 0인경우 빼주기
    if target == 0:
        answer -= 1

    print(answer)
