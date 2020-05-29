arr = [1,2,4]   #각 배열의 인덱스는 그 인덱스에 해당하는 숫자+1의 표현가능한 가지수를 저장함

def onetwothree(num):
    for i in range(3,num):
        arr.append( arr[i-1] + arr[i-2] + arr[i-3] ) ##num은 1 + (num-1)의 표현, 2 + (num-2)의 표현, 3 + (num-3)의 표현 로 이루어짐
    return arr[num-1]

if __name__ == "__main__":
    inputNum = int(input("입력 : "))
    answer = onetwothree(inputNum)
    print(answer)
