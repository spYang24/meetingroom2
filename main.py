import sys
from window import *
 
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
 
if __name__ == '__main__':   
    app = QApplication(sys.argv)    
    w = CWidget()
    w.show()
    sys.exit(app.exec_())
###시험삼아..