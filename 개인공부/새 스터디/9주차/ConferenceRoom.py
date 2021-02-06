#https://www.acmicpc.net/problem/1931

import sys

if __name__ == '__main__':
    conference = []

    for _ in range(int(sys.stdin.readline())):
        conference.append(tuple(map(int, sys.stdin.readline().split())))    #s_time, e_time
    conference.sort(key=lambda x:(x[1], x[0]))

    cur_e_time = conference[0][1]
    answer = 1

    for s_time, e_time in conference[1:]:
        if s_time >= cur_e_time and s_time <= e_time:
            cur_e_time = e_time
            answer += 1

    print(answer)

## 반례 ##
'''
3
7 7
8 8
7 8

answer : 3
'''