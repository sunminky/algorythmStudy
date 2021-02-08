array = [10,9,8,7,6,5,4,3,2,1]

def recursive(arr):
    if len(arr) <= 2:	#배열의 길이가 1이거나 2이면
        return sum(arr) #총합을 구해서 리턴한다
    else:   #배열의 길이가 2보다 크면 계속 입력값을 줄여서 reduction 할거임
        return recursive(arr[:len(arr)//2]) + recursive(arr[len(arr)//2:])

if __name__ == "__main__":
    result = recursive(array)
    print(result)