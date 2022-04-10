# https://www.acmicpc.net/problem/1254
import sys

if __name__ == '__main__':
    text = sys.stdin.readline().rstrip()
    reverse_text = text[::-1]
    start_idx = text.find(reverse_text[0], 0)

    while start_idx != -1:
        if hash(text[start_idx:]) == hash(reverse_text[:len(text) - start_idx]):
            print(len(text) + start_idx)
            break

        start_idx = text.find(reverse_text[0], start_idx + 1)
