# https://www.acmicpc.net/problem/15662

import sys

if __name__ == '__main__':
    gear = [list(sys.stdin.readline().rstrip()) for _ in range(int(sys.stdin.readline()))]

    for _ in range(int(sys.stdin.readline())):
        nth_gear, direction = map(int, sys.stdin.readline().split())
        
        # nth 기어보다 앞에 있는 바퀴
        for seq in range(nth_gear - 2, -1, -1):
            # seq + 1의 7번째 톱니와 seq의 3번째 톱니 비교
            if gear[seq + 1][6] == gear[seq][3]:
                continue
            else:
                # nth_gear - 1 ~ seq + 1 까지 기어 돌리기
                # seq + 1이 nth_gear - 1 이면 안함
                for i in range(nth_gear-2, seq, -1):
                    # 홀수 만큼 떨어짐 : direction과 반대
                    if (nth_gear - 1 - seq) & 1:
                        pass
                    # 짝수 만큼 떨어짐 : direction 방향
                    else:
                        pass

                break

        else:
            # 0 ~ nth 기어 까지 돌리기
            pass
        
        # nth 기어보다 뒤에 있는 바퀴
        for seq in range(nth_gear, len(gear)):
            # seq - 1의 3번째 톱니와 seq의 7번째 톱니 비교
            if gear[seq - 1][3] == gear[seq][6]:
                continue
            else:
                # nth_gear ~ seq - 1 까지 기어 돌리기
                # seq + 1이 nth_gear - 1 이면 안함

                # 홀수 만큼 떨어짐 : direction과 반대
                if (nth_gear - 1 - seq) & 1:
                    pass
                # 짝수 만큼 떨어짐 : direction 방향
                else:
                    pass

                break
        else:
            # nth ~ len(gear) 기어 까지 돌리기
            pass

        print(nth_gear, direction)
