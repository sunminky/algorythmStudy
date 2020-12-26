if __name__ == '__main__':
    input() #가게에서 파는 숫자의 개수 N, 필요없음
    stock = list(map(int, input().split()))
    balance = int(input())
    lst = [dict(zip(stock, range(len(stock))))]
    step = 1
    maxValue = -1

    for s in lst[0].keys():
        if s <= balance:
            maxValue = lst[0][s]

    while balance - min(lst[-1].keys()) >= min(lst[0].keys()):
        tmp = dict()

        for i in lst[0].keys():
            for j in lst[-1].keys():
                if i + j <= balance:
                    tmp[i + j] = lst[0][i] * pow(10, step) + lst[-1][j]

        step += 1
        lst.append(tmp)
        if max(tmp.values()) > maxValue:
            maxValue = max(tmp.values())

    print(maxValue)