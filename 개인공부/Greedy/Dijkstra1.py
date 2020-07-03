# https://level.goorm.io/exam/43211/%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-dijkstra-s-algorithm/quiz/1
import sys

def MinimunWeightIndex(unvisited, nodeValues):
    min = sys.maxsize
    minIdx = unvisited[0]
    for _,index in enumerate(unvisited):
        if nodeValues[index] < min :
            min = nodeValues[index]
            minIdx = index
    return minIdx

def updateWeight(index, nodeInfo, nodeValues):
    for i, value in enumerate(nodeInfo[index]): #이 노드와 연결된 정점을 찾는 중
        if not value == sys.maxsize and nodeValues[i] > value + nodeValues[index]:  #더 짧은 경로 발견시
            nodeValues[i] = value + nodeValues[index]
    return nodeValues
            

if __name__ == '__main__':
    nodeNum, edgeNum = map(int, input().split())  # 노드개수와 간선개수 입력
    nodeInfo = [[sys.maxsize for i in range(nodeNum)] for j in range(nodeNum)]
    nodeValues = [sys.maxsize for i in range(nodeNum)]  #간선의 가중치 저장
    unvisited = [i for i in range(nodeNum)] #방문 안한 노드 저장

    for i in range(nodeNum):
        nodeInfo[i][i] = 0

    for i in range(edgeNum):  # 간선 정보들 입력받음
        src, dst, weight = map(int, input().split())  # 간선 정보 입력받음
        if(nodeInfo[src-1][dst-1] > weight and nodeInfo[dst-1][src-1] > weight):
            nodeInfo[src-1][dst-1] = weight
            nodeInfo[dst-1][src-1] = weight
    
    startingPoint = int(input())-1    #시작 노드 입력
    nodeValues[startingPoint] = 0

    ###탐색 시작###
    while len(unvisited):
        curindex = MinimunWeightIndex(unvisited,nodeValues)
        unvisited.remove(curindex)
        nodeValues = updateWeight(curindex,nodeInfo,nodeValues)

    for i,value in enumerate(nodeValues):
        print("{seq}:{value}".format(seq=i+1, value=value))