# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=5&contestProbId=AWcPjE1qAFkDFAU4&categoryId=AWcPjE1qAFkDFAU4&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=5&pageSize=10&pageIndex=4
def solution(n) -> list:
    # '(' 와 ')'의 남은 개수에 따른 경우의 수 저장
    memo = [[0 if row != 0 else 1] * (n + 1) for row in range(n + 1)]
    # '('가 0개 남은 경우는 남은 ')'을 모두 쓰는 경우 1가지 밖에 없음

    for row in range(1, n + 1):
        for col in range(row, n + 1):
            memo[row][col] = memo[row - 1][col] + memo[row][col - 1]

    return memo


if __name__ == '__main__':
    memo = solution(100)

    for tc in range(1, int(input()) + 1):
        half_width, target = map(int, input().split())
        width = half_width * 2

        if memo[half_width][half_width] < target:
            print(f"#{tc} )(")
            continue

        answer = ['(']
        r_open = l_open = 0

        l_open += 1
        while r_open + l_open != width:
            flag = True

            if l_open + 1 <= half_width:
                if memo[half_width - l_open - 1][half_width - r_open] >= target:
                    l_open += 1
                    answer.append('(')
                    flag = False

            if flag:
                target -= memo[max(half_width - l_open - 1, 0)][half_width - r_open]
                r_open += 1
                answer.append(')')

        print(f"#{tc} {''.join(answer)}")
