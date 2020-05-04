import sys

def rec2(arr):
    sum = 0
    left = -sys.maxsize - 1  #최소값으로 만들기
    right = -sys.maxsize - 1 #최소값으로 만들기
    arrlen = len(arr) // 2

    for i in range(arrlen, -1, -1): #가운데에서 부터 왼쪽끝까지 더함
        sum += arr[i]
        if (sum > left):     #좋은 것만 더해진 상태라면
            left = sum       #최대값 갱신

    sum = 0
    for i in range(arrlen + 1, len(arr)):   #가운데에서 부터 오른쪽끝까지 더함
        sum += arr[i]
        if (sum > right):    #좋은 것만 더해진 상태라면
            right = sum      #최대값 갱신

    return max(left, right, left + right)   #왼쪽만 가진 값, 오른쪽만 가진 값, 좋은것만 골라서 더한 값

def rec(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        arrlen = len(arr) // 2
        return max(rec(arr[0:arrlen]), rec(arr[arrlen:]), rec2(arr))

if __name__ == "__main__":
    arr = [31 ,-41 ,59 ,26 ,-53 ,58 ,97 ,-93 ,-23 ,84]
    print(rec(arr))
