arr = (31,-41,59,26,-53,58,97,-93,-23,84)
#arr = (-1,-2,-3,-4,-5)   #-15
#arr = (1,2,3,4,5)   #15

def getMinIndex(arr):
    min = arr[0]
    index = 0;
    for seq,value in enumerate(arr[1:]):
        if arr[seq] < min:
            min = arr[seq]
            index = seq
    return index

if __name__ == '__main__':
    forwardSum = [0 for i in range(len(arr))]
    backwardSum = forwardSum.copy()
    forwardSum[0] = arr[0]  #앞에서 더했을 경우 합을 저장
    backwardSum[0] = arr[-1]    #뒤에서 더했을 경우 합을 저장
    answer = 0

    for seq,value in enumerate(arr[1:]):    #앞에서 부터 더함
        forwardSum[seq+1] = forwardSum[seq] + value 
    for seq,value in enumerate(reversed(arr[:-1])): #뒤에서 부터 더함
        backwardSum[seq + 1] = backwardSum[seq] + value

    answer = forwardSum[-1]

    forwardMinIndex = getMinIndex(forwardSum)

    if forwardSum[forwardMinIndex] < 0:
        answer = answer - forwardSum[forwardMinIndex]


    backwardMinIndex = getMinIndex(backwardSum[:len(backwardSum)-1-forwardMinIndex])
    if backwardSum[backwardMinIndex] < 0:
        answer = answer - backwardSum[backwardMinIndex]

    print(answer)
