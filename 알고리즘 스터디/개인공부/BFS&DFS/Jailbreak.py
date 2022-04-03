# https://www.acmicpc.net/problem/9376
import sys
import heapq


def find_pos(field):
    pos = []

    for row in range(len(field)):
        for col in range(len(field[row])):
            if field[row][col] == '$':
                pos.append((col, row))

    return pos


def edge_check(costs) -> int:
    result = min(min(costs[0]), min(costs[-1]))

    for row in range(1, len(field) - 1):
        result = min(result, costs[row][0], costs[row][-1])

    return result


if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        height, width = map(int, sys.stdin.readline().split())
        field = [sys.stdin.readline().rstrip() for _ in range(height)]
        costs = [[[10001] * width for _ in range(height)] for _ in range(3)]
        pos = find_pos(field)
        movement = ((0, 1), (0, -1), (1, 0), (-1, 0))

        for seq in range(2):
            costs[seq][pos[seq][1]][pos[seq][0]] = 0
            queue = [(0, pos[seq][0], pos[seq][1])]

            while queue:
                cur_cost, cur_x, cur_y = heapq.heappop(queue)

                for _move in movement:
                    new_x = cur_x + _move[0]
                    new_y = cur_y + _move[1]
                    new_cost = cur_cost

                    # 바운더리 체크
                    if not 0 <= new_x < width:
                        continue
                    if not 0 <= new_y < height:
                        continue
                    # 벽 체크
                    if field[new_y][new_x] == '*':
                        continue
                    # 잠금해제 여부
                    if field[new_y][new_x] == '#':
                        new_cost += 1
                    # 최소값 갱신
                    if costs[seq][new_y][new_x] > new_cost:
                        costs[seq][new_y][new_x] = new_cost
                        heapq.heappush(queue, (new_cost, new_x, new_y))

        queue = [(10001, pos[1][0], pos[1][1])]
        visited = [[False] * width for _ in range(height)]

        visited[pos[1][1]][pos[1][0]] = True

        for row in range(height):
            for col in range(width):
                costs[2][row][col] = costs[0][row][col] + costs[1][row][col]

                if field[row][col] == '#':
                    costs[2][row][col] -= 1

        while queue:
            cur_cost, cur_x, cur_y = heapq.heappop(queue)

            # print(cur_x, cur_y, cur_cost, visited[cur_y][cur_x])

            for _move in movement:
                new_x = cur_x + _move[0]
                new_y = cur_y + _move[1]
                new_cost = cur_cost

                # 바운더리 체크
                if not 0 <= new_x < width:
                    continue
                if not 0 <= new_y < height:
                    continue
                # 벽 체크
                if field[new_y][new_x] == '*':
                    continue
                # 잠금장치 해제
                if field[new_y][new_x] == '#':
                    new_cost += 1
                # 최소값 갱신
                if costs[2][new_y][new_x] > new_cost:
                    costs[2][new_y][new_x] = new_cost
                    heapq.heappush(queue, (costs[2][new_y][new_x], new_x, new_y))
                elif visited[new_y][new_x] is False:
                    heapq.heappush(queue, (costs[2][new_y][new_x], new_x, new_y))
                    visited[new_y][new_x] = True

        print(min(edge_check(costs[0]) + edge_check(costs[1]), edge_check(costs[2])))
