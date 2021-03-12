#https://www.acmicpc.net/problem/3111

import sys

def rabinkarp(text) -> int:
    hash_val = 0
    de = 1

    for ch in text:
        hash_val += ch * de
        de <<= 1

    return hash_val


if __name__ == '__main__':
    target = [ord(ch) - 96 for ch in sys.stdin.readline().rstrip()]
    reverse_target = list(reversed(target))
    text = [ord(ch) - 96 for ch in sys.stdin.readline().rstrip()]
    front_stack = []    # 앞에서부터 문자열의 문자를 집어넣는 스택
    back_stack = []     # 뒤에서부터 문자열의 문자를 집어넣는 스택
    front_pointer = 0        # 앞에서부터 한칸씩 올라오는 포인터
    back_pointer = len(text) - 1    #뒤에서부터 한칸씩 내려가는 포인터
    target_val = rabinkarp(target)   #타겟의 해쉬값
    reversed_target_val = rabinkarp(reverse_target)  #타겟의 역순의 해쉬값
    front_val = -1  # 앞에서 부터 쌓은 스택의 마지막 문자들의 해쉬값
    back_val = -1  # 뒤에서 부터 쌓은 스택의 마지막 문자들의 해쉬값

    while front_pointer <= back_pointer:
        # 앞에서 일치하는 문자열 처리
        while front_pointer <= back_pointer:
            front_stack.append(text[front_pointer]) #스택에 글자를 하나 넣음
            if len(front_stack) >= len(target):
                if front_val == -1:
                    front_val = rabinkarp(front_stack[-len(target):])
                else:
                    front_val = ((front_val - front_stack[-len(target) - 1]) >> 1) + front_stack[-1] * (1 << (len(target) - 1))
            front_pointer += 1
            if front_val == target_val and front_stack[-len(target):] == target:
                #일치하는 문자를 스택에서 제거
                for _ in range(len(target)):
                    del front_stack[-1]
                front_val = -1
                break

        # 뒤에서 일치하는 문자열 처리
        while front_pointer <= back_pointer:
            back_stack.append(text[back_pointer])   #스택에 글자를 하나 넣음
            if len(back_stack) >= len(target):
                if back_val == -1:
                    back_val = rabinkarp(back_stack[-len(target):])
                else:
                    back_val = ((back_val - back_stack[-len(target) - 1]) >> 1) + back_stack[-1] * (1 << (len(target) - 1))
            back_pointer -= 1
            if back_val == reversed_target_val and back_stack[-len(target):] == reverse_target:
                #일치하는 문자를 스택에서 제거
                for _ in range(len(target)):
                    del back_stack[-1]
                back_val = -1
                break

    front_val = -1
    #back큐에 있는 모든 문자를 front큐로 옮김
    while back_stack:
        item = back_stack.pop()
        front_stack.append(item)

        # 앞에서 일치하는 문자열 처리
        if len(front_stack) >= len(target):
            if front_val == -1:
                front_val = rabinkarp(front_stack[-len(target):])
            else:
                front_val = ((front_val - front_stack[-len(target) - 1]) >> 1) + front_stack[-1] * (1 << (len(target) - 1))
        if front_val == target_val and front_stack[-len(target):] == target:
            for _ in range(len(target)):
                del front_stack[-1]
            front_val = -1

    for i in range(len(front_stack)):
        front_stack[i] = chr(front_stack[i] + 96)   #아스키코드값을 문자열로 바꿔줌

    print("".join(front_stack).rstrip())