from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem
from PyQt5 import QtGui, QtCore
from settingFTP import SettingFtp
import os
import FtpFunc as FF
import sys

p = 'image/p.jpg'
f = 'image/f.jpg'

class List2(QListWidget):
    """класс для окна дирректории Files"""
    def __init__(self, window1):
        super().__init__(window1)

    
    
    def lineWid(self, settingftp):

        self.catalogFile = ''
        self.catalogDirect = ''
        self.catalogBack = ''
        self.setSortingEnabled(False)
        self.resize(250, 490)
        self.move(50, 50)
        self.Pi = QtGui.QIcon(p)
        self.Fi = QtGui.QIcon(f)
        sz = QtCore.QSize()
        sz.setHeight(10)
        sz.setWidth(10)
        self.currentTextChanged.connect(settingftp.namefile2)

    def clearlist(self):
        self.clear()
        self.Files()

    

    def addList(self, files):
        for i in files:
            File = QListWidgetItem(self.Fi, i)
            self.addItem(File)
    

    def Files(self):
        directory = 'files'
        self.files = os.listdir(directory)
        self.addList(self.files)
        
    
    