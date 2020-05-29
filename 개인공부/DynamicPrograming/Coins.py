arr =[] #동전 개수 저장
unit = (1,4,7,13,28,52,91,365)

def calcCases(fee):
    min = 0 #최소동전개수로 만들수 있는 가장 큰 수의 인덱스 저장
    for i in range(fee):
        if i+1 in unit: #동전 하나로 만들수 있는 금액이라면 패쓰
            min = i
            continue
        arr[i] = arr[min] + arr[i - min - 1]
    return arr[fee-1]

def calcCase2(fee):
    min = 0
    for seq,value in enumerate(reversed(unit)): #목표금액보다 작은 금액중 동전 한개로 만들수 있는 가장 큰 액수 구함, 그 동전은 반드시 포함되야 함
        if fee >= value:
            min = len(unit) - 1 - seq
            break
    arr[fee - 1] = getValue(unit[min] - 1) + getValue(fee - unit[min] - 1)
    return arr[fee-1]

def getValue(index):
    if index < 0:
        return 0
    if arr[index] == 0:
        return calcCase2(index+1)   #index+1은 계산해야 할 남은 금액
    return arr[index]

if __name__ == '__main__':
    fee = int(input("입력 :"))
    arr = [0 for i in range(fee)]

    for value in unit:  #동전 하나로 만들수 있는 금액은 개수를 1로 설정
        if value > fee:
            break
        arr[value-1] = 1
    answer = calcCase2(fee)
    print(answer)