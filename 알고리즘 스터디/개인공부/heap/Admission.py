#https://programmers.co.kr/learn/courses/30/lessons/43238

from queue import PriorityQueue

def solution(n, times):
    c_time = 0
    cnt = n
    queue = PriorityQueue()

    for _time in times:
        queue.put((_time, _time))

    while cnt != 0:
        c_time, unit = queue.get()
        cnt -= 1
        queue.put((c_time+unit, unit))

    return c_time

if __name__ == '__main__':
    solution(6, [7, 10])    #28