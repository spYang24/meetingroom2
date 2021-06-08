from PyQt5.QtCore import QPointF, QRect
from PyQt5.QtGui import QFont
from threading import Thread, Lock
from random import randint
from time import sleep
 
# 튜플 단어장
kor = ('문자열', '정수', '리스트', '튜플', '딕셔너리',
      '타입', '출력', '반복문', '변수' )
eng = ('input', 'int', 'string', 'type', 'list', 'class',
      'print', 'python', 'tuple', 'for', 'if', 'while',
     'thread', 'random', 'with', 'commit' )

score=0

class CWord:
 
    def __init__(self, pt, word):
        # 단어 좌표
        self.pt = pt
        # 단어 문자
        self.word = word        
 
 
class CMap:
 
    def __init__(self, parent):
        self.parent = parent
        self.rect = parent.rect()
        self.word = []
        self.thread = Thread(target=self.play)        
        self.bthread = False       
        self.lock = Lock()
 
    def __del__(self):
        self.gameOver()

    def gameStart(self, lang, level):
        self.lang = lang
        self.level = level
 
        self.bthread = True       
        if self.thread.is_alive() == False:
            self.thread = Thread(target=self.play)            
            self.thread.start()        
 
    def gameOver(self):
        self.bthread = False
        self.word.clear()
        self.parent.update()
 
    def draw(self, qp):
        qp.setFont(QFont('맑은 고딕', 12))
        self.lock.acquire()
        for w in self.word:
            qp.drawText(w.pt, w.word)        
        self.lock.release()

    def createWord(self):  
         
        self.rect= QRect(self.parent.rect())
         
        # 무작위 단어 선정
        str = ''
        if self.lang==0:
            n = randint(0, len(kor)-1)
            str = kor[n]
        else:
            n = randint(0, len(eng)-1)
            str = eng[n]
 
        # 무작위 좌표 선정
        x = randint(0, self.rect.width()-50)
        y = 0
 
        cword = CWord(QPointF(x,y), str)
        self.word.append(cword)

    def downWord(self, speed):      
 
        i=0
        for w in self.word[:]:
            if w.pt.y() < self.rect.bottom():
                w.pt.setY(w.pt.y()+speed)
                i+=1
            else:
                del(self.word[i])



    def delword(self, str):
        global score
        self.lock.acquire()
 
        i=0
        find = False
        for w in self.word[:]:
            if str == w.word:
                score += 3
                print(score)
                del(self.word[i])
                find = True
                break
            else:
                i+=1
        self.lock.release()
 
        if find:
            self.parent.update()
 
    def play(self):
 
        while self.bthread:
 
            if randint(1,200) == 1:
                self.lock.acquire()
                self.createWord()
                self.lock.release()
 
            self.lock.acquire()
            if self.level == 0:
                #김예영 학우님
                if score < 10:#임의로 score에 변화를 주었음..
                    self.downWord(0.3)
                elif 10 <= score <20:
                    self.downWord(0.5)
                else:
                    self.downWord(0.7)
            elif self.level == 1:
                if score < 10:
                    self.downWord(0.7)
                elif 10 <= score <20:
                    self.downWord(1.0)
                else:
                    self.downWord(1.5)
            else:
                if score < 10:
                    self.downWord(1.5)
                elif 10 <= score <20:
                    self.downWord(1.7)
                else:
                    self.downWord(2.0)
            self.lock.release()
 
            self.parent.update()
            sleep(0.01)   
