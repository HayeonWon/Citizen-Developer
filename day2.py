#####====================Intro====================#####
# GUI : 그래픽 사용자 인터페이스. graphic user interface
# GUI 프로그래밍을 위한 여러 파이썬 모듈이 존재함 - TkInter, wxPython, PyQT

# from PyQT5.QTWidgets import -> PyQT5 폴더 안의 QTwidgets 파일을 가져오겠다
# app = QA~ -> 메모리 상의 QA~를 app이 바인딩
# exec_()를 실행하면 프로그램이 죽지 않고 실행됨
# QLabel은 문자열을 보여주는 데 최적화된 클래스

import sys
from PyQt5.QtWidgets import QApplication, QLabel # PyQT5 폴더 안의 QTwidgets 파일을 가져와서 QApplication~ 임포트
QApplication(sys.argv)

# 또 다른 방법
# import sys as argv # sys.py 파일로부터 argv를 가져오겠다
QApplication(argv)

# Hello World 실행
# import sys
# from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)

lb = QLabel("Hello World")
lb.show()

app.exec() # 1. 종료되지 않고 실행, 2. 이벤트 처리를 해줌


#####====================윈도우 만들기====================#####
# 기본 포맷
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

class MyWin(QMainWindow):
    def __init__(self):
        super().__init__()

        #...

app = QApplication()

mw = MyWin()
mw.show() # 보여주기
mw.hide() # 숨기기

app.exec()

# 윈도우 크기 조절
# from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

class MyWin(QMainWindow):
    def __init__(self): 
        super().__init__()

        super().move(0, 0)
        self.resize(400, 300) # resize(width, height) # self가 가리키는 것 : MyWin 객체
        self.setWindowTitle("Hello World") 

app = QApplication()
mw = MyWin()
mw.show()
app.exec()

# 윈도우 아이콘
from PyQt5.QtGui import QIcon
class MyWin(QMainWindow):
    def __init__(self): 
        super().__init__()

        super().move(0, 0)
        self.resize(400, 300) # resize(width, height) # self가 가리키는 것 : MyWin 객체
        self.setWindowTitle("Hello World")
        icon = QIcon("title.png")
        # icon = QIcon(".../title.png") # 디렉토리 외 절대 경로에서 title.png 불러오기
        # icon = QIcon("2일차/title.png") # 디렉토리의 2일차 폴더에서 title.png 불러오기
        self.setWindowIcon(icon)

app = QApplication()
mw = MyWin()
mw.show()
app.exec()

# 버튼 만들기 - 아이콘 없이
from PyQt5.QtWidgets import QPushButton
class MyWin(QMainWindow):
    def __init__(self):
        super().__init__()

        QPushButton(text='버튼!!', parent=self)
        #self.btn = QPushButton(text='버튼!!', parent=self) # self.btn에 할당 가능

app = QApplication()
mw = MyWin()
mw.show()
app.exec()

# 버튼 만들기 - 아이콘 있게
from PyQt5.QtWidgets import QPushButton
class MyWin(QMainWindow):
    def __init__(self):
        super().__init__()

        icon = QIcon("title.png")
        self.btn = QPushButton(icon, text='버튼!!', parent=self)
        #self.btn.move(30, 30) # 메인 윈도우를 기준으로 오른쪽으로 30, 아래쪽으로 30 이동
        qp = QPoint(30,30)
        self.btn.move(qp)

app = QApplication()
mw = MyWin()
mw.show()
app.exec()

# 버튼 클릭 이벤트 처리 (1/2)
class MyWin(QMainWindow):
    def __init__(self):
        super().__init__()

        icon = QIcon("title.png")
        self.btn = QPushButton(icon, text='버튼!!', parent=self)
        #self.btn.move(30, 30) # 메인 윈도우를 기준으로 오른쪽으로 30, 아래쪽으로 30 이동
        qp = QPoint(30,30)
        self.btn.move(qp)

        self.btn.clicked.connect(self.clickBtn)

    def clickBtn(self):
        print("click")

app = QApplication()
mw = MyWin()
mw.show()
app.exec()


# 연습문제 - 1
# 내 풀이
class MyWin(QMainWindow):
    def __init__(self):
        super().__init()

        self.btn1 = QPushButton(text='1', parent=self)
        self.btn2 = QPushButton(text='2', parent=self)
        self.btn3 = QPushButton(text='3', parent=self)
        self.btn4 = QPushButton(text='4', parent=self)

        qp1 = QPoint(-30,-30)
        qp2 = QPoint(30,-30)
        qp3 = QPoint(-30,30)
        qp4 = QPoint(30,30)

        self.btn1.move(qp1)
        self.btn2.move(qp2)
        self.btn3.move(qp3)
        self.btn4.move(qp4)
app = QApplication()
mw = MyWin()
mw.show()
app.exec()

# 정답
class MyWin(QMainWindow):
    def __init__(self):
        super().__init()

        self.btn1 = QPushButton(text='1', parent=self)
        self.btn1.move(0,0)
        self.btn1.clicked.connect(self.clickBtn)

        self.btn2 = QPushButton(text='2', parent=self)
        self.btn2.move(60,0)
        self.btn2.clicked.connect(self.clickBtn)

        self.btn3 = QPushButton(text='3', parent=self)
        self.btn3.move(0,30)
        self.btn3.clicked.connect(self.clickBtn)
        
        self.btn4 = QPushButton(text='4', parent=self)
        self.btn4.move(60,30)
        self.btn4.clicked.connect(self.clickBtn)

        def clickBtn(self):
            # 누가 이벤트를 만들었는가?
            # self : MyWin 객체
            who = self.sender()
            # print(type(who), id(who))
            print(who.text()) # QPushButton의 text 가져옴

