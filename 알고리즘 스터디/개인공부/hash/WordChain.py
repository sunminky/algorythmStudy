# https://programmers.co.kr/learn/courses/30/lessons/12981
def solution(n, words):
    prev = words[0]
    exposed = {words[0]: True}

    for turn in range(1, len(words)):
        if exposed.get(words[turn], False):
            return [(turn % n) + 1, (turn // n) + 1]
        if words[turn][0] != prev[-1]:
            return [(turn % n) + 1, (turn // n) + 1]

        exposed[words[turn]] = True
        prev = words[turn]

    return [0, 0]


if __name__ == '__main__':
    solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])  # [3, 3]
    solution(5, [
        "hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang",
        "gather", "refer", "reference", "estimate", "executive"])  # [0, 0]
    solution(2, ["hello", "one", "even", "never", "now", "world", "draw"])  # [1, 3]
