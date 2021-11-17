# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14Rq5aABUCFAYi&categoryId=AV14Rq5aABUCFAYi&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1
def get_longest(field) -> int:
    max_len = 1

    for line in field:
        cost = [[0 if col != row else 1 for col in range(100)] for row in range(100)]

        for col in range(1, 100):
            for row in range(100 - col):
                if line[row] == line[row + col]:
                    if row + 1 > row + col - 1 or cost[row + 1][row + col - 1]:
                        cost[row][row + col] = cost[row + 1][row + col - 1] + 2
                        max_len = max(max_len, cost[row][row + col])

    return max_len


if __name__ == '__main__':
    for tc in range(1, 11):
        input()  # 필요없음

        answer = 1
        field = [input().rstrip() for _ in range(100)]

        # 가로 팰린드롬 구하기
        answer = max(answer, get_longest(field))

        # 세로 팰린드롬 구하기
        new_field = [[field[col][row] for col in range(100)] for row in range(100)]
        answer = max(answer, get_longest(new_field))

        print(f"#{tc} {answer}")
