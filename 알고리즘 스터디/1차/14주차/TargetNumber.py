def solution(numbers, target):
    answer = 0
    goal = int((sum(numbers) - target)/2) + target  #x+타겟 과 x 로 만들어 줍니다
    for i in range(len(numbers)):
        answer += recursive(i,0,numbers,goal)

    return answer

def recursive(start,sum,numbers,target):
    if(sum + numbers[start] > target):  #타겟보다 현재요소의 합들이 큰 경우
        return 0;
    if(sum+numbers[start] == target):   #타겟을 찾은 경우
        return 1;
    if (start == len(numbers) - 1):  # 제일 밑바닥 까지 다 훑은 경우
        return 0;
    ret = 0
    for idx in range(start+1,len(numbers)):
        ret += recursive(idx,sum+numbers[start],numbers,target)
    return ret

print(solution([2,3,5,7,9],2))