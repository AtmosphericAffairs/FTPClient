from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu
import sys
from buttonFtp import Button
from settingFTP import SettingFtp
from windowsetting import WindowSetting
from window2load import Modalwindow2Load
from QlistVidgets import List
from QlistVidgets2 import List2
from autoJob import TimerAuto
import os



if not os.path.exists('files'): #создание папок, если их нет
    os.makedirs('files')

if not os.path.exists('setting'): 
    os.makedirs('setting')

if not os.path.exists('Arhive'): 
    os.makedirs('Arhive')

if not os.path.exists('Arhive/Download'): 
    os.makedirs('Arhive/Download')

if not os.path.exists('Arhive/Load'): 
    os.makedirs('Arhive/Load')

f = 'ftp.jpg' #переменная иконки

class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.f = QtGui.QIcon(f)

        #создание переменных для подключаемых модулей
        self.list1 = List(self)
        self.list2 = List2(self)
        self.window2setting = WindowSetting(self)
        
        self.button = Button(self)
        self.settingftp = SettingFtp(self, self.button, self.list1, self.list2)
        self.autojob = TimerAuto(self, self.button)
        self.window2load = Modalwindow2Load(self, self.settingftp)

        self.tray_icon = QtWidgets.QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.f)

        #чуть ниже блок для работы программы в трей
        show_action = QAction('Развернуть', self)
        quit_action = QAction('Exit', self) #не реализовано
        hide_action = QAction('Свернуть', self)
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()
        
        


        self.setWindowTitle('менаджер')
        self.setGeometry(200, 200, 800, 650) #разрешение и расположение окна при запуска

        self.button.btn1(self.window2setting) #кнопка настройки
        self.button.btn2(self.settingftp) #кнопка подключение
        self.button.btn3(self.settingftp) #кнопка отключение
        self.button.btn4(self.settingftp)   #кнопка влево
        self.button.btn5(self.settingftp) #сохранить путь
        self.button.btn6(self.autojob) #кнопка запуск
        self.button.btn9(self.autojob) #кнопка стоп
        self.button.btn7(self.settingftp) #кнопка вправо
        self.button.btn8(self.list2) #кнопка обновить
        self.button.btn10(self.window2load)
        self.button.BSpin(self.autojob) #виджет настройки периода
        self.button.label1() #лейбл статус
        self.button.label2() #лейбл подключения
        self.button.label5() #лейбл автоработы
        self.button.label4() #лейбл автоматическая работа
        self.button.lblImage() #картинка Vostok
        self.button.chec(self.autojob) # чекбокс звука
        self.list1.lineWid(self.settingftp) #окно фтп
        self.list2.lineWid(self.settingftp) #окно папки files
        self.list2.Files() #метод проверки файлов
    
    






    
def appLication():    
    app = QApplication(sys.argv)
    window1 = Window()
    imag = QtGui.QIcon(f)
    window1.setWindowIcon(imag)
    app.setWindowIcon(imag)
    
    window1.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    appLication()