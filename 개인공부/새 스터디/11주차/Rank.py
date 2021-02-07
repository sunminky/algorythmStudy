#https://programmers.co.kr/learn/courses/30/lessons/72412

from bisect import bisect_left
from itertools import product

def solution(info, query):
    answer = [] #정답 저장
    language = {'cpp' : [0], 'java' : [1], 'python' : [2], '-' : [0, 1, 2]}
    part = {'backend' : [0], 'frontend' : [1], '-' : [0, 1]}
    career = {'junior' : [0], 'senior' : [1], '-' : [0, 1]}
    food = {'chicken' : [0], 'pizza' : [1], '-' : [0, 1]}
    #그룹별로 저장, ex) group[0][0][0][0] = cpp쓰고 backend이고 junior이고 chicken 좋아함
    group = [[[[[] for _ in range(len(food)-1)] for _ in range(len(career)-1)] for _ in range(len(part)-1)] for _ in range(len(language)-1)]

    for _info in info:
        data = _info.split()
        group[language[data[0]][0]][part[data[1]][0]][career[data[2]][0]][food[data[3]][0]].append(int(data[4]))

    #그룹별로 저장한 리스트 정렬
    for p in product(range(len(language)-1), range(len(part)-1), range(len(career)-1), range(len(food)-1)):
        group[p[0]][p[1]][p[2]][p[3]].sort()

    #쿼리 전처리
    for q in query:
        cnt = 0
        raw_query = q.split()
        r_l, r_p, r_c, r_f = raw_query[::2]    #언어, 직군, 경력, 음식, 점수
        r_s = int(raw_query[-1])

        #카티션 프로덕트
        for p in product(language[r_l], part[r_p], career[r_c], food[r_f]):
            # 그룹별 리스트의 길이 - 요구하는 점수보다 높은 점수가 제일 처음 나오는 위치 = 요구하는 점수보다 높은 지원자들의 개수
            cnt += len(group[p[0]][p[1]][p[2]][p[3]]) - bisect_left(group[p[0]][p[1]][p[2]][p[3]], r_s)

        answer.append(cnt)

    return answer

if __name__ == '__main__':
    solution(["java backend junior pizza 150",
              "python frontend senior chicken 210",
              "python frontend senior chicken 150",
              "cpp backend senior pizza 260",
              "java backend junior chicken 80",
              "python backend senior chicken 50"],
             ["java and backend and junior and pizza 100",
              "python and frontend and senior and chicken 200",
              "cpp and - and senior and pizza 250",
              "- and backend and senior and - 150",
              "- and - and - and chicken 100",
              "- and - and - and - 150"])