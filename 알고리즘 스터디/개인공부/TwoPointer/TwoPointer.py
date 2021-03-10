# https://www.acmicpc.net/problem/1806

import sys

if __name__ == '__main__':
    n_number, target = map(int, sys.stdin.readline().split())
    numbers = tuple(map(int, sys.stdin.readline().split()))
    answer = 100001 #최악의 경우
    pointer1 = pointer2 = 0
    num = numbers[0]    #구간 합 저장

    while True:
        # 구간 합이 타겟보다 큰 경우
        if num >= target:
            # 구간의 길이 최소값 갱신
            answer = min(answer, pointer2 - pointer1 + 1)
            # 구간을 앞에서 한 칸 줄임
            num -= numbers[pointer1]
            pointer1 += 1
            if pointer1 == n_number:
                break
            #구간이 한 칸 짜리 였던 경우(앞 포인터가 뒷 포인터를 넘어간 경우)
            if pointer1 == pointer2 + 1:
                pointer2 = pointer1
                num = numbers[pointer2]
        else:
            #구간 합이 타겟을 만족할 때 까지 뒤로 한 칸 씩 늘림
            pointer2 += 1
            if pointer2 == n_number:
                break
            num += numbers[pointer2]

    if answer == 100001:
        print(0)
    else:
        print(answer)
