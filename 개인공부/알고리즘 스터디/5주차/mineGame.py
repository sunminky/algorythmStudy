def solution(N, mine, P):   #필드크기, 지뢰 위치, 시작위치
    answer = 0
    global field
    global visited
    global nearLst
    field = [[0 for _ in range(N)] for _ in range(N)]   #필드를 0으로 초기화, -1지뢰 0안전 1 지뢰옆
    visited = [[False for _ in range(N)] for _ in range(N)] #방문한 필드 체크
    nearLst = []    #지뢰 인근 지역의 좌표 저장

    for i in mine:
        x,y = i
        field[x][y] = -1
        field = nearMine(x,y,field)

    recursive(P)

    for loc in nearLst:
        stuckLocation(loc)

    for i in range(n):
        for j in range(n):
            #print(visited[i][j], end=" ")
            if visited[i][j]:
                answer += 1
        #print()
    return answer

def nearMine(x,y,field):    #지뢰 근처 체크
    if (x > 0 and y < len(field) - 1) and field[x-1][y+1] != -1:
        field[x-1][y+1] = 1
    if (x > 0) and field[x-1][y] != -1:
        field[x-1][y] = 1
    if (x > 0 and y > 0) and field[x-1][y-1] != -1:
        field[x-1][y-1] = 1
    if (y < len(field) - 1) and field[x][y+1] != -1:
        field[x][y+1] = 1
    if field[x][y] != -1:
        field[x][y] = 1
    if (y > 0) and field[x][y-1] != -1:
        field[x][y-1] = 1
    if (x < len(field) - 1 and y < len(field) - 1) and field[x+1][y+1] != -1:
        field[x+1][y+1] = 1
    if (x < len(field) - 1) and field[x+1][y] != -1:
        field[x+1][y] = 1
    if (x < len(field) - 1 and y > 0) and field[x+1][y-1] != -1:
        field[x+1][y-1] = 1
    return field

def recursive(location):
    #길이 있고 방문 안 했으면 탐색, 숫자 구역인 경우 탐색후 종료
    if field[location[0]][location[1]] != 0:    #숫자영역에 방문한 경우
        nearLst.append(location)
        return
    #오른쪽 보기
    if location[1] < n-1 and not visited[location[0]][location[1]+1]:
        visited[location[0]][location[1]+1] = True
        recursive([location[0], location[1]+1])
    #위쪽 보기
    if location[0] < n-1 and not visited[location[0]+1][location[1]]:
        visited[location[0]+1][location[1]] = True
        recursive([location[0]+1, location[1]])
    #왼쪽 보기
    if location[1] > 0 and not visited[location[0]][location[1]-1]:
        visited[location[0]][location[1]-1] = True
        recursive([location[0], location[1]-1])
    #아래쪽 보기
    if location[0] > 0 and not visited[location[0]-1][location[1]]:
        visited[location[0]-1][location[1]] = True
        recursive([location[0]-1, location[1]])

def stuckLocation(location):
    #대각선에 1구역 존재 하면 그 사이 체크
    #인덱스 범위, 인덱스 범위, 대각선에 존재하는 좌표가 방문했던 곳,아직 안간 곳이 지뢰가 아님
    #동북
    if location[0] < n-1 and location[1] < n-1 and field[location[0]+1][location[1]+1] == 1 and visited[location[0]+1][location[1]+1] and field[location[0]][location[1]+1] != -1:
        visited[location[0]][location[1]+1] = True
    #동남
    if location[0] > 0 and location[1] < n-1 and field[location[0]-1][location[1]+1] == 1 and visited[location[0]-1][location[1]+1] and field[location[0]-1][location[1]] != -1:
        visited[location[0]-1][location[1]] = True
    #남서
    if location[0] > 0 and location[1] > 0 and field[location[0]-1][location[1]-1] == 1 and visited[location[0]-1][location[1]-1] and field[location[0]][location[1]-1] != -1:
        visited[location[0]][location[1]-1] = True
    #서북
    if location[0] < n-1 and location[1] > 0 and field[location[0]+1][location[1]-1] == 1 and visited[location[0]+1][location[1]-1] and field[location[0]][location[1]-1] != -1:
        visited[location[0]][location[1]-1] = True



n = 9
#solution(9,[[1,2],[2,6],[3,4],[3,8],[4,9],[5,4],[5,8],[6,7],[7,2],[9,1]],[8,5]) #29
print(solution(n,[[0,1],[1,5],[2,3],[2,7],[3,8],[4,3],[4,7],[5,6],[6,1],[8,0]],[7,4])) #29
n = 5
print(solution(n,[[2,0],[2,2],[4,2]],[4,4])) #16
