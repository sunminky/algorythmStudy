# http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=1109&sca=2060
import sys


def get_max(cost):
    # 0 ~ 최대 부분합인 인덱스, 값 구하기
    max_val = 0
    max_idx = -101
    for i in range(len(cost)):
        if max_val <= cost[i]:
            max_val = cost[i]
            max_idx = i

    # 0 ~ 최대 부분합 인덱스 까지의 최소 부분합 구하기
    min_val = 101
    for i in range(max_idx + 1):
        if min_val > cost[i]:
            min_val = cost[i]

    # 최소 부분합이 0보다 작으면 그 부분을 빼줌
    if min_val < 0:
        return max_val - min_val

    return max_val


if __name__ == '__main__':
    sys.stdin.readline()
    numbers = tuple(map(int, sys.stdin.readline().split()))
    cost = [0] * len(numbers)
    answer = 0
    
    # 정방향 합 (앞에서 부터 부분합 구하기)
    for i in range(len(numbers)):
        cost[i] = cost[i-1] + numbers[i]

    answer = max(get_max(cost), answer)

    # 역방향 합( 뒤에서 부터 부분합 구하기)
    cost[-1] = numbers[-1]
    for i in range(len(numbers) - 2, -1, -1):
        cost[i] = cost[i+1] + numbers[i]

    answer = max(get_max(list(reversed(cost))), answer)
    print(answer)
