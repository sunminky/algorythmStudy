#https://programmers.co.kr/learn/courses/30/lessons/72412

def solution(info, query):
    table = []  #프로그래밍언어(int), 직군(int), 경력(int), 소울푸드(int), 점수(int)
    language = {'cpp' : 0, 'java' : 1, 'python' : 2}
    part = {'backend' : 0, 'frontend' : 1}
    career = {'junior' : 0, 'senior' : 1}
    food = {'chicken' : 0, 'pizza' : 1}
    conditions = (language, part, career, food)

    for seq, profile in enumerate(info):
        data = profile.split()
        table.append((language[data[0]], part[data[1]], career[data[2]], food[data[3]], int(data[4])))

    for q in query:
        raw_query = q.split()
        request = raw_query[::2]    #언어, 직군, 경력, 음식, 점수
        request.append(raw_query[-1])

        fulfill = []

    answer = []
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