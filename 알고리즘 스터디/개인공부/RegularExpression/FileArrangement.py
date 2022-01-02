# https://programmers.co.kr/learn/courses/30/lessons/17686
import re


def parsing(text: str, seq: int) -> list:
    pattern = r"[0-9]+"
    start_idx = re.search(pattern, text).start()
    end_idx = re.search(pattern, text).end()

    head = text[:start_idx].lower()
    number = int(text[start_idx:end_idx])

    return [head, number, seq, text]


def solution(files):
    table = sorted([parsing(e, seq) for seq, e in enumerate(files)])
    answer = [e[-1] for e in table]

    return answer


if __name__ == '__main__':
    solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
    # ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
    solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])
    # ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
    solution(["muzi1.txt", "MUZI1.txt", "muzi001.txt", "muzi1.TXT"])
    # muzi1.txt, MUZI1.txt, muzi001.txt, muzi1.TXT
