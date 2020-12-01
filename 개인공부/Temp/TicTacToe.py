## 2020 객체지향프로그래밍 팀프로젝트 TicTacToe ##
from PyQt5 import uic
from PyQt5.QtWidgets import *
import sys
import random

class Game:
    def play(self, oppoent="COM"):
        #게임 시작
        self.field = Field()
        player = 1

        while self.field.remain:
            while True:
                if player == 1 and oppoent == "COM":
                    input_position = self.field.remain[random.randrange(0, len(self.field.remain))]
                    print(f"좌표입력 : {input_position}")
                else:
                    print("끝내고 싶으면 좌표에 9를 입력하세요")
                    input_position = int(input("좌표입력 : "))

                if input_position == 9: #9입력하면 종료
                    sys.exit(0)

                if not self.positioning(input_position, player, self.field):    #좌표 선택
                    break

            self.field.show_field() #게임판 출력

            winner = self.winner(input_position, self.field)
            if winner:
                print(f"플레이어{winner} 이김!")
                break

            player = -player    #상대 플레이어로 바꾸기
    
    def positioning(self, position, player, field):
        #좌표입력받기, x좌표 y좌표 입력받기 또는 0~8 숫자로 위치 지정
        if field.get_field_value(position): #이미 선택된 위치이면 다시 좌표 입력받게 함
            print("이미 둔 곳입니다. 다시입력하세요.")
            return -1
        field.positioning(position, player) #선택된 좌표를 게임판에 표시

    def winner(self, latest_position, field):
        #이긴 사람이 누구인지 출력
        player = 1 if field.get_field_value(latest_position) == 1 else 2
        #대각선 체크
        #오른쪽 위로 올라가는 대각선
        right_upper = [0, 4, 8]
        if latest_position in right_upper:
            if field.get_field_value(0) == field.get_field_value(4) == field.get_field_value(8):
                return player
        #오른쪽 아래로 내려가는 대각선
        right_lower = [2, 4, 6]
        if latest_position in right_lower:
            if field.get_field_value(2) == field.get_field_value(4) == field.get_field_value(6):
                return player
        #가로 체크
        if field.get_field_value(latest_position // 3 * 3) == field.get_field_value(latest_position // 3 * 3 + 1) == field.get_field_value(latest_position // 3 * 3 + 2):
            return player
        #세로 체크
        if field.get_field_value(latest_position % 3) == field.get_field_value(latest_position % 3 + 3) == field.get_field_value(latest_position % 3 + 6):
            return player
        #비기는 경우
        if not len(field.remain):
            print("비김")


class Field:
    symbols = {1: "O", -1: "X", None: " "}
    def __init__(self):
        #3x3 게임판 생성
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.remain = [i for i in range(9)]

    def positioning(self, position, player):
        #입력받은 좌표에 ox표시
        self.remain.remove(position)
        self.board[int(position) // 3][int(position) % 3] = player

    def get_field_value(self, position):
        #입력받은 좌표에 있는 게임판에 있는 값 반환
        return self.board[int(position) // 3][int(position) % 3]

    def show_field(self):
        #게임판 보여주기
        print("-------")
        print("", self.symbols[self.board[0][0]], self.symbols[self.board[0][1]], self.symbols[self.board[0][2]], "", sep="|")
        print("-------")
        print("", self.symbols[self.board[1][0]], self.symbols[self.board[1][1]], self.symbols[self.board[1][2]], "", sep="|")
        print("-------")
        print("", self.symbols[self.board[2][0]], self.symbols[self.board[2][1]], self.symbols[self.board[2][2]], "", sep="|")
        print("-------")
        print()

#GUI용
class Gui(QMainWindow):
    ui_path="gui.ui"

    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(self.ui_path, self)

        self.btn1.clicked.connect(
            lambda state, button=self.btn1: self.btn_clicked(state, button))
        self.btn2.clicked.connect(
            lambda state, button=self.btn2: self.btn_clicked(state, button))
        self.btn3.clicked.connect(
            lambda state, button=self.btn3: self.btn_clicked(state, button))
        self.btn4.clicked.connect(
            lambda state, button=self.btn4: self.btn_clicked(state, button))
        self.btn5.clicked.connect(
            lambda state, button=self.btn5: self.btn_clicked(state, button))
        self.btn6.clicked.connect(
            lambda state, button=self.btn6: self.btn_clicked(state, button))
        self.btn7.clicked.connect(
            lambda state, button=self.btn7: self.btn_clicked(state, button))
        self.btn8.clicked.connect(
            lambda state, button=self.btn8: self.btn_clicked(state, button))
        self.btn9.clicked.connect(
            lambda state, button=self.btn9: self.btn_clicked(state, button))

    def btn_clicked(self, state, button):
        print("눌림")

if __name__ == '__main__':
    '''app = QApplication(sys.argv)
    main_dialog = Gui()
    main_dialog.show()
    app.exec_()'''

    #Game().play(oppoent="person")   #사람과 게임
    Game().play()  #컴퓨터와 게임