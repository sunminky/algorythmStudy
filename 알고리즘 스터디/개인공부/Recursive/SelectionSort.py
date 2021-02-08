import random

array = [i+1 for i in range(20)]
random.shuffle(array)

def recursive(indicator):
    if indicator == len(array): #리스트 전체를 다 탐색함
        return;
    else:
        minIndex = array.index(min(array[indicator:]))  #아직 정렬 안된 리스트중 최소값 찾음
        array[indicator],array[minIndex] = array[minIndex],array[indicator] #찾은 최소값과 배열의 첫 자리값 와 교환
        recursive(indicator+1)  #입력값을 줄여서 reduction

if __name__ == "__main__":
    recursive(0)
    print(array)