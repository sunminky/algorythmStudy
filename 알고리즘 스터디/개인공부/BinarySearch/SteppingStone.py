#https://programmers.co.kr/learn/courses/30/lessons/43236?language=python3

def solution(distance, rocks, n):
    max_distance = distance + 1
    min_distance = 1
    sorted_rocks = [0] + sorted(rocks) + [distance] #시작점 ~ 돌 ~ 도착점
    gap_rocks = [sorted_rocks[i + 1] - sorted_rocks[i] for i in range(len(rocks) + 1)]  #돌 사이의 거리
    answer = distance

    while min_distance < max_distance:
        middle = (max_distance + min_distance) // 2

        # middel내로 거리 만족할 수 있는지 확인
        available_rock = n  #앞으로 더 치울수 있는 돌의 갯수
        c_sum = gap_rocks[0]    #이전 돌까지의 거리
    
        #모든 돌 사이의 거리가 middle보다 크거나 같도록 함
        for gap in gap_rocks[1:]:
            #돌 사이의 거리가 middle보다 작으면 돌을 치워서 middle보다 크게 만들어줌
            if c_sum < middle:
                c_sum += gap
                available_rock -= 1
                if available_rock == -1:
                    break
            else:
                c_sum = gap

        if available_rock == -1:
            max_distance = middle
        else:
            min_distance = middle + 1
            answer = middle

    return answer

if __name__ == '__main__':
    solution(25, [2, 14, 11, 21, 17], 2)