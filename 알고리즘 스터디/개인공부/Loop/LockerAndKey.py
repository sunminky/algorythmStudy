# https://programmers.co.kr/learn/courses/30/lessons/60059


# 충돌감지
def collision_check(key, lock, x, y) -> bool:
    for row in range(len(lock)):
        for col in range(len(lock)):
            # 둘 다 1인 경우, 와꾸가 안맞음
            if lock[row][col] == 1 and key[row + y][col + x] == 1:
                return
                # 둘 다 비어있는 경우, 빈 공간을 채우지 못함
            if lock[row][col] == 0 and key[row + y][col + x] == 0:
                return False

    return True


# 시계방향으로 90도 돌림
def rotate(lock: list) -> list:
    new_lock = [[0 for _ in range(len(lock))] for _ in range(len(lock))]

    for row in range(len(lock)):
        for col in range(len(lock)):
            new_lock[row][col] = lock[len(lock) - 1 - col][row]

    return new_lock


def solution(key, lock) -> bool:
    # 키 주변을 lock 길이 - 1 만큼 패딩
    padding_key = [[0 for _ in range(len(key) + (len(lock) - 1) * 2)] for _ in range(len(key) + (len(lock) - 1) * 2)]

    # 키 넣어주기
    for row in range(len(key)):
        for col in range(len(key)):
            padding_key[row + len(lock) - 1][col + len(lock) - 1] = key[row][col]

    # lock을 90, 180, 270, 360 도 씩 돌려가면서 키 탐색
    for _ in range(4):
        lock = rotate(lock)

        # 모든 키에 대해서 대입
        for row in range(len(lock) + len(key) - 1):
            for col in range(len(lock) + len(key) - 1):
                if collision_check(padding_key, lock, col, row):
                    return True

    return False


if __name__ == '__main__':
    print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))  # True
