def recursion(rotateCnt, arr):
    arrlen = len(arr)
    if len(arr) == 1:
        print("회전횟수 : ", rotateCnt + 1)
        return arr[0]
    if arr[0] > arr[arrlen // 2]:  # 앞에 회전된 배열의 부분집합이 있다
        return recursion(rotateCnt, arr[:arrlen // 2])  # 뒷 배열 제외하고 탐색 계속 진행
    else:   #회전된 배열의 부분집합 중 더 큰값이 뒤에 있다
        rotateCnt += arrlen // 2    #최대값의 위치를 갱신
        return recursion(rotateCnt, arr[arrlen // 2:])  # 앞 배열 제외하고 탐색 계속 진행


if __name__ == "__main__":
    arr = [10, 11, 1, 2, 5, 6, 7, 9]
    rotateCnt = 0   #몇번째에 최대값이 있는지 확인
    '''if not arr[0] > arr[len(arr) - 1]:  #회전을 한적이 없는 경우
        print(arr[len(arr) - 1])
    else:'''
    print(recursion(rotateCnt, arr))
