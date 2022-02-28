# https://www.acmicpc.net/problem/9328
import sys
from collections import deque


def key_masking(keys):
    result = 0

    if keys != '0':
        for ch in keys:
            result |= 1 << (ord(ch) - 97)

    result |= 3 << 26

    return result


def padding(height, width) -> list:
    field = [['.'] * (width + 2)]

    field.extend([['.'] + [ch for ch in sys.stdin.readline().rstrip()] + ['.'] for _ in range(height)])
    field.append(['.'] * (width + 2))

    return field


def bitmasking(field) -> list:
    master_key = 1 << 26
    mask_field = [
        [1 << (ord(field[row][col]) - 65) if str.isupper(field[row][col]) else 0 if field[row][col] == '*' else master_key
         for col in range(len(field[row]))]
        for row in range(len(field))]

    return mask_field


if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        height, width = map(int, sys.stdin.readline().split())
        field = padding(height, width)
        my_key = key_masking(sys.stdin.readline().rstrip())
        mask_field = bitmasking(field)
        queue = deque([(0, 0)])
        answer = 0

        while queue:
            cur_x, cur_y = queue.popleft()
            movement = ((1, 0), (-1, 0), (0, 1), (0, -1))     # 동 서 남 북
            
            # 문서인 경우
            if field[cur_y][cur_x] == '$':
                answer += 1
                field[cur_y][cur_x] = '.'
            # 키인 경우
            if str.islower(field[cur_y][cur_x]):
                my_key |= 1 << (ord(field[cur_y][cur_x]) - 97)

            for _x, _y in movement:
                new_x = cur_x + _x
                new_y = cur_y + _y

                # 바운더리
                if not 0 <= new_x < width + 2:
                    continue
                if not 0 <= new_y < height + 2:
                    continue

                # 키가 없거나 벽임
                if not mask_field[new_y][new_x] & my_key:
                    continue

                # 동일한 키값으로 같은 위치 방문
                if not mask_field[new_y][new_x] ^ my_key:
                    continue

                mask_field[new_y][new_x] = my_key
                queue.append((new_x, new_y))

        print(answer)
