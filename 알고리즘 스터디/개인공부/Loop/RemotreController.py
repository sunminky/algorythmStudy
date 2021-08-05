# https://www.acmicpc.net/problem/1107
import sys


# 현재 채널 중 고장난 버튼의 숫자가 들어가 있으면 False, 아니면 True
def check(src, broken):
    for i in range(len(str(src))):
        if broken.get(src % 10, False) is False:
            src //= 10
            continue

        return False

    return True


if __name__ == '__main__':
    target = int(sys.stdin.readline())  # 타겟
    n_broken = int(sys.stdin.readline())
    broken = dict(zip(map(int, sys.stdin.readline().split()), [True] * n_broken))
    answer = sys.maxsize

    ## 고장나지 않은 버튼으로 이루어진 채널 나올때 까지 목표로 하는 채널에서 1씩 빼기 ##
    cnt = 0
    tmp = target

    while tmp > -1:
        if tmp == 100:
            break

        # 모든 숫자가 고장난 버튼이 아닌 경우는?
        if check(tmp, broken):
            break

        tmp -= 1
        cnt += 1

    # tmp가 -1인 경우는 체널이 0이 될 때까지 고장나지 않은 버튼으로 이루어진 채널을 찾지 못한 것
    if tmp != -1:
        # 채널 번호 새로 누르는 것 보다 +, - 버튼 누르는게 더 나은 경우
        if 97 < tmp < 103:
            answer = min(answer, cnt + abs(100 - tmp))
        else:
            # - 버튼 누른 횟수 + 숫자 버튼 누른 횟수
            answer = min(answer, cnt + len(str(tmp)))

    ## 고장나지 않은 버튼으로 이루어진 채널 나올때 까지 목표로 하는 채널에서 1씩 더하기 ##
    cnt = 0
    tmp = target

    while tmp < 1000000:
        if tmp == 100:
            break

        # 모든 숫자가 고장난 버튼이 아닌 경우는?
        if check(tmp, broken):
            break

        tmp += 1
        cnt += 1

    # 채널 번호 새로 누르는 것 보다 +, - 버튼 누르는게 더 나은 경우
    if 97 < tmp < 103:
        answer = min(answer, cnt + abs(100 - tmp))
    else:
        # - 버튼 누른 횟수 + 숫자 버튼 누른 횟수
        answer = min(answer, cnt + len(str(tmp)))

    print(answer)
