## 2020 객체지향프로그래밍 팀프로젝트 TicTacToe ##

class Game:
    def play(self):
        #게임 시작
        pass
    
    def positioning(self, position, field):
        #좌표입력받기, x좌표 y좌표 입력받기 또는 0~8 숫자로 위치 지정
        pass

    def winner(self, field):
        #이긴 사람이 누구인지 출력
        pass


class Field:
    def __init__(self):
        #3x3 게임판 생성
        pass

    def positioning(self):
        #입력받은 좌표에 ox표시
        pass
    
    def show_field(self):
        #게임판 보여주기
        pass

if __name__ == '__main__':
    Game().play()   #게임실행