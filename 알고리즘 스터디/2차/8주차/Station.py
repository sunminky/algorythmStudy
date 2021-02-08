def solution(n, stations, w):
    answer = 0
    idx = 1 #커버안된 위치의 시작점
    area = []   #기지국이 커버하지 못하는 구간배열
    if stations[0] - w <= 1:    #원래 설치된 기지국이 앞쪽을 전부 커버할 때
        idx = stations[0] + w + 1   #커버안된 위치의 시작점을 기지국이 커버하지 못하는 구역중 제일 앞으로 옮김
        del stations[0]
    
    #기지국이 커버하지 못하는 구간을 구해서 저장
    for i in stations:  
        area.append(i-w-1 - idx + 1)
        idx = i + w + 1

    if idx <= n:    #원래 설치된 기지국이 커버하지 못하는 범위가 뒤에 더 있을때
        area.append(n-idx+1)

    #커버안된 구역에 필요한 기지국개수 계산
    for i in area:
        quota, remainder = divmod(i, w*2+1)
        answer += quota
        if remainder > 0:   #기지국이 2.1개 필요하다면 올림해서 3개로 만들어줌
            answer += 1
    return answer

if __name__ == '__main__':
    result = solution(12, [2, 10], 1)
    print(result)
    result = solution(16, [9], 2)
    print(result)