import copy

def solution(n):
    map = [[True for _ in range(n)] for _ in range(n)]
    answer = lookOver(map, n-1)
    return answer

def lookOver(map, leftN):
    count = 0
    if leftN == -1:  #끝까지 충돌없이 도착
        return 1
    for seq, allowance in enumerate(map[leftN]):
        if allowance == True:
            newmap = copy.deepcopy(map)
            newmap = vertical(newmap, seq, leftN)   #수직선 긋기
            newmap = diagonal(newmap, seq, leftN) #좌상대각선, 우상대각선 긋기
            count += lookOver(newmap, leftN-1)
    return count

def vertical(map, x, y):   #수직선 긋기
    for i in range(y, -1, -1):
        map[i][x] = False   #다른 퀸이 올수없게 만듬
    return map

def diagonal(map, x, y):   #대각선 긋기
    #좌상대각선
    for seq, i in enumerate(range(y, -1, -1)):
        if x < seq:
            break
        map[i][x-seq] = False
    #우상대각선
    for seq, i in enumerate(range(y, -1, -1)):
        if x + seq >= len(map[y]):
            break
        map[i][x + seq] = False
    return map

if __name__ == '__main__':
    result = solution(4)
    print(result)