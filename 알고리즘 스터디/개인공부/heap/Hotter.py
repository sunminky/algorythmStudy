# https://programmers.co.kr/learn/courses/30/lessons/42626
import heapq


def solution(scoville, K):
    answer = 0
    queue = list()

    for e in scoville:
        heapq.heappush(queue, e)

    while len(queue) > 1:
        s1, s2 = heapq.heappop(queue), heapq.heappop(queue)

        if s1 >= K:
            return answer

        heapq.heappush(queue, s1 + s2 * 2)
        answer += 1

    if heapq.heappop(queue) < K:
        return -1

    return answer


if __name__ == '__main__':
    solution([12, 2, 3, 9, 10, 1], 7)  # 2
    solution([0, 0, 0, 0, 0, 0], 7)  # -1
    solution([1, 1, 1, 1], 100)  # -1
