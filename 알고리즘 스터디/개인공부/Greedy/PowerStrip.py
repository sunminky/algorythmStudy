import sys
import heapq

if __name__ == '__main__':
    capacity, _ = map(int, sys.stdin.readline().split())
    plug_seq = [[e, 0] for e in map(int, sys.stdin.readline().split())]
    worth_cnt = [len(plug_seq)] * len(plug_seq)  # 미래에 자신이 사용되는 시점
    in_queue = [[-1, False] for _ in range(len(plug_seq))]  # [가장 가깝게 사용될 미래 시점, 멀티탭에 꽂혀있는지 체크]
    remain = capacity  # 멀티탭에 남은 자리수
    queue = []
    answer = 0

    for i in range(len(plug_seq) - 1, -1, -1):
        plug_seq[i][1] = worth_cnt[plug_seq[i][0] - 1]
        worth_cnt[plug_seq[i][0] - 1] = i

    for electonic, w_cnt in plug_seq:
        # 이미 멀티탭에 들어가 있는 경우
        if in_queue[electonic - 1][1]:
            in_queue[electonic - 1][0] = w_cnt
            heapq.heappush(queue, (-w_cnt, electonic))
            continue

        # 멀티탭에 자리가 있는 경우
        if remain:
            remain -= 1
            in_queue[electonic - 1][1] = True
            in_queue[electonic - 1][0] = w_cnt
            heapq.heappush(queue, (-w_cnt, electonic))
            continue

        # 자리가 없는 경우
        # pop
        while queue:
            _w_cnt, _electonic = heapq.heappop(queue)

            if in_queue[_electonic - 1][1]:
                remain += 1
                in_queue[_electonic - 1][1] = False
                answer += 1
                break

        remain -= 1
        in_queue[electonic - 1][1] = True
        in_queue[electonic - 1][0] = w_cnt
        heapq.heappush(queue, (-w_cnt, electonic))

    print(answer)
