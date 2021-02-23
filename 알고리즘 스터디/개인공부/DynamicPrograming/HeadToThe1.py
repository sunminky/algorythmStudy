#https://www.acmicpc.net/problem/1463

import sys

if __name__ == '__main__':
    target = int(sys.stdin.readline())
    numbers = {target}  #연산자를 operation_cnt번 사용해 만들 수 있는 수
    operation_cnt = 0   #연산자 사용 횟수

    while 1 not in numbers:
        #이전 집합에서 연산자를 사용해 만들 수 있는 수를 저장
        new_numbers = set()

        for n in numbers:
            new_numbers.add(n - 1)
            #2로 나누어 떨어지는 경우 2로 나눈값을 집합에 추가
            if n % 2 == 0:
                new_numbers.add(n // 2)
            #3으로 나누어 떨어지는 경우 3으로 나눈값을 집합에 추가
            if n % 3 == 0:
                new_numbers.add(n // 3)
        
        #연산자 사용 횟수 1증가
        operation_cnt += 1
        #만들어진 집합 업데이트
        numbers = new_numbers

    print(operation_cnt)