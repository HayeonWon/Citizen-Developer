
conda activate base
C:/Users/dseduoa.edu/AppData/Local/anaconda3/python.exe

from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5 import uic
import sys
QApplication(sys.argv)

import os
os.chdir("C:/Users/dseduoa.edu/Desktop/project_folder/")
dir = os.getcwd()

# 단계 - 2 : 콤보박스
class MyWin(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("mini_project.ui", self)

        list = os.listdir(dir + "/txtfolder")

        self.cb.addItems(list)

app = QApplication(sys.argv)
mw = MyWin()
mw.show()
app.exec()


# 단계 - 3 : 텍스트 파일 내용 출력
class MyWin(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("mini_project.ui", self)

        list = os.listdir(dir + "/txtfolder")
        self.cb.addItems(list)
        self.pb.clicked.connect(self.showtext)

    def showtext(self):

        cbitem = self.cb.currentText()

        with open(dir + "/txtfolder/" + cbitem, "r", encoding='utf-8') as f: # "r"-읽기모드로 열기
            for i in range(0,10):
                line = f.readline()
                self.lw.addItem(line.strip())
                
app = QApplication(sys.argv)
mw = MyWin()
mw.show()
app.exec()


# 단계 - 4 : 암호화
class MyWin(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("mini_project.ui", self)

        list = os.listdir(dir + "/txtfolder")
        self.cb.addItems(list)
        self.pb.clicked.connect(self.showtext)

    def showtext(self):

        cbitem = self.cb.currentText()

        import hashlib

        str1 = "samsung"

        enc_str1 = hashlib.sha256(str1.encode()).hexdigest()

        with open(dir + "/txtfolder/" + cbitem, "r", encoding='utf-8') as f: # "r"-읽기모드로 열기
            for i in range(0,10):
                line = f.readline()
                self.lw.addItem(line.strip())
                # 암호화하기
                str = line
                enc_str = hashlib.sha256(str.encode()).hexdigest()

app = QApplication(sys.argv)
mw = MyWin()
mw.show()
app.exec()