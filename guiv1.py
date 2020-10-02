# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiv1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot

class Ui_MainWindow( QObject ):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(570, 217)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 0, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 40, 541, 131))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.widget)
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
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 5)
        self.cancelButton = QtWidgets.QPushButton(self.frame)
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 2, 0, 1, 1)
        self.importButton = QtWidgets.QPushButton(self.frame)
        self.importButton.setObjectName("importButton")
        self.gridLayout.addWidget(self.importButton, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 3)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(428, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.nextButton = QtWidgets.QPushButton(self.widget)
        self.nextButton.setObjectName("nextButton")
        self.gridLayout_2.addWidget(self.nextButton, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 570, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.browseButton.clicked.connect(self.browseSlot)
        self.cancelButton.clicked.connect(self.cancelSlot)
        self.importButton.clicked.connect(self.importSlot)
        self.nextButton.clicked.connect(self.nextSlot)
        self.nextButton.setEnabled(False)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Import your Data"))
        self.label_2.setText(_translate("MainWindow", "File Name"))
        self.browseButton.setText(_translate("MainWindow", "Browse"))
        self.cancelButton.setText(_translate("MainWindow", "Cancel"))
        self.importButton.setText(_translate("MainWindow", "Import"))
        self.label_3.setText(_translate("MainWindow", "Please, choose a valid .csv file:"))
        self.nextButton.setText(_translate("MainWindow", "Next"))

    @pyqtSlot( )
    def browseSlot( self ):
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



