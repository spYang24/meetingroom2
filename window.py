from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from map1 import CMap
 


class CWidget(QWidget):
    def __init__(self):
        
        super().__init__()
 
        self.initUI()
 
    def initUI(self):
        
        #점수표시
        self.btn1 = QPushButton("0", self)        
        self.btn1.resize(self.btn1.sizeHint())
        self.btn1.move(0, 10)
        
        #생명력표시
        self.btn2 = QPushButton("5", self)
        self.btn2.resize(self.btn2.sizeHint())
        self.btn2.move(0, 50)
        
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
        self.setWindowTitle('파이썬 타자연습')
 
        self.map1 = CMap(self)
        
 

    def closeEvent(self, e):  
        c = 'GAME OVER'
        d = ('재도전 하시려면 Yes, 종료하시려면 No')
        react = QMessageBox.question(self, c,  d,
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if react == QMessageBox.Yes:
            e.ignore()
        else:
            e.accept()
            
              
        
    def paintEvent(self, e):
        qp = QPainter();
        qp.begin(self)
        self.map1.draw(qp)
        qp.end()
         
 
    def toggleButton(self, state):
        if state:
            self.map1.gameStart(self.lang.currentIndex(),
                              self.level.currentIndex())
            self.btn.setText('게임종료')
            scorereset = self.map1.score = 0
            self.btn1.setText(str(scorereset))
            countset = self.map1.count = 5
            self.btn2.setText(str(self.map1.count))
            self.lang.setEnabled(False)
            self.level.setEnabled(False)
        else:
            self.map1.gameOver()
            self.btn.setText('게임시작')
            self.lang.setEnabled(True)
            self.level.setEnabled(True)
 
    def keyPressEvent(self, e):
        # 계속 포커스를 가지도록
        self.edit.setFocus()
 
        # 엔터키 입력시 단어 확인
        if e.key() == Qt.Key_Return:
            self.map1.delword(self.edit.text())
            self.edit.setText('')
            self.btn1.setText(str(self.map1.score))
            self.map1.lifecount(self.edit.text())
            self.map1.aa = self.map1.count + self.map1.wd
            self.btn2.setText(str(self.map1.aa))   
            if self.map1.aa == 0:
                self.closeEvent(e)
                self.map1.gameOver()
                
            

               