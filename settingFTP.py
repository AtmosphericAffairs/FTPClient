from ftplib import FTP
import FtpFunc as FF
import os


class SettingFtp():
    def __init__(self, window1, button, list1, list2):
        self.creat_load_file = False
        self.window1 = window1
        self.button = button
        self.list1 = list1
        self.list2 = list2
        self.data = False
        self.data2 = False
        self.directAutoFile = []
        self.directAUTO = []   #путь для автоматической работы
        self.TrLP = True

    def OpenFileSetting(self):
        self.TrLP = True
        """Ввод данных из текстового файла и подключение к фтп"""
        try:
            f = open('setting/settingftp.txt')
            dataFTP = str(f.read())
            f.close()
            dataFTP = dataFTP.split('\n')
            ip = str(dataFTP[0])
            login = str(dataFTP[1])
            password = str(dataFTP[2])
        
                
            self.ftp = FTP(ip)
            self.ftp.login(user=login, passwd=password)
            self.ftp.connect(host=ip, port=22022)
            
        except:
            pass
        try:
            s = open('setting/commandOpen.txt', encoding='utf-8')   #мини для открытие сохраненной дирректории
            command = int(s.read())
            s.close()
            if self.creat_load_file:
                for i in self.directAutoFile:
                    self.ftp.cwd(i)
                self.downloadFileInFTP()
                self.creat_load_file = False

            elif command:

                d = open('setting/settingAUTO.txt', encoding='utf-8')
                direct = str(d.read())
                d.close()
                direct = direct.split('\n')

                for i in direct:
                    self.directAUTO.append(i)
                    self.ftp.cwd(i)

            
        except:
            pass
        try:
            FF.Connect(self.ftp, self.window1, self.button, self.list1)
        except:
            print('нет соеденения')    
        
    def directOpen(self, d):
        """открытие дирректории"""
        self.ftp.cwd(d)
        FF.Connect(self.ftp, self.window1, self.button, self.list1)
        
        if d == '..':
            if len(self.directAUTO) > 0:
                self.directAUTO.pop()
        else:
            self.directAUTO.append(d)
            
        

    def namefile2(self, d):
        self.data2 = d


    def namefile(self, d):
        self.data = d

    def downloadFile(self):
        """функция скачиваеия файоа"""
        try:
            if self.data:
                self.command = str(bytes('RETR', encoding='latin-1'), encoding='utf-8')
                with open('files/' + self.data, 'wb') as file:
                    self.ftp.retrbinary('RETR ' + self.data, file.write, 1000000)
            
        except:
            pass
        FF.nameDir(self.data)
        self.data = False
        FF.autoButton8(self.list2)
        
        


    def CloseFTP(self):
        """функция закрытия соеденение с фтп"""
        self.directAUTO = []
        try:
            self.ftp.close()
            self.button.label2()
            self.list1.clearlist()

        except:
            pass


    def downloadFileInFTP(self):
        """функция закачивания на фтп"""
        if self.data2:
            with open('files/' + self.data2, 'rb') as file:
                    self.ftp.storbinary('STOR ' + self.data2, file)
            FF.nameDirLoad(self.data2)
            self.data = False
        
        FF.Connect(self.ftp, self.window1, self.button, self.list1)


    def savedir(self):
        FF.fileSaveAuto(self.directAUTO)
    

    