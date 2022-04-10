# https://www.acmicpc.net/problem/1946
import sys

if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        n_candidate = int(sys.stdin.readline())
        rank = [list() for _ in range(2)]
        answer = 0
        cur_idx = n_candidate

        for seq in range(n_candidate):
            _rank1, _rank2 = map(int, sys.stdin.readline().split())
            rank[0].append((seq + 1, _rank1))
            rank[1].append((seq + 1, _rank2))

        rank[0].sort(key=lambda x: x[1])
        rank[1].sort(key=lambda x: x[1])

        rank_dict = dict(zip((e[0] for e in rank[1]), range(n_candidate)))

        for seq in range(n_candidate):
            if rank_dict[rank[0][seq][0]] < cur_idx:
                cur_idx = rank_dict[rank[0][seq][0]]
                answer += 1

        print(answer)
