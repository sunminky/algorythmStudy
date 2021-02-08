#https://programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    answer = set()
    
    for seq, i in enumerate(numbers[:-1]):
        for j in numbers[seq+1:]:
            answer.add(i + j)
    
    return sorted(list(answer))