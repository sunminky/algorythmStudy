# https://programmers.co.kr/learn/courses/30/lessons/42628
from queue import PriorityQueue


def solution(operations):
    answer = [0, 0]
    maxQueue = PriorityQueue()
    minQueue = PriorityQueue()

    for command in operations:
        opcode, parm = command.split()
        parm = int(parm)

        if opcode == "I":
            element = [parm, True]
            maxQueue.put((-parm, element))  # 힙은 기본적으로 최소힙을 구현
            minQueue.put((parm, element))

        elif opcode == "D":
            if parm == 1:
                while not maxQueue.empty():
                    _, _data = maxQueue.get()

                    if not _data[1]:
                        continue

                    _data[1] = False
                    break

            elif parm == -1:
                while not minQueue.empty():
                    _, _data = minQueue.get()

                    if not _data[1]:
                        continue

                    _data[1] = False
                    break

    # 정답배열 만들기
    while not maxQueue.empty():
        _, _data = maxQueue.get()

        if _data[1]:
            answer[0] = _data[0]
            break

    while not minQueue.empty():
        _, _data = minQueue.get()

        if _data[1]:
            answer[1] = _data[0]
            break

    return answer


if __name__ == '__main__':
    solution(["I 16", "D 1"])  # [0,0]
    solution(["I 7", "I 5", "I -5", "D -1"])  # [7,5]
    solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])  # [333, -45]
