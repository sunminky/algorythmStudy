# https://www.acmicpc.net/problem/3687

import sys
from math import ceil

price = {2: 1, 3: 7, 4: 4, 5: 2, 6: 0, 7: 8}    # 가격별 숫자
num_price = {1: 2, 7: 3, 4: 4, 2: 5, 0: 6, 8: 7, 6: 6}    # 숫자별 가격


def max_num(number):
    answer = []
    
    # 홀수인 경우
    if number & 1:
        answer.append(7)
        answer.extend([1] * ((number - 3) // 2))
    else:
        answer.extend([1] * (number // 2))

    return "".join(map(str, answer))


# 자리수가 늘어나지 않게 하는 것이 가장 작게 만드는 방법
def min_num(number):
    answer = [8] * ceil(number / 7)     # 모든 자릿수를 8(비용이 가장 많이 듬)로 채움
    debt = 7 * len(answer) - number     # number를 초과하여 사용한 성냥개비의 개수

    # 앞자리 부터 숫자 줄여나가기
    for digit in range(len(answer)):
        for small in sorted(num_price.keys()):
            # 숫자는 0으로 시작할 수 없음
            if small == 0 and digit == 0:
                continue
            diff = num_price[answer[digit]] - num_price[small]  # 성냥개비 개수를 줄이고 숫자도 줄임

            # 초과 사용한 성냥개비보다 덜 줄여지는 경우
            if diff <= debt:
                answer[digit] = small
                debt -= diff
                break

        if debt == 0:
            break
                
    # 초과 사용한 성냥개비가 아직 남아있는 경우
    else:
        # 뒷자릿부터 성냥을 빨리 줄이도록 함(뒷자릿수가 증가함)
        for digit in range(len(answer)-1, -1, -1):
            for big in sorted(price.keys()):
                diff = num_price[answer[digit]] - big   # 성냥개비 개수를 줄임
                # 줄인 개수가 0보다 크게 해야함
                if 0 < diff <= debt:
                    answer[digit] = price[big]
                    debt -= diff
                    break

            if debt == 0:
                break

    # 제일 작은 수가 0이면 6으로 만들어줌
    if answer[0] == 0:
        answer[0] = 6

    return "".join(map(str, answer))


if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        number = int(sys.stdin.readline())

        print(" ".join([min_num(number), max_num(number)]))
