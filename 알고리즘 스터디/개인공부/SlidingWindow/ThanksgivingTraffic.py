# https://programmers.co.kr/learn/courses/30/lessons/17676
import heapq


def solution(lines):
    answer = 0
    offer = []
    time_slice = []

    for e in lines:
        _, end_time, cost = e.split()
        e_times = tuple(map(float, end_time.split(':')))
        end_time = e_times[0] * 3600 + e_times[1] * 60 + e_times[2]
        start_time = end_time - float(cost[:-1]) + 0.001
        heapq.heappush(offer, (start_time, end_time))

    while offer:
        start_time, end_time = heapq.heappop(offer)

        # 현재 로그와 1초이상 차이나는 경우
        while time_slice:
            if time_slice[0] + 1 <= start_time:
                heapq.heappop(time_slice)
            break

        heapq.heappush(time_slice, end_time)
        answer = max(answer, len(time_slice))

    return answer


if __name__ == '__main__':
    solution(["2016-09-15 20:59:57.421 0.351s",
              "2016-09-15 20:59:58.233 1.181s",
              "2016-09-15 20:59:58.299 0.8s",
              "2016-09-15 20:59:58.688 1.041s",
              "2016-09-15 20:59:59.591 1.412s",
              "2016-09-15 21:00:00.464 1.466s",
              "2016-09-15 21:00:00.741 1.581s",
              "2016-09-15 21:00:00.748 2.31s",
              "2016-09-15 21:00:00.966 0.381s",
              "2016-09-15 21:00:02.066 2.62s"])  # 7
    solution(["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"])  # 1
    solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"])  # 2
    solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"])  # 1
    solution(["2016-09-15 23:59:59.999 0.001s"])  # 1
    solution(["2016-09-15 00:00:00.000 3s"])  # 1
    solution(["2016-09-15 00:00:00.500 0.5s",
              "2016-09-15 00:00:00.600 0.6s",
              "2016-09-15 00:00:00.700 0.7s",
              "2016-09-15 00:00:00.900 0.9s",
              "2016-09-15 00:00:01.000 1.0s",
              "2016-09-15 00:00:01.100 1.1s",
              "2016-09-15 00:00:03.000 3s",
              "2016-09-15 00:00:03.001 3s"])    # 8
