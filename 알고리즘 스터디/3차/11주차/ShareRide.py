# https://programmers.co.kr/learn/courses/30/lessons/72413?language=python3

from queue import PriorityQueue


def djikstra(path, src, n) -> list:  # 경로별 코스트 반환
    cost = [20000000 for _ in range(n)]
    queue = PriorityQueue()
    cost[src] = 0
    queue.put((cost[src], src))

    while not queue.empty():
        c, cur = queue.get()
        # 현재 노드와 연결된 애들 갱신
        for dst, n_cost in path[cur]:
            if cost[dst] > n_cost + cost[cur]:  # 갱신
                cost[dst] = n_cost + cost[cur]
                queue.put((cost[dst], dst))

    return cost


def solution(n, s, a, b, fares):
    path = [list() for _ in range(n)]
    costs = []

    for fare in fares:
        path[fare[0] - 1].append((fare[1] - 1, fare[2]))
        path[fare[1] - 1].append((fare[0] - 1, fare[2]))

    costs.append(djikstra(path, s - 1, n))
    costs.append(djikstra(path, a - 1, n))
    costs.append(djikstra(path, b - 1, n))

    answer = [costs[0][i] + costs[1][i] + costs[2][i] for i in range(n)]
    return min(answer)  # min(A까지 비용 + B까지 경로 + 출발지 까지 경로)


if __name__ == '__main__':
    solution(6, 4, 6, 2, [[4, 1, 10],
                          [3, 5, 24],
                          [5, 6, 2],
                          [3, 1, 41],
                          [5, 1, 24],
                          [4, 6, 50],
                          [2, 4, 66],
                          [2, 3, 22],
                          [1, 6, 25]])  # 82
    solution(7, 3, 4, 1, [[5, 7, 9],
                          [4, 6, 4],
                          [3, 6, 1],
                          [3, 2, 3],
                          [2, 1, 6]])  # 14
    solution(6, 4, 5, 6, [[2, 6, 6],
                          [6, 3, 7],
                          [4, 6, 7],
                          [6, 5, 11],
                          [2, 5, 12],
                          [5, 3, 20],
                          [2, 4, 8],
                          [4, 3, 9]])  # 18
