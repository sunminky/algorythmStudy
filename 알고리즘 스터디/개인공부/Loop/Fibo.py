#https://programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    answer = [0 for _ in range(n + 1)]
    answer[0], answer[1] = 0, 1

    for i in range(2, n + 1):
        answer[i] = answer[i - 1] + answer[i - 2]

    return answer[n] % 1234567