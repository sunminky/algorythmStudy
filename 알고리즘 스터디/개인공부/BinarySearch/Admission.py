#https://programmers.co.kr/learn/courses/30/lessons/43238
#https://www.acmicpc.net/problem/3079

def solution(n, times):
    max_time = 1000000000 * n + 1   #최악의 시간인 경우
    min_time = 1    #최선의 시간인 경우

    while min_time < max_time:
        middle_time = (max_time + min_time) // 2

        #정해진 시간내 심사관들이 처리할 수 있는 사람들의 총 합 >= 처리해야 할 사람
        if sum([middle_time // t for t in times]) >= n:
            max_time = middle_time
        else:
            min_time = middle_time + 1

    return (min_time + max_time) // 2


if __name__ == '__main__':
    solution(6, [7, 10])    #28
    solution(10, [1, 5])    #9
    solution(1, [1])  #1