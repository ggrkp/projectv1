# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiv1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import  pyqtSlot , QObject
import sys

class Ui_MainWindow(QObject):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(742, 595)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 691, 541))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.layoutWidget = QtWidgets.QWidget(self.page)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 621, 471))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(428, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.nextButton = QtWidgets.QPushButton(self.layoutWidget)
        self.nextButton.setObjectName("nextButton")
        self.gridLayout_2.addWidget(self.nextButton, 1, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.layoutWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.pathLine = QtWidgets.QLineEdit(self.frame)
        self.pathLine.setObjectName("pathLine")
        self.horizontalLayout.addWidget(self.pathLine)
        self.browseButton = QtWidgets.QPushButton(self.frame)
        self.browseButton.setObjectName("browseButton")
        self.horizontalLayout.addWidget(self.browseButton)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 2, 5)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 3)
        self.importButton = QtWidgets.QPushButton(self.frame)
        self.importButton.setObjectName("importButton")
        self.gridLayout.addWidget(self.importButton, 4, 1, 1, 1)
        self.cancelButton = QtWidgets.QPushButton(self.frame)
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 2)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.backButton1 = QtWidgets.QPushButton(self.page_2)
        self.backButton1.setGeometry(QtCore.QRect(520, 510, 80, 23))
        self.backButton1.setObjectName("backButton1")
        self.nextButton1 = QtWidgets.QPushButton(self.page_2)
        self.nextButton1.setGeometry(QtCore.QRect(610, 510, 80, 23))
        self.nextButton1.setObjectName("nextButton1")
        self.comboBox = QtWidgets.QComboBox(self.page_2)
        self.comboBox.setGeometry(QtCore.QRect(230, 370, 79, 23))
        self.comboBox.setMaximumSize(QtCore.QSize(79, 16777215))
        self.comboBox.setObjectName("comboBox")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setGeometry(QtCore.QRect(90, 370, 131, 20))
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_3.setGeometry(QtCore.QRect(580, 470, 80, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_4.setGeometry(QtCore.QRect(500, 470, 80, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 691, 121))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.page_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.browseButton.clicked.connect(self.browseSlot)
        self.cancelButton.clicked.connect(self.cancelSlot)
        self.importButton.clicked.connect(self.importSlot)
        self.nextButton.clicked.connect(self.nextSlot)
        self.backButton1.clicked.connect(self.backSlot)
        self.comboBox.activated['QString'].connect(self.featureSlot)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.stackedWidget.setCurrentIndex(0) # Na ksekinaei apo 1h othoni
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nextButton.setText(_translate("MainWindow", "Next"))
        self.label_2.setText(_translate("MainWindow", "File Name"))
        self.browseButton.setText(_translate("MainWindow", "Browse"))
        self.label_3.setText(_translate("MainWindow", "Please, choose a valid .csv file:"))
        self.importButton.setText(_translate("MainWindow", "Import"))
        self.cancelButton.setText(_translate("MainWindow", "Clear"))
        self.label.setText(_translate("MainWindow", "Import your Data"))
        self.backButton1.setText(_translate("MainWindow", "Back"))
        self.nextButton1.setText(_translate("MainWindow", "Next"))
        self.label_5.setText(_translate("MainWindow", "Select Target Feature"))
        self.pushButton_3.setText(_translate("MainWindow", "Next"))
        self.pushButton_4.setText(_translate("MainWindow", "Back"))
        self.label_4.setText(_translate("MainWindow", "Im the 3rd Page. Later Bitches."))

    @pyqtSlot( )
    def browseSlot( self ):
        pass

    @pyqtSlot( )
    def backSlot( self ):
        pass

    @pyqtSlot( )
    def importSlot( self ):
        pass

    @pyqtSlot( )
    def cancelSlot( self ):
        pass

    @pyqtSlot( )
    def nextSlot( self ):
        pass

    @pyqtSlot( )
    def featureSlot( self ):
        pass

