# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiOrganizer.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 567)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 681, 601))
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 22);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 561, 481))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.txtPath = QLineEdit(self.widget)
        self.txtPath.setObjectName(u"txtPath")
        self.txtPath.setMinimumSize(QSize(0, 30))
        self.txtPath.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-color: rgb(147, 147, 147);")

        self.horizontalLayout_3.addWidget(self.txtPath)

        self.btnOpen = QPushButton(self.widget)
        self.btnOpen.setObjectName(u"btnOpen")
        self.btnOpen.setMinimumSize(QSize(120, 30))
        self.btnOpen.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);\n"
"border-radius: 15px;\n"
"hover{color: #000;background-color: #fff}")

        self.horizontalLayout_3.addWidget(self.btnOpen)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.btnOrganize = QPushButton(self.widget)
        self.btnOrganize.setObjectName(u"btnOrganize")
        self.btnOrganize.setMinimumSize(QSize(200, 35))
        self.btnOrganize.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);\n"
"border-radius: 15px;\n"
"hover{color: #000;background-color: #fff}")

        self.horizontalLayout_2.addWidget(self.btnOrganize)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">FILE ORGANIZER</span></p></body></html>", None))
        self.txtPath.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CHOOSE THE FOLDER", None))
        self.btnOpen.setText(QCoreApplication.translate("MainWindow", u"OPEN", None))
        self.label_2.setText("")
        self.btnOrganize.setText(QCoreApplication.translate("MainWindow", u"ORGANIZE", None))
        self.label_3.setText("")
    # retranslateUi

