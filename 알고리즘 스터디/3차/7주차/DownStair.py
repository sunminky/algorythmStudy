# https://www.acmicpc.net/problem/1520

import sys
sys.setrecursionlimit(500*500)

movement = ((1, 0), (-1, 0), (0, 1), (0, -1))

def search(my_map, visited, x, y) -> int:
    answer = 0

    #끝에 도달한 경우
    if x == width-1 and y == height-1:
        visited[y][x] = 1
        return 1

    #이미 방문한 곳인 경우
    if visited[y][x] != -1:
        return visited[y][x]

    for _move in movement:
        new_x = x + _move[0]
        new_y = y + _move[1]

        #바운더리 체크
        if 0 <= new_x < width and 0 <= new_y < height:
            #내리막길 체크
            if my_map[y][x] > my_map[new_y][new_x]:
                answer += search(my_map, visited, new_x, new_y)
                visited_map[y][x] = answer  #도착지 까지 경로의 가지수 를 저장

    return answer

if __name__ == '__main__':
    global height, width
    height, width = tuple(map(int, sys.stdin.readline().rstrip().split()))  # 지도 높이, 지도 너비
    my_map = []
    visited_map = [[-1 for _ in range(width)] for _ in range(height)]    #방문 여부 저장

    for _ in range(height):
        my_map.append(list(map(int, sys.stdin.readline().rstrip().split())))

    print(search(my_map, visited_map, 0, 0))