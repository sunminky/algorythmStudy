# https://www.acmicpc.net/problem/1253
import sys

if __name__ == '__main__':
    n_num = int(sys.stdin.readline())
    num = tuple(map(int, sys.stdin.readline().split()))
    num_dict = dict()
    answer = 0

    for seq, e in enumerate(num):
        num_dict[e] = num_dict.get(e, set())
        num_dict[e].add(seq)

    for seq1, e1 in enumerate(num):
        for seq2, e2 in enumerate(num):
            if seq1 == seq2:
                continue

            if e1 - e2 in num_dict:
                if len(num_dict[e1 - e2]) - (seq1 in num_dict[e1 - e2]) - (seq2 in num_dict[e1 - e2]) > 0:
                    answer += 1
                    break

    print(answer)
