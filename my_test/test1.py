import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QAction, QTextBrowser,QDockWidget
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import Qt

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()
    def setMenu_toolBar(self):
        exitAct = QAction(QIcon('pic/TS.jpg'), 'Exit', self)
        exitAct.setToolTip('Exit application')
        exitAct.triggered.connect(self.close)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAct)
    def initUI(self):
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('pic/TS.jpg'))
        self.setCentralWidget(self.label)

        self.dock=QDockWidget('LOG',self)
        self.textbrowser=QTextBrowser(self)
        self.dock.setWidget(self.textbrowser)
        self.addDockWidget(Qt.RightDockWidgetArea,self.dock)

        self.setMenu_toolBar()
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

