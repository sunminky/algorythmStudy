#https://www.acmicpc.net/problem/3344
import sys

'''
1. n 을 6 으로 나눈 나머지 가 2 또는 3이 아니면 목록은 단순히 모든 짝수 다음에 n 보다 크지 않은 모든 홀수가 오는 것 입니다.
2. 그렇지 않으면 짝수와 홀수(2, 4, 6, 8 – 1, 3, 5, 7)의 목록을 별도로 작성하십시오.
3. 나머지가 2이면 홀수 목록에서 1과 3을 바꾸고 5를 끝으로 이동합니다( 3, 1 , 7, 5 ).
4. 나머지가 3이면 2를 짝수 목록의 끝으로 이동하고 1,3을 홀수 목록의 끝으로 이동합니다(4, 6, 8, 2 – 5, 7, 1, 3 ).
5. 짝수 목록에 홀수 목록을 추가하고 왼쪽에서 오른쪽으로(a2, b4, c6, d8, e3, f1, g7, h5) 이 숫자로 지정된 행에 퀸을 배치합니다.
'''

if __name__ == '__main__':
    n = int(sys.stdin.readline())

    if n % 6 not in (2, 3):
        for i in range(2, n + 1, 2):
            print(i)
        for i in range(1, n + 1, 2):
            print(i)

    else:
        even = [i for i in range(2, n + 1, 2)]
        odd = [i for i in range(1, n + 1, 2)]

        if n % 6 == 2:
            # 1과 3을 바꿈
            odd[0] = 3
            odd[1] = 1
            del odd[2]  # 5 삭제
            odd.append(5)

        else:
            # 2를 짝수 목록의 끝으로 이동
            del even[0]
            even.append(2)

            # 1,3을 홀수 목록의 끝으로 이동
            del odd[0]  # 1제거
            del odd[0]  # 3 제거
            odd.append(1)
            odd.append(3)

        # 출력
        for e in even:
            print(e)
        for e in odd:
            print(e)
