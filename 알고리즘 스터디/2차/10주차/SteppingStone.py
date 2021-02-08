from collections import deque


def solution(stones, k):
    kset = deque(stones[:k])
    maxVal, count = maxCount(kset)

    for step in range(k, len(stones)):

        if stones[step] <= maxVal:
            kset.append(stones[step])
        else:
            kset.append(maxVal)
            count = count + 1

        if kset[0] == maxVal:
            count = count - 1
            kset.popleft()
            if count == 0:
                maxVal, count = maxCount(kset)
        else:
            kset.popleft()

    return maxVal

def maxCount(kset):
    maxVal = 0
    count = 0
    for i in kset:
        if i > maxVal:
            maxVal = i
            count = 0
        if i == maxVal:
            count = count + 1

    return maxVal, count

if __name__ == '__main__':
    result = solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)
    print(result)
    result = solution([i for i in range(10**12, 0, -1)], 10**6)
    print(result)
