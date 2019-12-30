import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QAction, QTextBrowser, QDockWidget
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

def my_func_ext(self):
    self.statusBar().showMessage('kkkkkk')

def setMenu_toolBar_ext(self):
    exitAct = QAction(QIcon('../pic/TS.jpg'), 'Exit', self)
    exitAct.setToolTip('Exit application')
    exitAct.triggered.connect(self.close)

    myAct=QAction('my',self)
    myAct.triggered.connect(self.my_func)
    # myAct.triggered.connect(self.statusBar().showMessage('kkkkkk'))


    menubar = self.menuBar()
    fileMenu = menubar.addMenu('File')
    fileMenu.addAction(exitAct)
    myMenu=menubar.addMenu('my')
    myMenu.addAction(myAct)

    toolbar = self.addToolBar('Exit')
    toolbar.addAction(exitAct)