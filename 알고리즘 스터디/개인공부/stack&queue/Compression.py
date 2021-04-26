# https://programmers.co.kr/learn/courses/30/lessons/17684


def solution(msg):
    dictionary = dict(zip([chr(ch) for ch in range(65, 65+26)], range(1, 27)))
    answer = []
    seq = 0

    while seq < len(msg):
        seq2 = seq
        stack = []
        result = 0

        while seq2 < len(msg):
            stack.append(msg[seq2])

            if dictionary.get("".join(stack), False) is False:
                # 새로운 단어 추가
                dictionary["".join(stack)] = len(dictionary) + 1
                seq = seq2
                break

            result = dictionary["".join(stack)]
            seq2 += 1

        else:
            seq = seq2 + 1
            
        answer.append(result)

    return answer


if __name__ == '__main__':
    solution("KAKAO")  # [11, 1, 27, 15]
    solution("TOBEORNOTTOBEORTOBEORNOT")  # [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
    solution("ABABABABABABABAB")  # [1, 2, 27, 29, 28, 31, 30]
