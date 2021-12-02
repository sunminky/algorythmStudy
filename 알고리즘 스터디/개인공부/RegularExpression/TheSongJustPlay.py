# https://programmers.co.kr/learn/courses/30/lessons/17683?language=python3
import re


def timeTovalue(time):
    hour, minute = map(int, time.split(':'))

    return hour * 60 + minute


def play(song, playtime):
    song_len = len(song)
    q, r = divmod(playtime, song_len)
    result = []

    for _ in range(q):
        result.append(song)

    result.append(song[:r])

    return "".join(result)


def replaceSharp(text):
    text = re.sub("C#", "H", text)
    text = re.sub("D#", "I", text)
    text = re.sub("F#", "J", text)
    text = re.sub("G#", "K", text)
    text = re.sub("A#", "L", text)

    return text


def find(target, pattern):
    # KMP로 구현할 수 있지만 귀찮쓰~
    return re.search(pattern, target)


def solution(m, musicinfos):
    songs = []
    m = replaceSharp(m)

    for info in musicinfos:
        song_start, song_end, title, song = info.split(',')
        song = replaceSharp(song)
        playtime = timeTovalue(song_end) - timeTovalue(song_start)

        songs.append((playtime, title, play(song, playtime)))

    songs.sort(key=lambda x: -x[0])

    for _, title, song in songs:
        if find(song, m):
            return title

    return "(None)"


if __name__ == '__main__':
    solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])  # "HELLO"
    solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])  # "FOO"
    solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])  # "WORLD"
