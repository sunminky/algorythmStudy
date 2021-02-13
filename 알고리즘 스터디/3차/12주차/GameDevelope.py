#https://www.acmicpc.net/problem/1516

import sys

def search(node):
    global parent, costs, estimate
    #부모가 나 자신임
    if parent[node][0] == node + 1:
        estimate[node] = costs[node]

    #초기화가 안 된 경우
    if estimate[node] == -1:
        estimate[node] = max([search(p-1) for p in parent[node]]) + costs[node]

    return estimate[node]



if __name__ == '__main__':
    global parent, costs, estimate
    n_structure = int(sys.stdin.readline())
    parent = []
    costs = []
    estimate = [-1 for _ in range(n_structure)]

    for i in range(n_structure):
        cost, *_parents = map(int, sys.stdin.readline().split())
        costs.append(cost)

        if len(_parents) == 1:
            parent.append([i+1])
        else:
            parent.append(_parents[:-1])

    for i in range(n_structure):
        estimate[i] = search(i)

    for e in estimate:
        print(e)