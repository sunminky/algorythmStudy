# https://programmers.co.kr/learn/courses/30/lessons/12902

def solution(n):
    acc = 1     # 0 ~ n까지 누적합
    past = 1   # 이전 너비의 경우의 수

    for _ in range(0, n, 2):
        past = calc = (acc * 2 + past) % 1000000007    # 현재 너비일 때 경우의 수
        acc = (acc + calc) % 1000000007

    return past


if __name__ == '__main__':
    solution(6)
    solution(8)
    solution(10)
    solution(12)
    solution(14)
    solution(16)
    solution(18)
    solution(5000)
