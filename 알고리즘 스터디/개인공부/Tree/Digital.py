# https://www.acmicpc.net/problem/8111
import sys
from collections import deque


def get_last_digit(base):
    table = [list() for _ in range(10)]

    for i in range(0, 10):
        table[base * i % 10].append(base * i)

    return table


if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        base = int(sys.stdin.readline())
        queue = deque()
        memoization = dict()

        memoization[base] = (-1, -1)  # base를 만나면 종료하게 함, (이전 숫자, 잘려나간 마지막 숫자)
        queue.append(base)
        tail_index = get_last_digit(base)    # 마지막 한자리 인덱싱

        while queue:
            cur_num = queue.popleft()

            if cur_num == 1:
                break

            # 끝자리가 0이 되게 함
            for new_nums in tail_index[(10 - cur_num % 10) % 10]:
                if (new_nums + cur_num) // 10 in memoization:
                    continue
                memoization[(new_nums + cur_num) // 10] = (cur_num, '0')
                queue.append((new_nums + cur_num) // 10)

            # 끝자리가 1이 되게 함
            for new_nums in tail_index[(11 - cur_num % 10) % 10]:
                if (new_nums + cur_num) // 10 in memoization:
                    continue
                memoization[(new_nums + cur_num) // 10] = (cur_num, '1')
                queue.append((new_nums + cur_num) // 10)
                
        # 출력
        # 1 -> ... -> base
        print_val = 1

        print(print_val, end="")
        while print_val != base:
            print(memoization[print_val][1], end="")
            print_val =memoization[print_val][0]

        print()
