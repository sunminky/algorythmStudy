#https://programmers.co.kr/learn/courses/30/lessons/67259]

up, right, down, left = (0, 1, 2, 3)

def solution(board):
    global circuitMap
    global costMap
    circuitMap = board  #전체 맵 저장
    costMap = [[9999 for _ in range(len(board))] for _ in range(len(board))]    #출발지 ~ 각 좌표까지 건설비용 저장
    costMap[0][0] = 0   #출발지의 건설비용은 0
    move(right, right, 1, 0, 0)
    move(down, down, 0, 1, 0)
    return costMap[len(board)-1][len(board)-1] * 100

def move(prevDirection, Direction, locationX, locationY, prevValue):
    if circuitMap[locationY][locationX] == 1 :  #장애물 있음
        return
    if prevDirection == Direction : #이전 진행방향과 현재 진행방향이 같다, 코너를 만들 필요가 없다
        cost = 1
    else :
        cost = 6
    if renewal(prevValue + cost, locationX, locationY) :    # 탐색을 이어나갈지 말지 선택
        return

    #상 우 하 좌 이동
    if locationY - 1 >= 0 :
        move(Direction, up, locationX, locationY - 1, costMap[locationY][locationX])  #위로 이동
    if locationX + 1 < len(circuitMap) :
        move(Direction, right, locationX + 1, locationY, costMap[locationY][locationX])    #우로 이동
    if locationY + 1 < len(circuitMap) :
        move(Direction, down, locationX, locationY + 1, costMap[locationY][locationX])    #아래로 이동
    if locationX - 1 >= 0 :
        move(Direction, left, locationX - 1, locationY, costMap[locationY][locationX])   #좌로 이동

def renewal(value, locationX, locationY):
    if costMap[locationY][locationX] >= value :
        costMap[locationY][locationX] = value
        return False    #새 값이 더 작을 경우 계속 탐색 진행
    return True # 새 값이 더 큰 경우 탐색 중지


if __name__ == '__main__':
    print(solution([[0,0,1],[0,0,0],[0,0,0]]))
    print("----------")
    print(costMap)