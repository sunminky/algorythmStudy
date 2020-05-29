arr = (31, -41, 59, 26, -53, 58, 97, -93, -23, 84)


# arr = (-1,-2,-3,-4,-5)   #-15
# arr = (1,2,3,4,5)   #15

def getMinIndex(arr):
    min = arr[0]
    index = 0;
    for seq, value in enumerate(arr[1:]):
        if arr[seq] < min:
            min = arr[seq]
            index = seq
    return index


if __name__ == '__main__':
    forwardSum = [0 for i in range(len(arr))]
    backwardSum = forwardSum.copy()
    forwardSum[0] = arr[0]  # 앞에서 더했을 경우 합을 저장
    backwardSum[0] = arr[-1]  # 뒤에서 더했을 경우 합을 저장
    answer = 0

    for seq, value in enumerate(arr[1:]):  # 앞에서 부터 더함
        forwardSum[seq + 1] = forwardSum[seq] + value
    for seq, value in enumerate(reversed(arr[:-1])):  # 뒤에서 부터 더함
        backwardSum[seq + 1] = backwardSum[seq] + value

    answer = forwardSum[-1]

    forwardMinIndex = getMinIndex(forwardSum)   #앞에서 더했을때 가장 작은 경우를 구함, 먹으면 손해인 구간

    if forwardSum[forwardMinIndex] < 0: #제일 작은 구간이 음수임, 먹으면 손해
        answer = answer - forwardSum[forwardMinIndex]   #그 구간을 뺌
    else:   #제일 작은 구간이 음수가 아님, 먹어도 손해는 아님
        answer

    backwardMinIndex = getMinIndex(backwardSum[:len(backwardSum) - 1 - forwardMinIndex])    #뒤에서 더했을때 가장 작은 경우를 구함, 먹으면 손해인 구간
    
    if backwardSum[backwardMinIndex] < 0:   #제일 작은 구간이 음수임, 먹으면 손해
        answer = answer - backwardSum[backwardMinIndex] #그 구간을 뺌
    else:   #제일 작은 구간이 음수가 아님, 먹어도 손해는 아님
        answer

    print(answer)
