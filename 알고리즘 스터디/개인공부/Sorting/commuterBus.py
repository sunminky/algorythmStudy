# https://programmers.co.kr/learn/courses/30/lessons/17678
from collections import deque


# HH:MM 을 00:00 경과 분으로 변환
def trans(time):
    hour, minute = map(int, time.split(':'))

    return hour * 60 + minute


def solution(n, t, m, timetable):
    answer = 0
    queue = deque(sorted(map(trans, timetable)))
    last = queue[0]

    for bus in range(n):
        remain = m

        while queue and remain and queue[0] <= 540 + bus * t:
            remain -= 1
            last = queue.popleft()

        # 막차
        if bus == n - 1:
            answer = 540 + bus * t if remain else last - 1

    return f"{(answer // 60):02}:{(answer % 60):02}"


if __name__ == '__main__':
    solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"])  # "09:00"
    solution(2, 10, 2, ["09:10", "09:09", "08:00"])  # "09:09"
    solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"])  # "08:59"
    solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"])  # "00:00"
    solution(1, 1, 1, ["23:59"])  # "09:00"
    solution(10, 60, 45,
             ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
              "23:59",
              "23:59", "23:59", "23:59", "23:59"])  # "18:00"
