from tkinter import *
from tkinter import messagebox

scoreList = []

def calcAvg():
    ret = sum(scoreList) / len(scoreList)
    print(scoreList)
    labelAvgVal.config(text=ret)

def saveScore():
    scoreList.append(int(entry.get()))

window = Tk()   #윈도우 생성
window.geometry("300x150")     #윈도우 크기 지정
window.resizable(False,False)   #창크기 변경 불가능

labelScore = Label(window,text="점수")
labelScore.grid(column=0,row=0)
entry = Entry(window)
entry.grid(column=1,row=0)
labelAvg = Label(window,text="평균")
labelAvg.grid(column = 0, row = 1)
labelAvgVal = Label(window,text="")
labelAvgVal.grid(column = 1, row = 1)
buttonSave = Button(window, text = "저장", command = saveScore)
buttonSave.grid(column = 0, row = 2)
buttonSave = Button(window, text = "평균", command = calcAvg)
buttonSave.grid(column = 1, row = 2)

window.mainloop()   #입력대기, 이벤트 루프