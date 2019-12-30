import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QAction, QTextBrowser, QDockWidget,QScrollArea
from PyQt5.QtGui import QIcon, QPixmap,QImage
from PyQt5.QtCore import Qt
from Menu_Toolbar import *

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    setMenu_toolBar=setMenu_toolBar_ext
    my_func=my_func_ext
    pic_scale=pic_scale_ext
    load_func=load_func_ext
    open_file=open_file_ext
    save_file=save_file_ext
    clear_log=clear_log_ext

    def initUI(self):
        self.label = QLabel(self)
        # self.label.setScaledContents(True)
        self.img_ori=QImage('../pic/TS.jpg')
        # self.img_ori=QImage('../pic/top_mosaic_09cm_area31.tif')
        self.pixmap=QPixmap.fromImage(self.img_ori)
        self.ori_width = self.img_ori.width()
        self.ori_height=self.img_ori.height()
        # self.label.setPixmap(self.pixmap)
        self.label.setAlignment(Qt.AlignCenter)
        self.scroll=QScrollArea()
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setWidget(self.label)

        self.dock = QDockWidget('LOG', self)
        self.textbrowser = QTextBrowser(self)
        self.dock.setWidget(self.textbrowser)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)
        self.textbrowser.setText('k\nkk')

        self.setMenu_toolBar()
        self.statusBar()


        # self.scroll.setWidgetResizable(True)
        # self.scroll.setFixedWidth(700)
        # self.scroll.setFixedHeight(700)
        self.scroll.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.scroll)

        self.setGeometry(300, 300, 900, 700+19)
        self.setWindowTitle('Main window')
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
