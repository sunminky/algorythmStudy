#https://www.acmicpc.net/problem/7562
import sys
from queue import PriorityQueue

def Levenshtein(current, target):
    return abs(target[0] - current[0]) + abs(target[1] - current[1])

if __name__ == '__main__':
    n_testcase = int(sys.stdin.readline())

    for _ in range(n_testcase):
        field_size = int(sys.stdin.readline())
        start_loc = tuple(map(int, sys.stdin.readline().split()))
        target_loc = tuple(map(int, sys.stdin.readline().split()))
        field_count = [[sys.maxsize for _ in range(field_size)] for _ in range(field_size)]
        visited = [[False for _ in range(field_size)] for _ in range(field_size)]
        queue = PriorityQueue()

        field_count[start_loc[1]][start_loc[0]] = 0
        visited[start_loc[1]][start_loc[0]] = True
        queue.put(((field_count[start_loc[1]][start_loc[0]], Levenshtein(start_loc, target_loc)), start_loc))

        while True:
            cost_distance, current_loc = queue.get()
            #print(current_loc, cost_distance)

            if cost_distance[1] == 0:
                break

            ## 탐색 ##
            direction = ((1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1))
            for item in direction:
                x = current_loc[1] - item[0]
                y = current_loc[0] - item[1]
                if x < 0 or x >= field_size or y < 0 or y >= field_size or visited[y][x]:
                    continue
                visited[y][x] = True
                field_count[y][x] = cost_distance[0] + 1
                queue.put(((field_count[y][x],Levenshtein((x,y), target_loc)), (x, y)))

        if field_count[target_loc[1]][target_loc[0]] == sys.maxsize:
            print(0)
        else:
            print(field_count[target_loc[1]][target_loc[0]])