# https://programmers.co.kr/learn/courses/30/lessons/64062
# 슬라이딩 윈도우, 최소값 큐


from collections import deque


def solution(stones, k):
    stepping_cnt = [0] * (len(stones) + 1)  # 모든 징검다리의 개수 + 도착 지점에 있는 땅
    sliding_window = deque()  # 슬라이딩 윈도우
    max_queue = deque()  # 최대값 저장 큐

    sliding_window.append(200000000)  # 징검다리를 밟기전 땅의 숫자(무한번 밟기 가능)
    max_queue.append(200000000)
    stones.append(200000000)    # 징검다리를 건넌 후 땅의 숫자(무한번 밟기 가능)

    for seq, stone in enumerate(stones):
        # 슬라이딩 윈도우에 원소 추가
        if len(sliding_window) > k:
            del_stone = sliding_window.popleft()

            if del_stone == max_queue[0]:
                max_queue.popleft()

        stepping_cnt[seq] = min(max_queue[0], stones[seq])

        # 최대큐에서 자기보다 작은 값은 제거
        while max_queue:
            if max_queue[-1] < stepping_cnt[seq]:
                max_queue.pop()
            else:
                break

        # 현재 돌 추가
        max_queue.append(stepping_cnt[seq])
        sliding_window.append(stepping_cnt[seq])

    return stepping_cnt[-1]     # 도착지 땅에 발을 디딜수 있는 횟수 반환


if __name__ == '__main__':
    result = solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)
    print(result)
    result = solution([i for i in range(200000, 0, -1)], 200000)
    print(result)
