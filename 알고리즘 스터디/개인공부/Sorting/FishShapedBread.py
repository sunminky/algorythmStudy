# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV5LsaaqDzYDFAXc&categoryId=AV5LsaaqDzYDFAXc&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=CCPP&select-1=3&pageSize=10&pageIndex=2
if __name__ == '__main__':
    for tc in range(int(input())):
        _, timecomplexity, output = map(int, input().split())
        sold = 0
        answer = True
        customers = sorted(map(int, input().split()))

        for c in customers:
            if c // timecomplexity * output < sold + 1:
                answer = False
                break
            sold += 1

        print(f"#{tc + 1} {'Possible' if answer else 'Impossible'}")
