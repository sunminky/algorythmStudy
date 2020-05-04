import random

array = [i+1 for i in range(20)]
random.shuffle(array)
print("list : ",array)

def recursive(indicator):   #0 ~ 인디케이터 : 정렬 안된 구간
    global array

    if indicator == 1:  #정렬해야 할게 두개 남음
        maxIndex = array.index(max(array[:indicator+1]))

        if maxIndex != indicator:   #정렬 안된 상태
            arr2 = flip(indicator, array)  # 전체 뒤집기
            arr2.extend(array[indicator + 1:])  # 뒤집은것과 안뒤집은것 합체
            array = arr2
        return;

    maxIndex = array.index(max(array[:indicator+1]))

    if maxIndex != indicator:   #정렬 안된 상태
        arr2 = flip(maxIndex,array)     #0 ~ 제일큰 판 까지 뒤집음
        arr2.extend(array[maxIndex+1:]) #뒤집은것과 안뒤집은것 합체
        arr2 = flip(indicator,arr2) #전체 뒤집기
        arr2.extend(array[indicator + 1:])  #뒤집은것과 안뒤집은것 합체
        array = arr2

    recursive(indicator - 1)    #입력값을 줄여서 reduction

def flip(maxIndex,arr):
    return list(reversed(arr[:maxIndex+1]))

if __name__ == "__main__":
    recursive(len(array)-1)
    print("result : ",array)