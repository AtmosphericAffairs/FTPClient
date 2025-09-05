from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import os
from datetime import datetime
import shutil







def Connect(ftp, window1, button, list1):
    """функция проверки содержимого директории фтп сервера и от типа раскидывание по разным спискам"""
    try:
        catalogback = []
        catalogDir = []
        catalogFile = []
        for i in ftp.mlsd(facts=["type"]):
            if i[1]['type'] == 'dir':
                catalogDir.append(i[0])
            elif i[1]['type'] == 'file':
                catalogFile.append(i[0])
            elif i[1]['type'] == 'pdir':
                catalogback.append(i[0])

        list1.clearlist()
        list1.addList(catalogback, catalogDir, catalogFile)
        button.label3()
        
        
    except:

        try:
            for i in ftp.nlst():
                catalogDir.append(i)
            list1.clearlist()
            list1.addList(catalogback, catalogDir, catalogFile)
            button.label3()
        except:
            button.label2()

        


def fileSaveAuto(directAUTO):
    """функция для записи пути в текстовой файл"""
    with open('setting/settingAUTO.txt', 'w', encoding='utf-8') as tw:
        for i in directAUTO:
            tw.write(i +'\n')
    tw.close()

def autoButton8(list2):
    """очистка содержимого левого окна директории и новое заполнение"""
    list2.clearlist()



def CopyFiles(catalogFile, Date):
        """функция копирует скачанные файлы в архив"""
        if type(catalogFile) is str:
            shutil.copy2('files/' + catalogFile, Date + '/' + catalogFile)
        else:
            for i in catalogFile:
                shutil.copy2('files/' + i, Date + '/' + i)

def nameDir(catalogFile):
        """создает название дирректории по дате и создают эту дирректорию для архива взодяших файлов"""
        Date ='Arhive/Download/' + str(datetime.now().year) + '-' + str((datetime.now().month)) + '-' + str(datetime.now().day)
        if not os.path.exists(Date): 
            os.makedirs(Date)
        CopyFiles(catalogFile, Date)

def nameDirLoad(catalogFile):
        """создает название дирректории по дате и создают эту дирректорию для архива исходящих файлов"""
        Date ='Arhive/Load/' + str(datetime.now().year) + '-' + str((datetime.now().month)) + '-' + str(datetime.now().day)
        if not os.path.exists(Date): 
            os.makedirs(Date)
        CopyFiles(catalogFile, Date)   
