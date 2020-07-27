#https://programmers.co.kr/learn/courses/30/lessons/12899?language=python3#_=_

def solution(n):
    seq = ['1', '2', '4']

    if n == 0:
        return ""
    if n % 3 == 0:
        return solution(n // 3 - 1) + seq[2]
    else:
        return solution(n // 3) + seq[n % 3 - 1]

if __name__ == '__main__':
    for i in range(1,51):
        print("{0:<4}".format(solution(i)), end=" ")
        if i % 10 == 0:
            print()