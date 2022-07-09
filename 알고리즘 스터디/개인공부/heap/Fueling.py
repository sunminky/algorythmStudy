# https://www.acmicpc.net/problem/1826
import sys
import heapq

if __name__ == '__main__':
    n_gasstation = int(sys.stdin.readline())
    gasstations = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(n_gasstation)],
                         key=lambda x: x[0])
    destination, cur_fuel = map(int, sys.stdin.readline().split())
    answer = 0
    queue = []

    gasstations.append((destination, 0))

    for _distance, _fuel in gasstations:
        while queue and cur_fuel < _distance:
            answer += 1
            _pop_fuel, _ = heapq.heappop(queue)
            cur_fuel += -_pop_fuel

        if cur_fuel < _distance:
            answer = -1
            break

        heapq.heappush(queue, (-_fuel, _distance))

    print(answer)
