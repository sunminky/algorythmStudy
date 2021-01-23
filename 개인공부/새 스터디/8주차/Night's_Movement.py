#https://www.acmicpc.net/problem/7562
import sys
import heapq

if __name__ == '__main__':
    n_testcase = int(sys.stdin.readline())

    for _ in range(n_testcase):
        field_size = int(sys.stdin.readline())
        start_loc = tuple(map(int, sys.stdin.readline().split()))
        target_loc = tuple(map(int, sys.stdin.readline().split()))
        field_count = [[1000000 for _ in range(field_size+1)] for _ in range(field_size+1)]
        queue = []

        field_count[start_loc[0]][start_loc[1]] = 0
        heapq.heappush(queue, (0, start_loc))

        cur_loc = start_loc

        while cur_loc != target_loc:
            cost, cur_loc = heapq.heappop(queue)
            
            #나이트가 움직일 수 있는 좌표을 큐에 추가
            if cur_loc[1] -2 >= 0 and cur_loc[0] - 1 >= 0:
                if cost + 1 <= field_count[cur_loc[1] - 2][cur_loc[0] - 1]:  #범위 체크
                    field_count[cur_loc[1] - 2][cur_loc[0] - 1] = cost + 1  #계산한 값이 더 작으면 갱신
                    heapq.heappush(queue, (cost+1, (cur_loc[0] -1, cur_loc[1] -2)))  #큐에 추가

            if cur_loc[1] -2 >= 0 and cur_loc[0] + 1 <= field_size:
                if cost + 1 < field_count[cur_loc[1] - 2][cur_loc[0] + 1]:  #범위 체크
                    field_count[cur_loc[1] - 2][cur_loc[0] + 1] = cost + 1  #계산한 값이 더 작으면 갱신
                    heapq.heappush(queue, (cost+1, (cur_loc[0] +1, cur_loc[1] -2)))  #큐에 추가

            if cur_loc[1] -1 >= 0 and cur_loc[0] - 2 >= 0:
                if cost + 1 < field_count[cur_loc[1] - 1][cur_loc[0] - 2]:  #범위 체크
                    field_count[cur_loc[1] - 1][cur_loc[0] - 2] = cost + 1  #계산한 값이 더 작으면 갱신
                    heapq.heappush(queue, (cost+1, (cur_loc[0] -2, cur_loc[1] -1)))  #큐에 추가

            if cur_loc[1] +1 <= field_size and cur_loc[0] - 2 >= 0:
                if cost + 1 < field_count[cur_loc[1] + 1][cur_loc[0] - 2]:  #범위 체크
                    field_count[cur_loc[1] + 1][cur_loc[0] - 2] = cost + 1  #계산한 값이 더 작으면 갱신
                    heapq.heappush(queue, (cost+1, (cur_loc[0] -2, cur_loc[1] + 1)))  #큐에 추가

            if cur_loc[1] +2 <= field_size and cur_loc[0] - 1 >= 0:
                if cost + 1 < field_count[cur_loc[1] + 2][cur_loc[0] - 1]:  #범위 체크
                    field_count[cur_loc[1] + 2][cur_loc[0] - 1] = cost + 1  #계산한 값이 더 작으면 갱신
                    heapq.heappush(queue, (cost+1, (cur_loc[0] -1, cur_loc[1] + 2)))  #큐에 추가

            if cur_loc[1] +2 <= field_size and cur_loc[0] + 1 <= field_size:
                if cost + 1 < field_count[cur_loc[1] + 2][cur_loc[0] + 1]:  #범위 체크
                    field_count[cur_loc[1] + 2][cur_loc[0] + 1] = cost + 1  #계산한 값이 더 작으면 갱신
                    heapq.heappush(queue, (cost+1, (cur_loc[0] +1, cur_loc[1] + 2)))  #큐에 추가

            if cur_loc[1] +1 <= field_size and cur_loc[0] - 2 >= 0:
                if cost + 1 < field_count[cur_loc[1] + 1][cur_loc[0] - 2]:  #범위 체크
                    field_count[cur_loc[1] + 1][cur_loc[0] - 2] = cost + 1  #계산한 값이 더 작으면 갱신
                    heapq.heappush(queue, (cost+1, (cur_loc[0] - 2, cur_loc[1] + 1)))  #큐에 추가

            if cur_loc[1] +1 <= field_size and cur_loc[0] + 2 <= field_size:
                if cost + 1 < field_count[cur_loc[1] + 1][cur_loc[0] + 2]:  #범위 체크
                    field_count[cur_loc[1] + 1][cur_loc[0] + 2] = cost + 1  #계산한 값이 더 작으면 갱신
                    heapq.heappush(queue, (cost+1, (cur_loc[0] + 2, cur_loc[1] + 1)))  #큐에 추가

        print(field_count[target_loc[1]][target_loc[0]])
        #print(field_count)