import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QAction, QTextBrowser, QDockWidget,QScrollArea
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from Menu_Toolbar_set import *

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    setMenu_toolBar=setMenu_toolBar_ext
    my_func=my_func_ext


    def initUI(self):
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('../pic/top_mosaic_09cm_area31.tif'))
        self.scroll=QScrollArea()
        self.scroll.setWidget(self.label)
        # self.scroll.setWidgetResizable(True)
        # self.scroll.setFixedWidth(700)
        # self.scroll.setFixedHeight(700)

        self.setCentralWidget(self.scroll)

        self.dock = QDockWidget('LOG', self)
        self.textbrowser = QTextBrowser(self)
        self.dock.setWidget(self.textbrowser)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)
        self.textbrowser.setText('k\nkk')

        self.setMenu_toolBar()
        self.statusBar()
        self.setGeometry(300, 300, 900, 700)
        self.setWindowTitle('Main window')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
