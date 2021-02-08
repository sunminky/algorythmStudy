def solution(n):
    answer = 0
    position = []   #퀸들이 놓인 위치를 저장하는 배열
    for i in range(n):
        position.append((i,n-1))    #새로 놓인 퀸의 좌표를 좌표배열에 추가
        answer += lookFor(n, n-1, position) #다음줄에 놓일수 있는 퀸을 찾으러 가자
        position.pop()  #가장 최근에 추가된 퀸을 가지고 만들수 있는 경우는 모두 찾았으므로 가장 최근에 추가된 퀸의 위치 제거
    return answer

#다음줄에 퀸이 어디에 놓일지 찾는다(lookfor)
def lookFor(width, leftN, position):    #체스판의 크기, 아직 퀸이 놓이지않은 줄의 수, 이전의 퀸들이 놓인 좌표배열
    count = 0   #퀸을 모든줄에 놓을수 있는 경우의 수 저장
    if leftN == 0:  #퀸이 모든줄에 다 놓임
        return 1    #퀸이 모든줄에 놓이는 경우의 수 1증가
    accessable = block(width, leftN, position)  #다음줄에 어느 자리에 퀸이 놓일수 있는지(accessable) 체크
    for i in range(width):  #현재 줄 모두 탐색
        if accessable[i]:   #다른퀸에 의해 방해되지 않는 accessable한 구역이라면
            position.append((i, leftN - 1)) #그 자리에 퀸을 놓고
            count += lookFor(width, leftN - 1, position)    #그 다음줄을 탐색
            position.pop()  #이 퀸으로 구할수 있는 경우의 수는 모두 구했으므로 이 퀸의 위치 제거
    return count

def block(width, leftN, position):
    accessable = [True for _ in range(width)]

    for x,y in position:
        accessable[x] = False   #바로 윗줄 제거
        if x - (y - leftN + 1) >= 0:
            accessable[x - (y - leftN + 1)] = False   #좌상줄 제거
        if x + (y - leftN + 1) < width:
            accessable[x + (y - leftN + 1)] = False   #우상줄 제거

    return accessable

if __name__ == '__main__':
    for i in range(1,13):
        result = solution(i)
        print(i," :",result)