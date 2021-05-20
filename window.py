from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import map
 
class CWidget(QWidget):
    def __init__(self):
        super().__init__()
 
        self.initUI()
 
    def initUI(self):
 
        #컨트롤 레이아웃 박스
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
         
        #한글 영어 선택
        self.lang = QComboBox()
        self.lang.addItem('한글')
        self.lang.addItem('영어')
        self.lang.setCurrentIndex(0)
 
        #난이도
        self.level = QComboBox()
        self.level.addItem('초보자')
        self.level.addItem('중급자')
        self.level.addItem('전문가')
        self.level.setCurrentIndex(0)
 
        #단어 입력창
        self.edit = QLineEdit()        
 
        #게임 시작버튼
        self.btn = QPushButton('게임시작')
        self.btn.setCheckable(True)
        self.btn.toggled.connect(self.toggleButton)
 
        #수평 레이아웃 위젯 추가
        self.hbox.addWidget(self.lang)
        self.hbox.addWidget(self.level)
        self.hbox.addWidget(self.edit)
        self.hbox.addWidget(self.btn)
 
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.hbox)
        self.setLayout(self.vbox)
        self.setGeometry(100,100, 500,500)
        self.setWindowTitle('파이썬 문법 타자연습')
 
        self.map = map.CMap(self)
 
    def closeEvent(self, e):
        self.map.gameOver()
 
    def paintEvent(self, e):
        qp = QPainter();
        qp.begin(self)
        self.map.draw(qp)
        qp.end()
         
 
    def toggleButton(self, state):
        if state:
            self.map.gameStart(self.lang.currentIndex(),
                              self.level.currentIndex())
            self.btn.setText('게임종료')
            self.lang.setEnabled(False)
            self.level.setEnabled(False)
        else:
            self.map.gameOver()
            self.btn.setText('게임시작')
            self.lang.setEnabled(True)
            self.level.setEnabled(True)
 
    def keyPressEvent(self, e):
        # 계속 포커스를 가지도록
        self.edit.setFocus()
 
        # 엔터키 입력시 단어 확인
        if e.key() == Qt.Key_Return:
            self.map.delword(self.edit.text())
            self.edit.setText('')
