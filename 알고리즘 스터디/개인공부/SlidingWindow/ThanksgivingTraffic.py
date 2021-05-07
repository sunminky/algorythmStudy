# https://programmers.co.kr/learn/courses/30/lessons/17676


import heapq


def timeTosec(time):
    time_h, time_m, time_s = map(float, time.split(':'))

    return 3600 * time_h + 60 * time_m + time_s


def sort_criteria(log):
    _, src, cost = log.split()
    return timeTosec(src) - float(cost[:-1]) + 0.001


def solution(lines):
    queue = []
    answer = 0

    for log in sorted(lines, key=sort_criteria):
        _, src, cost = log.split()
        src = timeTosec(src)

        # 현재 측정시간을 범위를 벗어나는 경우 제거
        while queue:
            time_slice = queue[0]

            if time_slice + 1 <= src - float(cost[:-1]) + 0.001:
                heapq.heappop(queue)
            else:
                break
        else:
            time_slice = src

        heapq.heappush(queue, src)
        answer = max(answer, len(queue))

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
