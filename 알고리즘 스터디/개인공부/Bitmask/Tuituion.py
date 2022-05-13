# https://www.acmicpc.net/problem/1062
import sys

bit_dict = dict()
alpha_dict = {
    'b': 1,
    'd': 2,
    'e': 4,
    'f': 8,
    'g': 16,
    'h': 32,
    'j': 64,
    'k': 128,
    'l': 256,
    'm': 512,
    'o': 1024,
    'p': 2048,
    'q': 4096,
    'r': 8192,
    's': 16384,
    'u': 32768,
    'v': 65536,
    'w': 131072,
    'x': 262144,
    'y': 524288,
    'z': 1048576,
}


def count_word(bit) -> int:
    result = 0

    for key in bit_dict.keys():
        if not bit ^ (bit | key):
            result += bit_dict[key]

    return result


def make_bit(remain, bit, seq):
    if remain == 0 or seq == 21:
        if remain:
            return 0

        return count_word(bit)

    return max(make_bit(remain, bit, seq + 1), make_bit(remain - 1, (1 << seq) | bit, seq + 1))


def get_bit(text):
    result = 0

    for ch in text:
        if ch in alpha_dict:
            result |= alpha_dict[ch]

    return result


if __name__ == '__main__':
    n_word, n_teach = map(int, sys.stdin.readline().split())
    answer = 0

    for _ in range(n_word):
        bit = get_bit(sys.stdin.readline().rstrip())

        bit_dict[bit] = bit_dict.get(bit, 0) + 1

    answer = make_bit(n_teach - 5, 0, 0)

    print(answer)
