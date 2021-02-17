#https://programmers.co.kr/learn/courses/30/lessons/42587

from _collections import deque

def solution(priorities, location):
    priority_lst = sorted(priorities, reverse=True)
    p_idx = 0   #프린트가 끝난 작업의 우선순위 인덱스
    answer = 0
    queue = deque()

    #모든 원소를 큐에 넣음
    for seq, e in enumerate(priorities):
        queue.append([e, seq])

    while True:
        doc, seq = queue.popleft()

        #우선순위가 가장 높은 작업이면 큐에 다시 넣지 않음
        if priority_lst[p_idx] == doc:
            answer += 1
            p_idx += 1
            
            #방금 프린트 한 작업이 우리가 원하는 작업인 경우
            if seq == location:
                break
            else:
                continue

        queue.append([doc, seq])

    return answer

if __name__ == '__main__':
    solution([2, 1, 3, 2], 2)   #1
    solution([1, 1, 9, 1, 1, 1], 0) #5