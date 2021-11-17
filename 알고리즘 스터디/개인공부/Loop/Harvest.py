# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GLXqKAWYDFAXB
if __name__ == '__main__':
    for tc in range(int(input())):
        width = int(input())
        field = [[int(e) for e in input()] for _ in range(width)]

        print(f"#{tc + 1} {sum([sum(field[row][width // 2 - row: width // 2 + 1 + row]) + sum(field[width - 1 - row][width // 2 - row: width // 2 + 1 + row]) for row in range(width // 2 + 1)]) - sum(field[width // 2])}")
