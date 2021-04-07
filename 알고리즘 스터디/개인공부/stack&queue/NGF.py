# https://www.acmicpc.net/problem/17299

import sys
from collections import deque

if __name__ == '__main__':
    sys.stdin.readline()
    number = sys.stdin.readline().split()
    cnt_dict = dict()
    stack = deque(maxlen=len(number))
    answer = ['-1'] * len(number)

    # 숫자 개수 세기
    for n in number:
        if cnt_dict.get(n, False) is False:
            cnt_dict.setdefault(n, 0)
        cnt_dict[n] += 1
        
    # 스택에 숫자 집어넣기
    for seq, n in enumerate(reversed(number)):
        # 자기 보다 작은 숫자 제거
        while stack:
            if cnt_dict[stack[-1]] <= cnt_dict[n]:
                stack.pop()
            else:
                answer[-seq-1] = stack[-1]
                break
        stack.append(n)

    print(" ".join(answer))
