# https://www.acmicpc.net/problem/1084

import sys

if __name__ == '__main__':
    while True:
        try:
            int(sys.stdin.readline())  # 가게에서 파는 숫자의 개수 N
        except ValueError:
            break

        stock_dict = dict()  # 비용별 최대 숫자 저장
        answer = dict(zip(range(10), [0] * 10))

        stock = list(map(int, sys.stdin.readline().split()))    # 판매하는 숫자의 가격
        n_number = len(stock)   # 문구점에서 판매하는 숫자의 길이

        # 코스트별 최대값 저장
        for seq, cost in enumerate(stock):
            if stock_dict.get(cost, False) is False:
                stock_dict.setdefault(cost)
            stock_dict[cost] = seq

        balance = int(sys.stdin.readline())  # 잔액
        cost_list = sorted(stock_dict.keys())   # 가격이 낮은 순서대로 정의

        zero_pass = True    # 0밖에 안파는 경우
        # 몸집 최대한 늘리기, 모두 0이 아니지 않게 하기
        if stock_dict[cost_list[0]] == 0:
            # 0 말고 다른 숫자도 파는 경우
            if len(cost_list) > 1 and balance >= cost_list[1]:
                answer[stock_dict[cost_list[1]]] += 1
                balance -= cost_list[1]
            else:
                zero_pass = False

        # 0 말고 다른 숫자도 파는 경우
        if zero_pass:
            answer[stock_dict[cost_list[0]]] += balance // cost_list[0]
            balance %= cost_list[0]

            # 돈이 남았다면 앞에서 부터 큰수로 업데이트 하기
            for num in range(n_number-1, -1, -1):
                if balance <= 0:
                    break

                # 숫자가 들어있었다면
                if answer[num] != 0:
                    #숫자 업그레이드 가능한지 체크
                    for upper in range(n_number-1, num, -1):
                        diff = stock[upper] - stock[num]
                        upgrade_cnt = min(balance // diff, answer[num])

                        #업그레이드
                        answer[upper] += upgrade_cnt
                        answer[num] -= upgrade_cnt
                        balance -= diff * upgrade_cnt

                        if balance <= 0:
                            break
        else:
            # 0밖에 안팔고 0을 살돈이 있는 경우
            if balance >= cost_list[0]:
                answer[0] = 1

        print(sum(answer.values()))     # 방번호 길이

        # 앞에서 50개
        forward_answer = []
        limit = 0
        for key in range(n_number-1, -1, -1):
            repeat = min(answer[key], 50-limit)
            forward_answer.extend([key] * repeat)
            limit += repeat
            if limit >= 50:
                break

        print("".join(map(str, forward_answer)))

        # 뒤에서 50개
        backward_answer = []
        limit = 0
        for key in range(n_number):
            repeat = min(answer[key], 50 - limit)
            backward_answer.extend([key] * repeat)
            limit += repeat
            if limit >= 50:
                break

        print("".join(map(str, reversed(backward_answer))))
