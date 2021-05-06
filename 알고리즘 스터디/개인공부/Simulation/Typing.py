# https://programmers.co.kr/learn/courses/30/lessons/67256


key_location = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                4: (1, 0), 5: (1, 1), 6: (1, 2),
                7: (2, 0), 8: (2, 1), 9: (2, 2),
                -1: (3, 0), 0: (3, 1), -2: (3, 2)}


def distance(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


def solution(numbers, hand):
    hand = 'R' if hand == 'right' else 'L'
    answer = []
    right_hand = (3, 0)
    left_hand = (3, 2)
    for num in numbers:
        # 1, 4 , 7 인 경우
        if num in [1, 4, 7]:
            answer.append('L')
            left_hand = key_location[num]
        # 3, 6, 9 인 경우
        elif num in [3, 6, 9]:
            answer.append('R')
            right_hand = key_location[num]
        else:
            right_distance = distance(right_hand, key_location[num])
            left_distance = distance(left_hand, key_location[num])

            if right_distance > left_distance:
                answer.append('L')
                left_hand = key_location[num]
            elif left_distance > right_distance:
                answer.append('R')
                right_hand = key_location[num]
            # 둘의 거리가 같은 경우
            else:
                answer.append(hand)
                if hand == 'R':
                    right_hand = key_location[num]
                else:
                    left_hand = key_location[num]

    return "".join(answer)


if __name__ == '__main__':
    solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")  # "LRLLLRLLRRL"
    solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")  # "LRLLRRLLLRR"
    solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right")  # "LLRLLRLLRL"
