def rec(arr):
    arrlen = len(arr) // 2
    if arr[arrlen] == arrlen:   #인덱스랑 데이터가 같은 경우
        return arrlen           #그 인덱스 반환
    else:
        if arr[arrlen] > arrlen:    #인덱스보다 데이터가 더 큰 경우
            return rec(arr[:arrlen])    #아래쪽을 탐색
        else:   #인덱스보다 데이터가 더 작은 경우
            return rec(arr[arrlen+1:])  #위쪽을 탐색

if __name__ == "__main__":
    arr = [-10,1,2,4,9,10,11,12]
    arr = [-5, -3, -1, 2, 4, 5, 6, 10]
    arr = [0,1,2,3,4,5]
    index = rec(arr)
    for i in range(index,len(arr)): #주변 탐색, index ~ 배열 끝
        if arr[i] == i:
            print(arr[i])
        else:
            break
    for i in range(index-1,-1,-1):  #주변 탐색, 배열처음 ~ index
        if arr[i] == i:
            print(arr[i])
        else:
            break