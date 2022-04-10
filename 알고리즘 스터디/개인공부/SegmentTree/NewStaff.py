# https://www.acmicpc.net/problem/1946
import sys

if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        cur_idx = n_candidate = int(sys.stdin.readline())
        rank = [[0] * n_candidate for _ in range(2)]
        answer = 0

        for seq in range(n_candidate):
            _rank1, _rank2 = map(int, sys.stdin.readline().split())
            rank[0][_rank1 - 1] = rank[1][_rank2 - 1] = seq

        rank_dict = dict(zip(rank[1], range(n_candidate)))

        for e in rank[0]:
            if rank_dict[e] < cur_idx:
                cur_idx = rank_dict[e]
                answer += 1

        print(answer)
