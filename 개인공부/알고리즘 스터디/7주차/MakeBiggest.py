#https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    lstNumber = list(number)
    targetLen = len(number) - k
    answer = lstNumber[:targetLen]
    count = k

    for i in number[targetLen:]:
        for j in range(targetLen - 1):
            if answer[j] < answer[j+1]:
                del answer[j]
                answer.append(i)  # 뒤에있는 숫자 추가
                count = count - 1
                if count == 0:  #빼야할 갯수만큼 다 뺌
                    return "".join(answer)
                break

        if answer[-1] < i:  #answer 맨뒤랑 현재 추가되는 숫자 비교
            answer[-1] = i  #뒤에있는 숫자 추가

    return "".join(answer)

if __name__ == '__main__':
    result = solution("1924",2)
    print(result)

    result = solution("1231234", 3)
    print(result)

    result = solution("4177252841", 4)
    print(result)