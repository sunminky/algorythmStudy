# https://www.acmicpc.net/problem/1339
import operator
import sys

if __name__ == '__main__':
    digit_cnt = [dict() for _ in range(8)]  # 자리수별 알파벳 등장횟수 저장
    alphabet_dict = dict()  # 알파벳별 숫자값 저장
    num = [sys.stdin.readline().rstrip() for _ in range(int(sys.stdin.readline().rstrip()))]

    # 자리수 별 알파벳 등장횟수 저장
    for _num in num:
        for i in range(len(_num)):
            digit_cnt[-i - 1][_num[-i - 1]] = digit_cnt[-i - 1].get(_num[-i - 1], 0) + 1

    # 낮은 자리수에서 등장한 알파벳의 가중치를 상위 자리수에 더해줌
    for i in range(len(digit_cnt) - 1):
        if digit_cnt[-i - 2]:
            for e in digit_cnt[-i - 1]:
                digit_cnt[-i - 2][e] = digit_cnt[-i - 2].get(e, 0) + digit_cnt[-i - 1][e] / 10

    # 높은 자리부터 등장 빈도가 높은 알파벳을 큰 숫자로 바꿔줌
    for e in digit_cnt:
        for key, _ in sorted(e.items(), key=operator.itemgetter(1), reverse=True):   # 딕셔너리 value로 정렬
            if alphabet_dict.get(key, False) is False:
                alphabet_dict[key] = 9 - len(alphabet_dict)

    print(sum([int("".join(map(lambda x: str(alphabet_dict[x]), e))) for e in num]))
