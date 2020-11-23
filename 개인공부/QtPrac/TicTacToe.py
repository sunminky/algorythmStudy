#객체지향프로그래밍 팀프로젝트
#틱택토 게임 만들기

import sys
import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

CalUI = "calculator.ui"

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(CalUI, self)

        self.num_pushButton_0.clicked.connect(
            lambda state, button=self.num_pushButton_0: self.NumClicked(state, button))
        self.num_pushButton_1.clicked.connect(
            lambda state, button=self.num_pushButton_1: self.NumClicked(state, button))
        self.num_pushButton_2.clicked.connect(
            lambda state, button=self.num_pushButton_2: self.NumClicked(state, button))
        self.num_pushButton_3.clicked.connect(
            lambda state, button=self.num_pushButton_3: self.NumClicked(state, button))
        self.num_pushButton_4.clicked.connect(
            lambda state, button=self.num_pushButton_4: self.NumClicked(state, button))
        self.num_pushButton_5.clicked.connect(
            lambda state, button=self.num_pushButton_5: self.NumClicked(state, button))
        self.num_pushButton_6.clicked.connect(
            lambda state, button=self.num_pushButton_6: self.NumClicked(state, button))
        self.num_pushButton_7.clicked.connect(
            lambda state, button=self.num_pushButton_7: self.NumClicked(state, button))
        self.num_pushButton_8.clicked.connect(
            lambda state, button=self.num_pushButton_8: self.NumClicked(state, button))
        self.num_pushButton_9.clicked.connect(
            lambda state, button=self.num_pushButton_9: self.NumClicked(state, button))

        self.sign_pushButton_1.clicked.connect(
            lambda state, button=self.sign_pushButton_1: self.NumClicked(state, button))
        self.sign_pushButton_2.clicked.connect(
            lambda state, button=self.sign_pushButton_2: self.NumClicked(state, button))
        self.sign_pushButton_3.clicked.connect(
            lambda state, button=self.sign_pushButton_3: self.NumClicked(state, button))
        self.sign_pushButton_4.clicked.connect(
            lambda state, button=self.sign_pushButton_4: self.NumClicked(state, button))

        self.reset_pushButton.clicked.connect(
            lambda state, button=self.reset_pushButton: self.clearButton(state, button))


    def NumClicked(self, state, button):
        #print(f"{button.text()}번 버튼이 눌렷을 때 반응하는 함수")
        self.q_lineEdit.setText(f"{button.text()}번 버튼이 글자 입력함")
        self.del_pushButton.setStyleSheet("image:url(smile.png)")
        
    def clearButton(self, state, button):
        print(f"{state} 상태 입력창 초기화")
        self.q_lineEdit.clear()
        self.del_pushButton.setStyleSheet("image:url(frog.jpeg)")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_dialog = MainDialog()
    main_dialog.show()
    app.exec_()