app = QApplication()
mw = MyWin()
mw.show()
app.exec()


# 레이블 위젯 생성 
# 버튼을 클릭하면 login, 또 클릭하면 logout, 또 클릭하면 login이 뜨도록 하는 위젯 만들기
class MyWin(QMainWindow):
    def __init__(self):
        super().__init()

        self.btn1 = QPushButton("click", self)
        self.btn1.move(10,50)
        self.btn1.clicked.connect(self.clickBtn)

        self.lb = QLabel("login", self)

        self.toggleFlag = True

    def clickBtn(self):
        if self.toggleFlag == True:
            self.lb.setText("login")
            self.toggleFlag = False
        else:
            self.lb.setText("logout")
            self.toggleFlag = True

app = QApplication([])
mw = MyWin()
mw.show()
app.exec()


# 연습문제 - 3
# QLabel 객체에 1부터 10까지 순차 증가하는 숫자를 출력하라. (버튼 클릭 x)
class MyWin(QMainWindow):
    def __init__(self):
        super().__init()

        self.lb = QLabel("", self)

        for i in range(10):
            self.lb.setText(f"{i}")
            time.sleep(1) # 여기서 끝내면 창에 9만 출력됨
                          # 실제로 화면에 그리는 건 이벤트 loop이 함.
                          # !!! QTimer를 사용하면 가능 !!!
app = QApplication()
mw = MyWin()
mw.show()
app.exec()                        


#####====================QTimer====================#####
from PyQt5.QtCore import QTimer
import time

class MyWin(QMainWindow):
    def __init__(self):
        super().__init__()

        self.lb = QLabel("", self)

        t = QTimer(parent=self)
        t.start(1000)
        t.timeout.connect(self.getTimeEvent) 

        self.idx = 0
     
    def getTimeEvent(self): # 보통 class는 소문자로 시작. 클래스명에 커서 두고 F2 눌러서 변경하면 한꺼번에 변경 가능
        pself.lb.setText(f"{self.idx}")
        if self.idx < 10:
            self.idx += 1

app = QApplication()
mw = MyWin()
mw.show()
app.exec()

            

#####====================QThread====================#####
from PyQt5.QtCore import QThread

class Worker(QThread): # worker thread를 여기서 만들고
    def run(self):
        while True:
            print('hello')
            time.sleep(2)

class MyWin(QMainWindow):
    def __init__(self):
        super().__init()

        self.th = QThread()
        self.th.start() # Mywin에서 worker thread 호출!

app = QApplication()
mw = MyWin()
mw.show()
app.exec()

# 버튼을 클릭하면 thread가 실행되도록 코딩하라.
# 하나의 process는 하나의 main thread, 부모 thread라고 부른다.
# 추가적으로 만든 thread는 work thread, 자식 thread라고 부르며, 복잡한 연산은 여기서 처리하도록 해야 빠르다.
class MyWin(QMainWindow):
    def __init__(self):
        super().__init()

        self.th = Worker()

        self.btn = QPushButton("click", self)
        self.btn.clicked.connect(self.clickBtn)

    def clickBtn(self):
        self.th.start()


app = QApplication()
mw = MyWin()
mw.show()
app.exec()

# pyqt의 signal을 class로 정의해야 한다고 생각하기
from PyQt5.QtCore import QThread, pyqtSignal
import time

class BtcPriceWorker(QThread):
    price = pyqtSignal(int)

    def run(self):
        while True:
            # 가격 조회 
            price1 = 100 # 일반 변수로서의 price1
            price2 = 200

            # 이벤트 발생
            self.price.emit(price1, price2) # BtcPriceWorker 클래스 내의 price
            time.sleep(1)

class MyWin(QMainWindow):
    def __init__(self):
        super().__init__()

        self.btc = BtcPriceWorker()
        self.btc.price.connect(self.getPrice)
        self.btc.start() # start 안해주면 BtcPriceWorker가 실행 안 됨.

    def getPrice(self, price1, price2):
        print(price1, price2)

app = QApplication()
mw = MyWin()
mw.show()
app.exec()

#####====================QT Designer====================#####
# QT Designer 창 내에서 미리보기 단축키 ctrl + R
from PyQt5 import uic

class MyWin(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("new.ui")
        
        self.btn0.clicked.connect(self.clickBtn)

    def clickBtn(self):
        print("btn click")

app = QApplication()
mw = MyWin()
mw.show()
app.exec()


#####====================다양한 변형====================#####
# list widget 생성하기
class MyWin(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("lw.ui", self)

        item = QListWidgetItem('삼성메디슨')
        self.lw.addItem(item)

    def clickBtn(self):
        print("btn click")

app = QApplication()
mw = MyWin()
mw.show()
app.exec()

# QListWidget 사용하기
class MyWin(QMainWindow):
    def __init__(self):
        super().__init__()

        item = QListWidgetItem('삼성메디슨')
        self.lw.addItem(item)
        item = self.lw.item(0)
        print(item.text())

        self.lw.itemClicked.connect(self.clickItem)

    def clickItem(self, item):
        print(type(item), item.text())
        item.setText()

app = QApplication()
mw = MyWin()
mw.show()
app.exec()


# QComboBox 사용하기
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtCore import QVariant
from PyQt5.QtGui import QIcon

class MyWin(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('cb.ui', self)

        v = QVariant('00001')
        self.cb.addItem('삼성메디슨', v)

        self.btn.clicked.connect(self.clickBtn)

    def clickBtn(self):
        self.cb.currentText()


app = QApplication()
mw = MyWin()
mw.show()
app.exec()


