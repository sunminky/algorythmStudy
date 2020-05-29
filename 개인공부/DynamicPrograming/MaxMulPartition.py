if __name__ == "__main__":
    arr = [-6,12,-7,0,14,-7,5]

    maxVal = arr[0] #현재 가장 큰 곱 저장
    maxMul = arr[0] #양의 정수만 곱해져서 제일 큰 최대곱
    minMul = arr[0] #음의 정수가 곱해져서 제일 작은 최소곱

    for i in range(len(arr)):
        prevMax = maxMul    #이전 최대 곱
        prevMin = minMul    #이전 최소 곱
    
        #3가지 경우가 있다.
        '''1. 이전의 요소들 다 버리고 현재요소부터 시작
            2. 이전의 최대곱과 현재 요소를 곱함
            3. 이전의 최소곱과 현재 요소를 곱함'''
        maxMul = max(arr[i], arr[i] * prevMax, arr[i] * prevMin)
        minMul = min(arr[i], arr[i] * prevMax, arr[i] * prevMin)
        maxVal = max(maxVal, maxMul)

    answer = maxVal
    print(answer)