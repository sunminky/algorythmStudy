#https://programmers.co.kr/learn/courses/30/lessons/42579


class Song:
    def __init__(self, playtime, index):
        self.songs = [(playtime, index)]

    def add(self, playtime, index):
        self.songs.append((playtime, index))
        #곡 재생횟수에 따라 오름차순 정렬, 재생횟수가 같으면 인덱스 가 작은 순으로 정렬
        self.songs.sort(reverse=True, key=lambda x:(x[0], -x[1]))
        #재생횟수 상위 2개 곡 만 저장
        if len(self.songs) == 3:
            self.songs.pop()

    #재생횟수 상위 2개의 곡을 재생횟수가 많은 순서대로 반환
    def show(self):
        tmp = []
        while self.songs:
            tmp.append(self.songs.pop()[1])
        return list(reversed(tmp))


def solution(genres, plays):
    answer = []
    genre_count = dict()    #장르별 재생횟수 저장
    genre_songs = dict()    #노래별 재생횟수 상위 2개 저장

    for i, g in enumerate(genres):
        if not genre_count.get(g, False):
            genre_count[g] = plays[i]
            genre_songs[g] = Song(plays[i], i)
        else:
            genre_count[g] += plays[i]
            genre_songs[g].add(plays[i], i)

    #재생횟수가 높은 장르를 내림차순으로 정렬
    genre_list = sorted(list(zip(genre_count.values(), genre_count.keys())), reverse=True)

    for gl in genre_list:
        answer.extend(genre_songs[gl[1]].show())

    return answer

if __name__ == '__main__':
    solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500])   #[4, 1, 3, 0]