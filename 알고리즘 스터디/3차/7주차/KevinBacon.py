#https://docs.google.com/spreadsheets/d/1vWFRyJWPBBSlo7aMolhchE9a7jn3fkO4hJI4FHLuo04/edit#gid=0
#플로이드 와샬

import sys

def search(floyd):
    global node

    # x -> n -> y
    for n in range(node):    #거치는 노드
        for row in range(node): #모든 노드에 대해
            for col in range(node): #모든 연결된 노드
                if floyd[row][col] > floyd[row][n] + floyd[n][col]:
                    floyd[row][col] = floyd[row][n] + floyd[n][col]

if __name__ == '__main__':
    global node
    node, edge = tuple(map(int, sys.stdin.readline().split()))
    path = [[] for _ in range(node)]
    floyd = [[100 for _ in range(node)] for _ in range(node)]   #다른 사용자까지의 거리를 저장

    for _ in range(edge):
        src, dst = tuple(map(int, sys.stdin.readline().split()))
        path[src-1].append(dst-1)

    #인접 노드 채우기
    for i in range(node):
        floyd[i][i] = 0
        for _path in path[i]:
            floyd[i][_path] = floyd[_path][i] = 1

    search(floyd)
        
    #값이 가장 작은 사용자 구하기
    min_value = 100
    winner = 1

    for i in range(len(floyd)):
        r_sum = sum(floyd[i])
        if r_sum < min_value:
            min_value = r_sum
            winner = i + 1

    print(winner)