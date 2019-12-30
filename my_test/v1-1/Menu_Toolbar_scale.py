import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QAction, QTextBrowser, QDockWidget,QSpinBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

def my_func_ext(self):
    self.statusBar().showMessage('kkkkkk')
def load_func_ext(self):
    self.label.setPixmap(self.pixmap)
    self.spin.setValue(100)
    self.pic_scale()

def pic_scale_ext(self):
    spin_value=self.spin.value()
    spin_factor=spin_value/100
    scroll_width=self.scroll.width()-50
    scroll_height=self.scroll.height()-50
    print(self.scroll.height(),self.scroll.width())
    if spin_value==40:
        target_width=self.ori_width
        target_height=self.ori_height
    else:
        target_width=spin_factor*scroll_width
        target_height=spin_factor*scroll_height
    print(target_height,target_width)
    #-10 for not fulfill the whole area
    # ori_width=self.img_ori.width()
    # ori_height=self.img_ori.height()
    # ori_length=ori_width if ori_width>=ori_height else ori_height
    # final_factor=spin_factor*scroll_width/ori_length

    scaled_img=self.img_ori.scaled(target_width,target_height,Qt.KeepAspectRatio)
    self.pixmap = QPixmap.fromImage(scaled_img)
    scaled_width=scaled_img.width()
    scaled_height=scaled_img.height()
    self.label.resize(scaled_width,scaled_height)
    self.label.setPixmap(self.pixmap)

    print('kk')
    print(spin_value)

def setMenu_toolBar_ext(self):
    exitAct = QAction(QIcon('../pic/TS.jpg'), 'Exit', self)
    exitAct.setToolTip('Exit application')
    exitAct.triggered.connect(self.close)

    myAct=QAction('my',self)
    myAct.triggered.connect(self.my_func)
    # myAct.triggered.connect(self.statusBar().showMessage('kkkkkk'))
    loadAct=QAction('load',self)
    loadAct.triggered.connect(self.load_func)

    menubar = self.menuBar()
    fileMenu = menubar.addMenu('File')
    fileMenu.addAction(exitAct)
    myMenu=menubar.addMenu('my')
    myMenu.addAction(myAct)
    menu_load=menubar.addMenu('load')
    menu_load.addAction(loadAct)

    toolbar = self.addToolBar('Exit')
    toolbar.addAction(exitAct)
    self.spin=QSpinBox(self)
    self.spin.setRange(40, 150)
    self.spin.setSingleStep(10)
    self.spin.setSuffix("%")
    self.spin.setSpecialValueText("Original")
    self.spin.setValue(100)
    toolbar.addWidget(self.spin)
    self.spin.valueChanged.connect(self.pic_scale)

