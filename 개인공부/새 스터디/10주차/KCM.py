#https://www.acmicpc.net/problem/10217
#시간초과..
import sys
import heapq

if __name__ == '__main__':
    n_testcase = int(sys.stdin.readline())

    for _ in range(n_testcase):
        airport, support, ticket = tuple(map(int, sys.stdin.readline().split()))
        path = [[] for _ in range(airport+1)] #간선 저장
        fee = [[sys.maxsize for _ in range(airport+1)] for _ in range(support + 1)]   #요금 저장
        visited = [False for _ in range(support + 1)]
        dst_cost = []
        queue = []

        for _ in range(ticket):
            src, dst, cost, time = tuple(map(int, sys.stdin.readline().split()))
            path[src].append((dst, cost, time))

        visited[0] = True
        fee[0][1] = 0
        heapq.heappush(queue, 0)

        while queue:
            cur_cost = heapq.heappop(queue)
            for ap in range(1, airport + 1):
                if fee[cur_cost][ap] == sys.maxsize:
                    continue
                for neigh, cost, time in path[ap]:
                    if cur_cost + cost > support:
                        continue
                    #값이 더 작으면 갱신
                    if fee[cur_cost + cost][neigh] > fee[cur_cost][ap] + time:
                        #사이클 감지
                        cycle_flag = False
                        for i in range(cur_cost):
                            if fee[i][neigh] < fee[cur_cost][ap] + time:
                                cycle_flag = True
                                break
                        if not cycle_flag:
                            fee[cur_cost + cost][neigh] = fee[cur_cost][ap] + time
                            if not visited[cur_cost + cost]:
                                heapq.heappush(queue, cur_cost + cost)
                                visited[cur_cost + cost] = True
                            if neigh == airport:
                                dst_cost.append(fee[cur_cost][ap] + time)
        if not dst_cost:
            print("Poor KCM")
        else:
            print(min(dst_cost))

        del fee, path, visited

