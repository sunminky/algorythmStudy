# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AXmwOSJaSNIDFARX&categoryId=AXmwOSJaSNIDFARX&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=1
if __name__ == '__main__':
    for tc in range(int(input())):
        height, width = map(int, input().split())
        field = [list(input().rstrip().strip()) for _ in range(height)]
        answer = True

        for row in range(height):
            for col in range(width):
                if field[row][col] == '.':
                    continue

                answer &= col + 1 < width and row + 1 < height

                if answer is False:
                    break

                answer &= field[row][col + 1] == '#'
                answer &= field[row + 1][col] == '#'
                answer &= field[row + 1][col + 1] == '#'

                if answer is False:
                    break

                field[row][col] = '.'
                field[row][col + 1] = '.'
                field[row + 1][col] = '.'
                field[row + 1][col + 1] = '.'

            if answer is False:
                break

        print(f"#{tc + 1} {'YES' if answer else 'NO'}")
