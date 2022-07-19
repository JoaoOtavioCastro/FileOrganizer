import os
import shutil
from tkinter import messagebox 
from PySide2.QtWidgets import *
from uiMain import Ui_MainWindow
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('FILE ORGANIZER')
        self.file = ''
        self.btnOpen.clicked.connect(self.openPath)
        self.btnOrganize.clicked.connect(self.organizer)
    
    def openPath(self):
        self.file = QFileDialog.getExistingDirectory(self, str("pasta xml"), '/home', QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        self.txtPath.setText(self.file)
    
    def organizer(self):
        path = self.file
        files = os.listdir(path)

        for file in files:
            filename, extension = os.path.splitext(file)
            extension = extension[1:]
            if(os.path.exists(path+'/'+extension)):
                shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
            else:
                os.makedirs(path+'/'+extension)
                shutil.move(path+'/'+file, path+'/'+extension)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.information)
        msg.setText("DONE!\n The files are successfully organized!")
        msg.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()