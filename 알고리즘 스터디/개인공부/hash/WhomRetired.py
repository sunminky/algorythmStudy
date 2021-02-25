#https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3

def solution(participant, completion):
    answer = dict()

    for runner in participant:
        if not answer.get(runner, False):
            answer[runner] = 1
        else:
            answer[runner] += 1

    for runner in completion:
        answer[runner] -= 1

    for key in answer.keys():
        if answer[key] != 0:
            return key

if __name__ == '__main__':
    solution(['leo', 'kiki', 'eden'], ['eden', 'kiki'])
    solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav'])