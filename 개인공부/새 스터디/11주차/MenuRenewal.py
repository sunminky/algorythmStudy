#https://programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations

def solution(orders, course):

    dictionary = [dict() for _ in range(11)]
    maxValue = [-1 for _ in range(11)]
    answer = []

    for c in course:
        for o in orders:
            if len(o) >= c:
                for s in combinations(sorted(o), c):
                    if not dictionary[c].get("".join(s), False):
                        dictionary[c]["".join(s)] = 1
                    else:
                        dictionary[c]["".join(s)] += 1
                    if dictionary[c]["".join(s)] > maxValue[c]:
                        maxValue[c] = dictionary[c]["".join(s)]

    for c in course:
        if maxValue[c] < 2:
            continue
        for item in dictionary[c].keys():
            if maxValue[c] == dictionary[c][item]:
                answer.append(item)

    answer.sort()
    print(answer)
    return answer

if __name__ == '__main__':
    solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])
    solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5])
    solution(["XYZ", "XWY", "WXA"], [2,3,4])