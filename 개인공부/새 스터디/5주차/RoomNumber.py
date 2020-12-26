def betweenValue(lst, limit):   #lst 안의 원소중 limit 보다 작은 수중 가장 큰 수 반환
    ret = 0
    for i in lst:
        if i > limit:
            break
        ret = i

    return ret


if __name__ == '__main__':
    input() #가게에서 파는 숫자의 개수 N, 필요없음
    stock = list(map(int, input().split()))
    balance = int(input())
    lst = [dict(zip(stock, range(len(stock))))] #키 : 만든 숫자 가격, 값 : 만든 숫자
    step = 1
    maxValue = lst[0][betweenValue(stock, balance)]

    while balance - min(lst[-1].keys()) >= min(lst[0].keys()):
        tmp = dict()
        
        #앞에다가 파는 숫자를 하나씩 붙여서 자리수를 늘림
        for i in lst[0].keys():
            for j in lst[-1].keys():
                if i + j <= balance:
                    tmp[i + j] = lst[0][i] * pow(10, step) + lst[-1][j]

        step += 1
        lst.append(tmp)
        if max(tmp.values()) > maxValue:
            maxValue = max(tmp.values())

    print(maxValue)