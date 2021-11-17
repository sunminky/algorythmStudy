# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&problemLevel=3&contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=CCPP&select-1=3&pageSize=10&pageIndex=1
if __name__ == '__main__':
    for tc in range(int(input())):
        answer = 0
        criteria = -1

        input()
        for e in reversed(input().split()):
            e = int(e)

            if e > criteria:
                criteria = e

            answer += max(criteria - e, 0)

        print(f"#{tc + 1} {answer}")
