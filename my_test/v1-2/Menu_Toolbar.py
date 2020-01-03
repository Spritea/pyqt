import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QAction, QTextBrowser, QDockWidget,QSpinBox,QFileDialog
from PyQt5.QtGui import QIcon, QPixmap,QImage
from PyQt5.QtCore import Qt

def my_func_ext(self):
    self.statusBar().showMessage('kkkkkk')
def load_func_ext(self):
    self.label.setPixmap(self.pixmap)
    self.spin.setValue(100)
    self.pic_scale()
def open_file_ext(self):
    fname = QFileDialog.getOpenFileName(self, 'Open file', '/')
    self.current_path=fname[0]
    self.img_ori=QImage(fname[0])
    self.ori_width = self.img_ori.width()
    self.ori_height = self.img_ori.height()
    self.pixmap = QPixmap.fromImage(self.img_ori)
    self.load_func()
    self.textbrowser.append('Open file %s' %fname[0])
def save_file_ext(self):
    fname_save=QFileDialog.getSaveFileName(self,'Save file','/','Image(*.png,*.jpg,*.tif)')
    img_save=self.img_ori
    img_save.save(fname_save[0])
    self.textbrowser.append('Save file %s' % fname_save[0])
def clear_log_ext(self):
    self.textbrowser.clear()
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
    openAct = QAction(QIcon('../pic/Open.png'), 'Open', self)
    openAct.setStatusTip('Open file')
    openAct.triggered.connect(self.open_file)

    exitAct = QAction(QIcon('../pic/Close.png'), 'Exit', self)
    exitAct.setStatusTip('Exit application')
    exitAct.triggered.connect(self.close)

    saveAct = QAction(QIcon('../pic/Save.png'), 'Save', self)
    saveAct.setStatusTip('Save file')
    saveAct.triggered.connect(self.save_file)

    clearAct=QAction(QIcon('../pic/Break.png'), 'Clear', self)
    clearAct.setStatusTip('Clear log')
    clearAct.triggered.connect(self.clear_log)

    myAct=QAction('my',self)
    myAct.triggered.connect(self.my_func)
    # myAct.triggered.connect(self.statusBar().showMessage('kkkkkk'))
    loadAct=QAction('load',self)
    loadAct.triggered.connect(self.load_func)

    menubar = self.menuBar()
    fileMenu = menubar.addMenu('File')
    fileMenu.addAction(openAct)
    fileMenu.addAction(saveAct)
    fileMenu.addAction(clearAct)

    fileMenu.addAction(exitAct)

    myMenu=menubar.addMenu('my')
    myMenu.addAction(myAct)
    menu_load=menubar.addMenu('load')
    menu_load.addAction(loadAct)

    toolbar = self.addToolBar('TBar')

    toolbar.addAction(openAct)
    toolbar.addAction(saveAct)
    toolbar.addAction(clearAct)

    toolbar.addAction(exitAct)

    self.spin=QSpinBox(self)
    self.spin.setRange(40, 150)
    self.spin.setSingleStep(10)
    self.spin.setSuffix("%")
    self.spin.setSpecialValueText("Original")
    self.spin.setValue(100)
    toolbar.addWidget(self.spin)
    self.spin.valueChanged.connect(self.pic_scale)

