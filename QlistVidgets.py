from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem
from PyQt5 import QtGui, QtCore
from settingFTP import SettingFtp

p = 'image/p.jpg'
f = 'image/f.jpg'

class List(QListWidget):
    def __init__(self, window1):
        super().__init__(window1)


    
    def lineWid(self, settingftp):
        def proverka(d):
            if d in self.catalogDirect:
                settingftp.directOpen(d)
            elif d in self.catalogBack:
                settingftp.directOpen(d)
            elif d in self.catalogFile:
                settingftp.namefile(d)

        self.catalogFile = ''
        self.catalogDirect = ''
        self.catalogBack = ''
        self.setSortingEnabled(False)
        self.resize(250, 490)
        self.move(500, 50)
        self.Pi = QtGui.QIcon(p)
        self.Fi = QtGui.QIcon(f)
        sz = QtCore.QSize()
        sz.setHeight(10)
        sz.setWidth(10)
        self.currentTextChanged.connect(proverka)



    def clearlist(self):
        self.clear()

    def addList(self, catalogback, catalogDir, catalogFile):
        self.catalogBack = catalogback
        self.catalogDirect = catalogDir
        self.catalogFile = catalogFile
        self.addItems(catalogback)
        for i in catalogDir:
            Direct = QListWidgetItem(self.Pi, i)
            self.addItem(Direct)
        for i in catalogFile:
            File = QListWidgetItem(self.Fi, i)
            self.addItem(File)
        
        
    