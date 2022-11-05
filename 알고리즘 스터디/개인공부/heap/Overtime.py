# https://school.programmers.co.kr/learn/courses/30/lessons/12927
import heapq


def solution(n, works):
    answer = 0
    queue = []

    for e in works:
        heapq.heappush(queue, -e)

    while queue and n:
        _work = -heapq.heappop(queue) - 1
        heapq.heappush(queue, -_work)
        n -= 1

    for e in queue:
        answer += max(-e, 0) ** 2

    return answer
