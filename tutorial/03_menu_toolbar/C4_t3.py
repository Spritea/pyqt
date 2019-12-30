import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication
class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        impMenu=QMenu('Import',self)
        #qmenu is used to add submenu
        impAct=QAction('Import mail',self)
        impMenu.addAction(impAct)

        newAct=QAction('New',self)
        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())