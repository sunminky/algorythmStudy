# https://www.acmicpc.net/problem/10942

import sys

if __name__ == '__main__':
    sys.stdin.readline()    # 칠판에 쓴 숫자, 필요없음
    numbers = sys.stdin.readline().split()
    palindrome_avail = [[1] * len(numbers) for _ in range(len(numbers))]
    
    # 팰린드롬 배열 만들기
    for col in range(1, len(numbers)):
        for row in range(len(numbers) - col):
            if numbers[row] == numbers[row + col]:
                palindrome_avail[row][row + col] = palindrome_avail[row + 1][row + col - 1]
            else:
                palindrome_avail[row][row + col] = 0

    for _ in range(int(sys.stdin.readline())):
        src, dst = map(int, sys.stdin.readline().split())
        print(palindrome_avail[src-1][dst-1])
