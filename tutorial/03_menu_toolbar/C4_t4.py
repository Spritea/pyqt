import sys
from PyQt5.QtWidgets import QMainWindow,QAction,qApp,QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        exitAct=QAction(QIcon('../pic/TS.jpg'),'Exit',self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)

        self.toolbar=self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('absolute')
        self.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec())