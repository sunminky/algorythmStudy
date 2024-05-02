# https://school.programmers.co.kr/learn/courses/30/lessons/250135
def solution(h1, m1, s1, h2, m2, s2):
    start = h1 * 3600 + m1 * 60 + s1
    end = h2 * 3600 + m2 * 60 + s2
    cur_time = [(h1 % 12) * 3600 + m1 * 60 + s1, m1 * 720 + s1 * 12, s1 * 720]
    answer = 0

    while start < end:
        # 초침이 분/시침과 같은 값
        if cur_time[2] == cur_time[1] or cur_time[2] == cur_time[0]:
            answer += 1

        # 지금은 작은데 1초 뒤 커짐
        if cur_time[2] < cur_time[0] and cur_time[2] + 720 > cur_time[0] + 1:
            answer += 1

        if cur_time[2] < cur_time[1] and cur_time[2] + 720 > cur_time[1] + 12:
            answer += 1

        cur_time[0] = (cur_time[0] + 1) % 43200
        cur_time[1] = (cur_time[1] + 12) % 43200
        cur_time[2] = (cur_time[2] + 720) % 43200
        start += 1

    # 초침이 분/시침과 같은 값
    if cur_time[2] == cur_time[1] or cur_time[2] == cur_time[0]:
        answer += 1

    return answer


if __name__ == '__main__':
    solution(0, 5, 30, 0, 7, 0)  # 2
    solution(12, 0, 0, 12, 0, 30)  # 1
    solution(0, 6, 1, 0, 6, 6)  # 0
    solution(11, 59, 30, 12, 0, 0)  # 1
    solution(11, 58, 59, 11, 59, 0)  # 1
    solution(1, 5, 5, 1, 5, 6)  # 2
    solution(0, 0, 0, 23, 59, 59)  # 2852
