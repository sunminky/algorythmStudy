#https://level.goorm.io/exam/43122/merge-sort/quiz/1
def mergeSort(array):
    if len(array) <= 1 :
        return array

    arr1 = mergeSort(array[:len(array)//2]) #반으로 쪼개서 앞에 것에 대해 다시 쪼개기
    arr2 = mergeSort(array[len(array)//2:]) #반으로 쪼개서 뒤에 것에 대해 다시 쪼개기

    ###정렬 수행###
    ret = mySort(arr1, arr2)
    return ret

def mySort(arr1, arr2): #정렬을 수행
    i = 0
    j = 0
    ret = []

    while i < len(arr1) and j < len(arr2):  
        if arr1[i] < arr2[j]:   #앞에서 부터 하나씩 비교하면서 정렬
            ret.append(arr1[i])
            i += 1
        else:
            ret.append(arr2[j])
            j += 1
    ret += arr1[i:] + arr2[j:]  #먼저 정렬이 다 끝난 배열이 있을 경우 남은 배열을 뒤에 붙여줌
    return ret

if __name__ == "__main__":
    _ = input()
    elements = list(map(int,input().split()))
    ret = mergeSort(elements)
    print(" ".join([str(i) for i in ret]) + " ")    #출력할때 뒤에 빈 칸 하나 붙어있음