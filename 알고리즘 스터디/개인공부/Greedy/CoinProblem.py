# https://www.acmicpc.net/problem/1398
import sys
from math import log10, floor

if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        cost_ten = [0] * 16     # 10 ** k 번째 동전의 개수 저장
        data = int(sys.stdin.readline())

        divider = floor(log10(data))    # 현재 금액이 가질 수 있는 가장 큰 액수의 동전

        # 10 ** k 짜리 동전만 사용한 경우 필요한 동전의 개수
        for div in range(divider, -1, -1):
            cost_ten[div] = data // (10 ** div)
            data %= 10 ** div

        answer = sum(cost_ten)

        for i in range(1, 16, 2):
            # 10 * 2 + 1 * 5 => 25 * 1
            exchange = min(cost_ten[i] // 2, cost_ten[i-1] // 5)
            cost_ten[i] -= 2 *exchange
            cost_ten[i - 1] -= 5 * exchange
            answer -= exchange * 6  # 7개 였던 동전을 1개로 만들었기 때문에 6개가 절약됨

            # 10 * 5 => 25 * 2
            exchange = cost_ten[i] // 5
            # cost_ten[i] -= exchange * 5   # 불필요한 계산
            answer -= exchange * 3  # 5개였던 동전을 2개로 만들었기 때문에 3개가 절약됨

        print(answer)
