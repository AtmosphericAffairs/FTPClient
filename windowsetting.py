from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class WindowSetting():
    def __init__(self, window1):
        self.window1 = window1
        self.ip = ''
        self.login = ''
        self.Pass = ''


    def read_ip(self, text):
        self.ip = text

    def read_login(self, text):
        self.login = text
        

    def read_pass(self, text):
        self.Pass = text
        

    def read_file_setting(self):
        "запись в файл настроек подключения"
        with open('setting/settingftp.txt', 'w', encoding='utf-8') as tw:
            tw.write(self.ip +'\n')
            tw.write(self.login +'\n')
            tw.write(self.Pass)
        tw.close()

    def openDir(self, s):
        """запись в файл галочки или ее отстутствие"""
        with open('setting/commandOpen.txt', 'w', encoding='utf-8') as tw:
            tw.write(str(s))
        tw.close()


    def window2Show(self):
        """настройки модального окна с настройками"""
        modalWindow = QtWidgets.QWidget(self.window1, QtCore.Qt.Window)
        modalWindow.setWindowTitle("Настройки подключения")
        modalWindow.resize(400, 300)
        modalWindow.setWindowModality(QtCore.Qt.WindowModal)
        modalWindow.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        modalWindow.move(self.window1.geometry().center() - modalWindow.rect().center() - 
        QtCore.QPoint(4, 30))


        try:
            s = open('setting/commandOpen.txt', encoding='utf-8')   #открытие файла, и на данных файла ставится галочка
            self.command = int(s.read())
            s.close()
        except:
            self.command = 0



        qleIP = QtWidgets.QLineEdit(modalWindow)
        qleIP.move(10, 30)                              #окно ip
        qleIP.textChanged[str].connect(self.read_ip)


        qleLogin = QtWidgets.QLineEdit(modalWindow)
        qleLogin.move(10, 55)                           #окно логин
        qleLogin.textChanged[str].connect(self.read_login)

        qlePass = QtWidgets.QLineEdit(modalWindow)
        qlePass.move(10, 80)                            # окно пароль
        qlePass.textChanged[str].connect(self.read_pass)

        btn1 = QtWidgets.QPushButton(modalWindow)
        btn1.move(55, 110)                              #кнопка ввести
        btn1.setText('Ввести')
        btn1.clicked.connect(self.read_file_setting)

        lbIp = QtWidgets.QLabel(modalWindow)
        lbIp.move(150, 33)                              #подписи
        lbIp.setText('Ip')

        lbLogin = QtWidgets.QLabel(modalWindow)
        lbLogin.move(150, 58)
        lbLogin.setText('Login')

        lbPass = QtWidgets.QLabel(modalWindow)
        lbPass.move(150, 83)
        lbPass.setText('Password')

        QChec = QtWidgets.QCheckBox(modalWindow)
        QChec.move(10, 140)
        if self.command:
            QChec.setChecked(bool(self.command))
        QChec.stateChanged.connect(self.openDir)

        lbSaveD = QtWidgets.QLabel(modalWindow)
        lbSaveD.move(30, 140)                       #чекбокс
        lbSaveD.setText('-Открывать сохраненную дирректорию')
        


        

        modalWindow.show()
        
        