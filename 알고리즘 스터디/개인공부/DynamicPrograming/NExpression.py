# https://programmers.co.kr/learn/courses/30/lessons/42895


def solution(N, number):
    answer = -1
    store = [{int("0" + str(N) * (i))} for i in range(10)]

    for i in range(1, 9):
        for j in range(1, i):
            #s[j] ? s[i - j], j개 쓴 경우 (+, -, *, //) i-j개 쓴 경우 
            for e1 in store[j]:
                for e2 in store[i - j]:
                    store[i].add(e1 + e2)
                    store[i].add(e1 - e2)
                    store[i].add(e1 * e2)
                    if e2 != 0:
                        store[i].add(e1 // e2)

        if number in store[i]:
            answer = i
            break

    return answer


if __name__ == '__main__':
    solution(5, 12) #4
    solution(2, 11) #3