from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget
from datetime import datetime

class Modalwindow2Load():
    def __init__(self, window1, settingftp):
        self.window1 = window1
        self.settingftp = settingftp
        self.up_register = False
        self.text_message = ''
        self.number_message = ''

    def namePlus(self, name):
        """функция добавляет дату в шаблон"""
        name = name.split('\n')
        name[-1] = self.Day + self.Month + str(self.number_message) + ' ' + name[-1]
        name = '\n'.join(name)
        return name



    def radiop(self, number):
        self.Qtext.clear()
        self.Day = str(datetime.now().day)
        if len(self.Day) < 2:
            self.Day = '0' + self.Day
        self.Month = str(datetime.now().month)
        if len(self.Month) < 3:
            self.Month = '0' + self.Month
        self.NameDyqDay = 'ВОСТОК ' + self.Day + '/' + self.Month + ' ' + str(self.number_message) +  '=\n'
        if number == 1:
            self.Qtext.setPlainText(self.NameDyqDay + self.namePlus(self.sample1))
        elif number == 2:
            self.Qtext.setPlainText(self.NameDyqDay + self.namePlus(self.sample2))
        elif number == 3:
            self.Qtext.setPlainText(self.NameDyqDay + self.namePlus(self.sample3))

    def openUp(self, s):
        """запись в файл галочки или ее отстутствие"""
        with open('setting/UpRegOpen.txt', 'w', encoding='utf-8') as tw:
            tw.write(str(s))
        tw.close()
        self.up_register = int(s)

    def setting_adres(self, d):
        """добавление адреса отправки от выбранного адресата"""
        for i in range(len(self.list_adres)):
            if d in self.list_adres[i]:
                self.settingftp.directAutoFile = self.list_adres[i][1].split('/')


    def creat_number(self):
        with open('setting/number.txt', 'w', encoding='utf-8') as tw:
            tw.write(str(self.number_message + 1))
        tw.close()

    def creat_message(self):
        """создание имени файла и отправка"""
        
        name = 'vos' + self.Day + self.Month + str(self.number_message) + '.txt'
        with open('files/' + name, 'w', encoding='utf-8') as file:
            file.write(self.text_message.upper())
        file.close()
        self.settingftp.data2 = name
        self.settingftp.creat_load_file = True
        self.settingftp.OpenFileSetting()
        self.creat_number()


    def OpenFileAdress(self):
        """прочтение адресной книги и раскидывание инфы по спискам"""
        with open('adres/adres.txt', encoding='utf-8') as file:
            self.list_adres = file.read()
        file.close()
        self.list_adres = self.list_adres.split('\n\n\n')
        for i in range(len(self.list_adres)):
            self.list_adres[i] = self.list_adres[i].split('\n')

        


    def read_text(self):
        """запись введенного текста в переменную"""
        self.text_message = self.Qtext.toPlainText()

    def window2Show(self):
        self.OpenFileAdress()

        try:
            s = open('setting/UpRegOpen.txt', encoding='utf-8')   #открытие файла, и на данных файла ставится галочка
            self.up_register = int(s.read())
            s.close()
        except:
            self.up_register = 0

        with open('setting/sample1.txt', encoding='utf-8') as file:
            self.sample1 = file.read()
        file.close()

        with open('setting/sample2.txt', encoding='utf-8') as file:
            self.sample2 = file.read()
        file.close()

        with open('setting/sample3.txt', encoding='utf-8') as file:
            self.sample3 = file.read()
        file.close()
        
        with open('setting/number.txt', encoding='utf-8') as file:
            self.number_message = int(file.read())
        file.close()


        """настройки модального окна с вводом сообщения"""
        modalWindow = QtWidgets.QWidget(self.window1, QtCore.Qt.Window)
        modalWindow.setWindowTitle("Создание сообщения")
        modalWindow.resize(800, 600)
        modalWindow.setWindowModality(QtCore.Qt.WindowModal)
        modalWindow.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        modalWindow.move(self.window1.geometry().center() - modalWindow.rect().center() - 
        QtCore.QPoint(4, 30))


        self.Qtext = QtWidgets.QTextEdit(modalWindow)
        self.Qtext.move(250, 30)
        self.Qtext.resize(500, 500)
        self.Qtext.textChanged.connect(self.read_text)
        

    
        self.listAdres = QListWidget(modalWindow)
        self.listAdres.move(10, 30)
        self.listAdres.resize(220, 500)
        for i in range(len(self.list_adres)):
            self.listAdres.addItem(self.list_adres[i][0])
        self.listAdres.currentTextChanged.connect(self.setting_adres)

        self.btn1 = QtWidgets.QPushButton(modalWindow)
        self.btn1.move(660, 530)
        self.btn1.setText('Отправить')
        self.btn1.clicked.connect(self.creat_message)


        self.rb1 = QtWidgets.QRadioButton(modalWindow)
        self.rb1.move(265, 535)
        self.rb1.toggled.connect(lambda:self.radiop(1))
        self.rb2 = QtWidgets.QRadioButton(modalWindow)
        self.rb2.move(265, 555)
        self.rb2.toggled.connect(lambda:self.radiop(2))
        self.rb3 = QtWidgets.QRadioButton(modalWindow)
        self.rb3.move(265, 575)
        self.rb3.toggled.connect(lambda:self.radiop(3))

        lbSh1 = QtWidgets.QLabel(modalWindow)
        lbSh1.move(285, 535)                       #чекбокс
        lbSh1.setText('- радист')

        lbSh2 = QtWidgets.QLabel(modalWindow)
        lbSh2.move(285, 555)                       #чекбокс
        lbSh2.setText('- начальник')

        lbSh3 = QtWidgets.QLabel(modalWindow)
        lbSh3.move(285, 575)                       #чекбокс
        lbSh3.setText('- недельный отчет')

        lbSh4 = QtWidgets.QLabel(modalWindow)
        lbSh4.move(200, 555)                       #чекбокс
        lbSh4.setText('шаблоны:')

        lbSh5 = QtWidgets.QLabel(modalWindow)
        lbSh5.move(50, 5)                       #чекбокс
        lbSh5.setText('адресаты')


        lbSh6 = QtWidgets.QLabel(modalWindow)
        lbSh6.move(450, 5)                       #чекбокс
        lbSh6.setText('текст сообщения')



        modalWindow.show()