# https://programmers.co.kr/learn/courses/30/lessons/49191

from queue import PriorityQueue


def solution(n, results):
    floyd_table = [[False] * n for _ in range(n)]
    sub_cnt = [-1] * n
    answer = 0
    queue = PriorityQueue()
    cnt_dict = dict()

    for row in range(n):
        floyd_table[row][row] = True

    for winner, loser in results:
        floyd_table[loser - 1][winner - 1] = True

    # 플로이드 와샬
    for intermediate in range(n):
        for row in range(n):
            for col in range(n):
                floyd_table[row][col] = (floyd_table[row][intermediate] and floyd_table[intermediate][col]) or \
                                        floyd_table[row][col]

    for col in range(n):
        for row in range(n):
            sub_cnt[col] += floyd_table[row][col]
        queue.put(-sub_cnt[col])
        cnt_dict[sub_cnt[col]] = cnt_dict.get(sub_cnt[col], 0) + 1

    for seq in range(n - 1, -1, -1):
        data = -queue.get()

        if cnt_dict[data] > 1:
            continue
        if data == seq:
            answer += 1

    return answer


if __name__ == '__main__':
    solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])  # 2
    solution(7, [[1, 2], [1, 5], [2, 3], [3, 4], [3, 6], [4, 7], [5, 3], [6, 7]])  # 3
