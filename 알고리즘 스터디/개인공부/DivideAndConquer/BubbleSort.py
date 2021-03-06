#https://www.acmicpc.net/problem/1517
#https://justicehui.github.io/ps/2019/04/23/BOJ1517/

import sys


sys.stdin.readline()
numbers = list(map(int, sys.stdin.readline().split()))
answer = 0


#정렬된 배열을 반환
def mergeSort(start, end) -> list:
    global answer

    #기저조건
    if start >= end:
        return [numbers[end]]

    middle = (start + end) // 2

    #병합정렬 시작
    s_list = [0 for _ in range(end - start + 1)]    #정렬된 요소가 저장될 배열
    l_idx = 0
    r_idx = 0
    left_num = mergeSort(start, middle) #0 ~ 중간 까지 정렬된 리스트
    right_num = mergeSort(middle + 1, end)  #중간 ~ 끝 까지 정렬된 리스트

    for i in range(len(s_list)):
        #왼쪽 배열이 모두 사용된 경우
        if l_idx == len(left_num):
            s_list[i] = right_num[r_idx]
            r_idx += 1
        #오른쪽 배열이 모두 사용된 경우
        elif r_idx == len(right_num):
            s_list[i] = left_num[l_idx]
            l_idx += 1
        #오른쪽 배열이 더 큰 경우
        elif left_num[l_idx] <= right_num[r_idx]:
            s_list[i] = left_num[l_idx]
            l_idx += 1
        #왼쪽 배열이 더 큰 경우
        elif right_num[r_idx] < left_num[l_idx]:
            s_list[i] = right_num[r_idx]
            r_idx += 1
            answer += len(left_num) - l_idx #왼쪽 배열에 남아있는 원소의 개수만큼 스왑이 일어남

    return s_list



if __name__ == '__main__':
    if len(numbers) == 1:
        print(0)
    else:
        mergeSort(0, len(numbers)-1)
        print(answer)
