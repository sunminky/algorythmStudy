#https://www.acmicpc.net/problem/7562
import sys
from queue import PriorityQueue

def clear_que(queue : PriorityQueue):
    '''큐를 비워지는 역할을 함, PriorityQueue는 clear가 없어서 직접구현'''
    while not queue.empty():
        queue.get()


if __name__ == '__main__':
    n_testcase = int(sys.stdin.readline())

    for _ in range(n_testcase):
        field_size = int(sys.stdin.readline())
        start_loc = tuple(map(int, sys.stdin.readline().split()))
        target_loc = tuple(map(int, sys.stdin.readline().split()))
        cost_map = [[1000 for _ in range(field_size)] for _ in range(field_size)]   #비용 저장
        queue = PriorityQueue() #탐색할 위치 저장
        movement = ((1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-2, 1), (-1, -2), (-2, -1))

        #계산량을 줄이기 위해 필요 없는 필드 버림
        x_boundary = (max(min(start_loc[0]-2, target_loc[0]-2), 0), min(field_size-1, max(start_loc[0]+2, target_loc[0]+2)))
        y_boundary = (max(min(start_loc[1]-2, target_loc[1]-2), 0), min(field_size-1, max(start_loc[1]+2, target_loc[1]+2)))
        cost_map[start_loc[1]][start_loc[0]] = 0    #출발 위치까지 가는데 필요한 비용은 0
        queue.put((cost_map[start_loc[1]][start_loc[0]], start_loc))    #큐에 출발지와 출발지 비용을 넣음

        while not queue.empty():
            cost, cur_loc = queue.get()

            for _move in movement:
                #바운더리 체크
                x = cur_loc[0] + _move[0]
                y = cur_loc[1] + _move[1]

                #x바운더리 만족
                if x_boundary[0] <= x <= x_boundary[1]:
                    #y바운더리 만족
                    if y_boundary[0] <= y <= y_boundary[1]:
                        #비용 최소값 갱신
                        if cost_map[y][x] > cost + 1:
                            cost_map[y][x] = cost + 1
                            queue.put((cost_map[y][x], (x, y)))
                            #타겟에 도착한 경우
                            if (x, y) == target_loc:
                                clear_que(queue)

        print(cost_map[target_loc[1]][target_loc[0]])