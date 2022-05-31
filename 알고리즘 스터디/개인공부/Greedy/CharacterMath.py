# https://www.acmicpc.net/problem/1339
import sys

if __name__ == '__main__':
    words = [sys.stdin.readline().rstrip() for _ in range(int(sys.stdin.readline()))]
    count_dict = [dict() for _ in range(9)]
    alpha_dict = dict()
    answer = 0

    for e in words:
        for seq, ch in enumerate(e):
            count_dict[len(count_dict) - len(e) + seq][ch] = count_dict[len(count_dict) - len(e) + seq].get(ch, 0) + 1

    for i in range(len(count_dict) - 1, 0, -1):
        for key in count_dict[i]:
            count_dict[i - 1][key] = count_dict[i - 1].get(key, 0) + count_dict[i][key] / 10
            count_dict[i][key] %= 10

    table = sorted(count_dict[0].items(), key=lambda x: x[1], reverse=True)

    for i in range(min(10, len(table))):
        alpha_dict[table[i][0]] = str(9 - i)

    for word in words:
        answer += int("".join((map(lambda x: alpha_dict[x], word))))

    print(answer)
