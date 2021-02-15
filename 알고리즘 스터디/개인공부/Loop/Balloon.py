#https://programmers.co.kr/learn/courses/30/lessons/68646
def solution(lst):
    answer = set()  #중복을 제거하기 위해 set을 사용
    forward = lst.copy()
    reverse = lst.copy()

    min_value = 1000000000

    #0~i번째 까지 원소중 가장 작은 값 저장
    for i in range(len(forward)):
        if forward[i] < min_value:
            min_value = forward[i]
        else:
            forward[i] = min_value

    min_value = 1000000000

    # -1 ~ -i번째 까지 원소중 가장 작은 값 저장
    for i in range(1, len(reverse)+1):
        if reverse[-i] < min_value:
            min_value = reverse[-i]
        else:
            reverse[-i] = min_value

    #왼쪽과 오른쪽 비교
    for i in range(len(lst)):
        left = forward[i]   #나눈 기준으로 왼쪽 원소에서 가장 작은 값
        right = reverse[i]  #나눈 기준으로 오른쪽 원소에서 가장 작은 값
        answer.add(left)
        answer.add(right)

    return len(answer)

if __name__ == '__main__':
    solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]) #6
    solution([9,-1,-5]) #3