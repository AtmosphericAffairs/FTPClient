from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPainter

r = 'image/right.jpg'
l = 'image/left.jpg'
vos = 'image/vostok.jpg'

class Button():
    """класс содержащий кнопки и картинки и надписи"""
    def __init__(self, window1):
        self.r = QtGui.QIcon(r)
        self.l = QtGui.QIcon(l)
        self.window1 = window1
        self.status = QtWidgets.QLabel(self.window1)
        self.status.move(650, 5)
        self.sound = QtWidgets.QLabel(self.window1)
        self.sound.move(720, 550)
        self.sound.setText('Звук')
        self.auto = QtWidgets.QLabel(self.window1)
        self.auto.move(200, 606)
        self.infoDown = QtWidgets.QLabel(self.window1)
        self.infoDown.resize(210, 15)
        self.infoDown.move(550, 612)

    def btn1(self, window2setting):
        self.btn1 = QtWidgets.QPushButton(self.window1)
        self.btn1.move(10, 5)
        self.btn1.setText('Настройки')
        self.btn1.clicked.connect(window2setting.window2Show)

    def btn2(self, settingftp):
        self.btn2 = QtWidgets.QPushButton(self.window1)
        self.btn2.move(110, 5)
        self.btn2.setText('Подключение')
        self.btn2.clicked.connect(settingftp.OpenFileSetting)

    def btn3(self, settingftp):
        self.btn3 = QtWidgets.QPushButton(self.window1)
        self.btn3.move(210, 5)
        self.btn3.setText('Отключение')
        self.btn3.clicked.connect(settingftp.CloseFTP)

    def btn4(self, settingftp):
        self.btn4 = QtWidgets.QPushButton(self.window1)
        self.btn4.move(350, 250)
        self.btn4.setIcon(self.l) #скачать с сервера
        self.btn4.clicked.connect(settingftp.downloadFile)

    def btn7(self, settingftp):
        self.btn7 = QtWidgets.QPushButton(self.window1)
        self.btn7.move(350, 275)
        self.btn7.setIcon(self.r) #закинуть на сервер
        self.btn7.clicked.connect(settingftp.downloadFileInFTP)

    def btn8(self, List2):
        self.btn8 = QtWidgets.QPushButton(self.window1)
        self.btn8.move(100, 550)
        self.btn8.setText('обновить')
        self.btn8.clicked.connect(List2.clearlist)
    
    def btn5(self, settingftp):
        self.btn5 = QtWidgets.QPushButton(self.window1)
        self.btn5.move(400, 550)
        self.btn5.setText('сохранить')
        self.btn5.clicked.connect(settingftp.savedir)

    def btn6(self, TimerAuto):
        self.btn6 = QtWidgets.QPushButton(self.window1)
        self.btn6.move(600, 550)
        self.btn6.setText('запуск')
        self.btn6.clicked.connect(TimerAuto.time)


    def btn9(self, TimerAuto):
        self.btn9 = QtWidgets.QPushButton(self.window1)
        self.btn9.move(600, 579)
        self.btn9.setText('Стоп')
        self.btn9.clicked.connect(TimerAuto.timeStop)

    def btn10(self, window2load):
        self.btn1 = QtWidgets.QPushButton(self.window1)
        self.btn1.move(480, 5)
        self.btn1.setText('Создать')
        self.btn1.clicked.connect(window2load.window2Show)
    

    def chec(self, TimerAuto):
        self.QChec = QtWidgets.QCheckBox(self.window1)
        self.QChec.move(700, 550) #чекбокс звука
        self.QChec.stateChanged.connect(TimerAuto.soundClick)

    def BSpin(self, TimerAuto):
        self.selfSpin = QtWidgets.QSpinBox(self.window1)
        self.selfSpin.setMinimum(1)
        self.selfSpin.setMaximum(168)
        self.selfSpin.setSuffix('Ч.')
        self.selfSpin.move(500, 550)
        self.selfSpin.valueChanged.connect(TimerAuto.timeuotchanjet)
    

    def label1(self):
        status = QtWidgets.QLabel(self.window1)
        status.move(600, 5)
        status.setText('Статус:')


    def label4(self):
        status = QtWidgets.QLabel(self.window1)
        status.resize(210, 12)
        status.move(50, 615)
        status.setText('Автоматическая работа:')

    def label2(self):
        self.status.setText('Не подключено')

    def label3(self):
        self.status.setText('подключено')

    def label5(self):
        self.auto.setText('Не запущено')

    def label6(self):
        self.auto.setText('Запущено')

    def label7(self, count, time):
        text = 'В '+ time + " загружено " + str(count) + 'ф.'
        self.infoDown.setText(text)
    
    def lblImage(self):
        lbl = QtWidgets.QLabel(self.window1) #картинка
        pixmax = QtGui.QPixmap(vos)
        lbl.setPixmap(pixmax)
        lbl.resize(100, 40)
        lbl.move(350, 10)
        

