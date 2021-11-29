# https://programmers.co.kr/learn/courses/30/lessons/42584
def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for seq, value in enumerate(prices):
        while stack and stack[-1][1] > value:
            _seq, _ = stack.pop()
            answer[_seq] = seq - _seq

        stack.append((seq, value))

    while stack:
        _seq, _ = stack.pop()
        answer[_seq] = (len(prices) - 1) - _seq

    return answer


if __name__ == '__main__':
    solution([1, 2, 3, 2, 3])  # [4, 3, 1, 1, 0]
