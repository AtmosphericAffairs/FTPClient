from PyQt5 import QtWidgets, QtMultimedia
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QTimer
from ftplib import FTP
import sys
import FtpFunc as FF
from datetime import datetime
import os
import shutil

class TimerAuto():
    def __init__(self, window1, button):
        
        
        self.button = button
        self.tm = QTimer()
        self.tm.timeout.connect(self.workFtp)
        self.timeOut = 1
        self.sound = False
        self.count_files = 0
        self.Date = ''


    def soundClick(self, d):
        if d:
            self.sound = True
        else:
            self.sound = False


    def time(self):
        self.tm.stop()
        self.tm.start(3600000 * self.timeOut) #3600000
        self.button.label6()

    def timeStop(self):
        self.tm.stop()
        self.button.label5()

    def timeuotchanjet(self, d):
        self.timeOut = int(d)
        print(self.timeOut)
    

    def workFtp(self):

        

        self.catalogFile = []

        f = open('setting/settingftp.txt')
        dataFTP = str(f.read())
        f.close()
        dataFTP = dataFTP.split('\n')
        ip = str(dataFTP[0])
        login = str(dataFTP[1])
        password = str(dataFTP[2])
        
        try:
            FTP.close(ip)
        except:
            pass

        try:        
            ftp = FTP(ip)
            ftp.login(user=login, passwd=password)
            self.button.label3()
        
            
            d = open('setting/settingAUTO.txt', encoding='utf-8')
            direct = str(d.read())
            d.close()
            direct = direct.split('\n')

            for i in direct:
                ftp.cwd(i)
                
        except:
            pass

        try:
            for i in ftp.mlsd(facts=["type"]):
                if i[1]['type'] == 'file':
                    self.catalogFile.append(i[0])
        except:
            try:
                for i in ftp.nlst():
                    self.catalogFile.append(i)
            except:
                pass


        self.command = str(bytes('RETR', encoding='latin-1'), encoding='utf-8')
        for i in self.catalogFile:
            with open('files/' + i, 'wb') as file:
                ftp.retrbinary('RETR ' + i, file.write, 1000000)
                ftp.delete(i)
                self.count_files += 1
        try:
            ftp.close()
            self.button.label2()
            if len(self.catalogFile) > 0 and self.sound == True:
                self.sound = QtMultimedia.QSound('image/ss.wav')
                self.sound.play()
                FF.nameDir(self.catalogFile)
                
            current_time = str(datetime.now().hour)+':'+str(datetime.now().minute)+':'+str(datetime.now().second)
            self.button.label7(self.count_files, current_time)
            self.count_files = 0
        

            
        except:
            pass
        
        



       







    