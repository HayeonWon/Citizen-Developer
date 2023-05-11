from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5 import uic

# 연습문제 1-(1)
class MyWin(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:/Users/dseduoa.edu/Desktop/lw_ex.ui",self)
        # self.btn.clicked.connect(self.clickBtn) # btn이 클릭됐을 때 일어나는 이벤트를 connect라는 메서드에 연결

    def clickBtn(self):
        # 1)
        idx = self.lw_ex.currentRow() # 행을 return 해줌
        print(idx)

app = QApplication([ ])
mw = MyWin()
mw.show()
app.exec()
        

# 연습문제 1-(2)
class MyWin(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("C:/Users/dseduoa.edu/Desktop/lw_ex.ui", self)

        self.btn.clicked.connect(self.clickBtn) # btn이 클릭됐을 때 일어나는 이벤트를 connect라는 메서드에 연결
        self.lw.itemClicked.connect(self.clickLw)
        self.isSelect = False # 선택을 하면 true로 바꿔주기

    def clickLw(self, item):
        self.isSelect = True

    def clickBtn(self):
        if self.isSelect is False:
            # print("없음")
            self.statusbar.showMessage("없음") # statusbar의 결과가 출력됨
        else: # 사용자가 item을 클릭하면 true로 바뀌도록 하기 위해 click에 대한 event 정의하기
            # # 1)
            # idx = self.lw.currentRow() # 행을 return 해줌
            # print(idx)

            # 2)
            item = self.lw.currentItem()
            self.statusbar.showMessage(item.text())

app = QApplication([ ])
mw = MyWin()
mw.show()
app.exec()


# 연습문제 1-(2)
class MyWin(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("C:/Users/dseduoa.edu/Desktop/lw_ex.ui", self)

        self.btn.clicked.connect(self.clickBtn) 
        self.lw.itemClicked.connect(self.clickLw)
        self.isSelect = False 

        for idx in range(self.lw.count()):
            data = self.lw.item(idx)
            print(data.text())

app = QApplication([ ])
mw = MyWin()
mw.show()
app.exec()


# 연습문제 : radiobutton A, B, C 출력하기
conda activate base
C:/Users/dseduoa.edu/AppData/Local/anaconda3/python.exe

from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5 import uic
import sys
QApplication(sys.argv)

class MyWin(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("C:/Users/dseduoa.edu/Desktop/rb.ui", self)
        
        self.radioButton_1.clicked.connect(self.click_1)
        self.radioButton_2.clicked.connect(self.click_2)
        self.radioButton_3.clicked.connect(self.click_3)

    def click_1(self):
        print(self.radioButton_1.text())

    def click_2(self):
        print(self.radioButton_2.text())

    def click_3(self):
        print(self.radioButton_3.text())

app = QApplication(sys.argv)
mw = MyWin()
mw.show()
app.exec()


# 연습문제 : radiobutton A, B, C 출력하기
conda activate base
C:/Users/dseduoa.edu/AppData/Local/anaconda3/python.exe

from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5 import uic
import sys
QApplication(sys.argv)

class MyWin(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("C:/Users/dseduoa.edu/Desktop/rb.ui", self)
        
        self.radioButton_1.clicked.connect(self.click)
        self.radioButton_2.clicked.connect(self.click)
        self.radioButton_3.clicked.connect(self.click)

    def click(self):
        who = self.sender()
        print(who.text())

app = QApplication(sys.argv)
mw = MyWin()
mw.show()
app.exec()


# 연습문제 : tablewidget 창 띄우기
class MyWin(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("C:/Users/dseduoa.edu/Desktop/tb.ui", self)

        print(self.tb)

app = QApplication(sys.argv)
mw = MyWin()
mw.show()
app.exec()


# 연습문제 : tablewidget 창 띄우기 - 더블클릭하면 값 나오게
class MyWin(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("C:/Users/dseduoa.edu/Desktop/tb.ui", self)

        self.tb.cellDoubleClicked.connect(self.clickTb)

    def clickTb(self, row, col):
        print(row, col)
        self.tb.item(row, col)
        print(type(item), item)

app = QApplication(sys.argv)
mw = MyWin()
mw.show()
app.exec()


# 연습문제 : tablewidget 창 띄우기 - 더블클릭하면 값 나오게 - 창 꺼지지 않게
class MyWin(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("C:/Users/dseduoa.edu/Desktop/tb.ui", self)

        self.tb.cellDoubleClicked.connect(self.clickTb)

    def clickTb(self, row, col):
        item = self.tb.currentItem()
        print(type(item), item.text())

app = QApplication(sys.argv)
mw = MyWin()
mw.show()
app.exec()

# 연습문제 - 프로그램 실행 시 데이터 읽어서 채워넣기
# data.txt
# 안녕
# 반가워

# name.txt
# 라이언
# 어피치

# 안녕 | 라이언
# 반가워 | 어피치
with open("C:/Users/dseduoa.edu/Desktop/name.txt", "r", encoding='utf-8') as f: # "r"-읽기모드로 열기
    line = f.readline()
    print(line.strip())
    line = f.readline()
    print(line.strip())

f = open("C:/Users/dseduoa.edu/Desktop/name.txt", "r", encoding='utf-8')
f.close() # 파일 열고나면 반드시 닫아주기


conda activate base
C:/Users/dseduoa.edu/AppData/Local/anaconda3/python.exe

from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5 import uic
import sys
QApplication(sys.argv)


class MyWin(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("C:/Users/dseduoa.edu/Desktop/tb.ui", self)
        # self.tb.cellDoubleClicked.connect(self.clickTb)

        with open("C:/Users/dseduoa.edu/Desktop/name.txt", "r", encoding='utf-8') as f: # "r"-읽기모드로 열기
            line = f.readline()
            item = self.tb.item(0,1)
            item.setText(line.strip())

            line = f.readline()
            item = self.tb.item(1,1)
            item.setText(line.strip())

        with open("C:/Users/dseduoa.edu/Desktop/data.txt", "r", encoding='utf-8') as f:
            line = f.readline()
            item = self.tb.item(0,0)
            item.setText(line.strip())

            line = f.readline()
            item = self.tb.item(1,0)
            item.setText(line.strip())

app = QApplication(sys.argv)
mw = MyWin()
mw.show()
app.exec()





