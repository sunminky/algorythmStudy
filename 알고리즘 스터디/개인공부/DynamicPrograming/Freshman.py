# https://www.acmicpc.net/problem/5557
import sys

if __name__ == '__main__':
    n_numbers = int(sys.stdin.readline()) - 1
    *numbers, target = map(int, sys.stdin.readline().split())
    value_cnt = [dict() for _ in range(n_numbers)]    # 0 ~ 20 까지의 개수 저장

    value_cnt[0][numbers[0]] = 1    # 맨 처음은 양수만 들어갈 수 있음

    for i in range(1, n_numbers):
        for key in value_cnt[i - 1]:
            if key + numbers[i] <= 20:
                value_cnt[i][key + numbers[i]] = value_cnt[i].get(key + numbers[i], 0) + value_cnt[i-1][key]
            if key - numbers[i] >= 0:
                value_cnt[i][key - numbers[i]] = value_cnt[i].get(key - numbers[i], 0) + value_cnt[i-1][key]

    print(value_cnt[-1][target])
