# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiv1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import  pyqtSlot , QObject
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
import time
import sys

class Ui_MainWindow(QObject):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(914, 645)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(110, 50, 751, 551))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.layoutWidget = QtWidgets.QWidget(self.page)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 150, 641, 201))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QtWidgets.QFrame(self.layoutWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cancelButton = QtWidgets.QPushButton(self.frame)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_2.addWidget(self.cancelButton)
        self.importButton = QtWidgets.QPushButton(self.frame)
        self.importButton.setObjectName("importButton")
        self.horizontalLayout_2.addWidget(self.importButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
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
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(442, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.frame)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(428, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.nextButton = QtWidgets.QPushButton(self.layoutWidget)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout_3.addWidget(self.nextButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.page_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 470, 261, 25))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox.setMaximumSize(QtCore.QSize(79, 16777215))
        self.comboBox.setStyleSheet("selection-background-color: rgb(85, 255, 127);")
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_4.addWidget(self.comboBox)
        self.layoutWidget2 = QtWidgets.QWidget(self.page_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(601, 401, 82, 54))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.backButton1 = QtWidgets.QPushButton(self.layoutWidget2)
        self.backButton1.setObjectName("backButton1")
        self.verticalLayout_2.addWidget(self.backButton1)
        self.nextButton1 = QtWidgets.QPushButton(self.layoutWidget2)
        self.nextButton1.setObjectName("nextButton1")
        self.verticalLayout_2.addWidget(self.nextButton1)
        self.layoutWidget3 = QtWidgets.QWidget(self.page_2)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 40, 581, 421))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.tableWidget = QtWidgets.QTableWidget(self.layoutWidget3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_13 = QtWidgets.QLabel(self.page_3)
        self.label_13.setGeometry(QtCore.QRect(0, 0, 501, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_15 = QtWidgets.QLabel(self.page_3)
        self.label_15.setGeometry(QtCore.QRect(240, 100, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.page_3)
        self.label_16.setGeometry(QtCore.QRect(240, 410, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.groupBox = QtWidgets.QGroupBox(self.page_3)
        self.groupBox.setGeometry(QtCore.QRect(10, 100, 221, 421))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.dtreeBox = QtWidgets.QCheckBox(self.groupBox)
        self.dtreeBox.setGeometry(QtCore.QRect(10, 77, 105, 21))
        self.dtreeBox.setObjectName("dtreeBox")
        self.ldaBox = QtWidgets.QCheckBox(self.groupBox)
        self.ldaBox.setGeometry(QtCore.QRect(10, 212, 44, 21))
        self.ldaBox.setObjectName("ldaBox")
        self.gradientBox = QtWidgets.QCheckBox(self.groupBox)
        self.gradientBox.setGeometry(QtCore.QRect(10, 158, 134, 21))
        self.gradientBox.setObjectName("gradientBox")
        self.multinbBox = QtWidgets.QCheckBox(self.groupBox)
        self.multinbBox.setGeometry(QtCore.QRect(10, 293, 118, 21))
        self.multinbBox.setObjectName("multinbBox")
        self.adaBox = QtWidgets.QCheckBox(self.groupBox)
        self.adaBox.setGeometry(QtCore.QRect(10, 23, 81, 21))
        self.adaBox.setObjectName("adaBox")
        self.qdaBox = QtWidgets.QCheckBox(self.groupBox)
        self.qdaBox.setGeometry(QtCore.QRect(10, 401, 48, 21))
        self.qdaBox.setObjectName("qdaBox")
        self.pasagrBox = QtWidgets.QCheckBox(self.groupBox)
        self.pasagrBox.setGeometry(QtCore.QRect(10, 320, 142, 21))
        self.pasagrBox.setObjectName("pasagrBox")
        self.gaussianBox = QtWidgets.QCheckBox(self.groupBox)
        self.gaussianBox.setGeometry(QtCore.QRect(10, 131, 100, 21))
        self.gaussianBox.setObjectName("gaussianBox")
        self.liblinearBox = QtWidgets.QCheckBox(self.groupBox)
        self.liblinearBox.setGeometry(QtCore.QRect(10, 239, 100, 21))
        self.liblinearBox.setObjectName("liblinearBox")
        self.libsvmBox = QtWidgets.QCheckBox(self.groupBox)
        self.libsvmBox.setGeometry(QtCore.QRect(10, 266, 91, 21))
        self.libsvmBox.setObjectName("libsvmBox")
        self.rforoestBox = QtWidgets.QCheckBox(self.groupBox)
        self.rforoestBox.setGeometry(QtCore.QRect(10, 347, 113, 21))
        self.rforoestBox.setObjectName("rforoestBox")
        self.sgdBox = QtWidgets.QCheckBox(self.groupBox)
        self.sgdBox.setGeometry(QtCore.QRect(10, 374, 47, 21))
        self.sgdBox.setObjectName("sgdBox")
        self.extratreeBox = QtWidgets.QCheckBox(self.groupBox)
        self.extratreeBox.setGeometry(QtCore.QRect(10, 104, 94, 21))
        self.extratreeBox.setObjectName("extratreeBox")
        self.knnBox = QtWidgets.QCheckBox(self.groupBox)
        self.knnBox.setGeometry(QtCore.QRect(10, 185, 150, 21))
        self.knnBox.setObjectName("knnBox")
        self.bernoulliBox = QtWidgets.QCheckBox(self.groupBox)
        self.bernoulliBox.setGeometry(QtCore.QRect(10, 50, 99, 21))
        self.bernoulliBox.setObjectName("bernoulliBox")
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(0, 0, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.widget = QtWidgets.QWidget(self.page_3)
        self.widget.setGeometry(QtCore.QRect(240, 120, 314, 221))
        self.widget.setObjectName("widget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        spacerItem2 = QtWidgets.QSpacerItem(118, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.timeLeft_box = QtWidgets.QSpinBox(self.widget)
        self.timeLeft_box.setObjectName("timeLeft_box")
        self.verticalLayout_5.addWidget(self.timeLeft_box)
        self.perRun_box = QtWidgets.QSpinBox(self.widget)
        self.perRun_box.setObjectName("perRun_box")
        self.verticalLayout_5.addWidget(self.perRun_box)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        spacerItem3 = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.memory_box = QtWidgets.QSpinBox(self.widget)
        self.memory_box.setObjectName("memory_box")
        self.horizontalLayout_6.addWidget(self.memory_box)
        self.verticalLayout_9.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.ressampleCombo = QtWidgets.QComboBox(self.widget)
        self.ressampleCombo.setObjectName("ressampleCombo")
        self.horizontalLayout_7.addWidget(self.ressampleCombo)
        self.verticalLayout_9.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.metricCombo = QtWidgets.QComboBox(self.widget)
        self.metricCombo.setObjectName("metricCombo")
        self.horizontalLayout_8.addWidget(self.metricCombo)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        self.checkBox_16 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_16.setObjectName("checkBox_16")
        self.verticalLayout_9.addWidget(self.checkBox_16)
        self.widget1 = QtWidgets.QWidget(self.page_3)
        self.widget1.setGeometry(QtCore.QRect(240, 440, 311, 81))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_12 = QtWidgets.QLabel(self.widget1)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_10.addWidget(self.label_12)
        spacerItem4 = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        self.memory_box_3 = QtWidgets.QSpinBox(self.widget1)
        self.memory_box_3.setObjectName("memory_box_3")
        self.horizontalLayout_10.addWidget(self.memory_box_3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_11 = QtWidgets.QLabel(self.widget1)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)
        spacerItem5 = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.memory_box_2 = QtWidgets.QSpinBox(self.widget1)
        self.memory_box_2.setObjectName("memory_box_2")
        self.horizontalLayout_9.addWidget(self.memory_box_2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)
        self.widget2 = QtWidgets.QWidget(self.page_3)
        self.widget2.setGeometry(QtCore.QRect(600, 440, 82, 83))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.run_Button = QtWidgets.QPushButton(self.widget2)
        self.run_Button.setObjectName("run_Button")
        self.verticalLayout_10.addWidget(self.run_Button)
        self.backButton2 = QtWidgets.QPushButton(self.widget2)
        self.backButton2.setObjectName("backButton2")
        self.verticalLayout_10.addWidget(self.backButton2)
        self.nextButton2 = QtWidgets.QPushButton(self.widget2)
        self.nextButton2.setObjectName("nextButton2")
        self.verticalLayout_10.addWidget(self.nextButton2)
        self.stackedWidget.addWidget(self.page_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        self.perRun_box.valueChanged['QString'].connect(self.perrun_Slot)
        self.nextButton1.clicked.connect(self.nextSlot_1)
        self.nextButton.clicked.connect(self.nextSlot)
        self.importButton.clicked.connect(self.importSlot)
        self.timeLeft_box.valueChanged['QString'].connect(self.timeleft_Slot)
        self.comboBox.activated['QString'].connect(self.featureSlot)
        self.backButton1.clicked.connect(self.backSlot)
        self.browseButton.clicked.connect(self.browseSlot)
        self.cancelButton.clicked.connect(self.cancelSlot)
        self.nextButton2.clicked.connect(self.nextSlot_2)
        self.backButton2.clicked.connect(self.backSlot_1)
        self.memory_box.valueChanged['QString'].connect(self.ensmemory_Slot)
        self.metricCombo.activated['QString'].connect(self.metricBox)
        self.ressampleCombo.activated['QString'].connect(self.resampleBox)
        self.run_Button.clicked.connect(self.modelSlot)
        self.adaBox.stateChanged['int'].connect(self.adaChecked)
        QtCore.QMetaObject.connectSlotsByName(self)
# extra: 
        self.stackedWidget.setCurrentIndex(0) # Na ksekinaei apo 1h othoni
        self.nextButton.setEnabled(False) # Otan ginei to import me valid file energopoieitai to next button
        self.nextButton1.setEnabled(False) # Otan ginei to import me valid file energopoieitai to next button
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Import your Data"))
        self.label_3.setText(_translate("MainWindow", "Please, choose a valid .csv file:"))
        self.cancelButton.setText(_translate("MainWindow", "Clear"))
        self.importButton.setText(_translate("MainWindow", "Import"))
        self.label_2.setText(_translate("MainWindow", "File Name"))
        self.browseButton.setText(_translate("MainWindow", "Browse"))
        self.nextButton.setText(_translate("MainWindow", "Next"))
        self.label_5.setText(_translate("MainWindow", "Select Target Feature"))
        self.backButton1.setText(_translate("MainWindow", "Back"))
        self.nextButton1.setText(_translate("MainWindow", "Next"))
        self.label_6.setText(_translate("MainWindow", "Preview of imported file:"))
        self.label_13.setText(_translate("MainWindow", "Select Parameters for the Classifier"))
        self.label_15.setText(_translate("MainWindow", "Select Other Parameters"))
        self.label_16.setText(_translate("MainWindow", "Select Resampling Arguments"))
        self.dtreeBox.setText(_translate("MainWindow", "decision_tree"))
        self.ldaBox.setText(_translate("MainWindow", "lda"))
        self.gradientBox.setText(_translate("MainWindow", "gradient_boosting"))
        self.multinbBox.setText(_translate("MainWindow", "multinomial_nb"))
        self.adaBox.setText(_translate("MainWindow", "adaboost"))
        self.qdaBox.setText(_translate("MainWindow", "qda"))
        self.pasagrBox.setText(_translate("MainWindow", "passive_aggressive"))
        self.gaussianBox.setText(_translate("MainWindow", "gaussian_nb"))
        self.liblinearBox.setText(_translate("MainWindow", "liblinear_svc"))
        self.libsvmBox.setText(_translate("MainWindow", "libsvm_svc"))
        self.rforoestBox.setText(_translate("MainWindow", "random_forest"))
        self.sgdBox.setText(_translate("MainWindow", "sgd"))
        self.extratreeBox.setText(_translate("MainWindow", "extra_trees"))
        self.knnBox.setText(_translate("MainWindow", "k_nearest_neighbors"))
        self.bernoulliBox.setText(_translate("MainWindow", "bernoulli_nb"))
        self.label_17.setText(_translate("MainWindow", "Select Estimators"))
        self.label_4.setText(_translate("MainWindow", "Time left for this task"))
        self.label_7.setText(_translate("MainWindow", "Per run time limit"))
        self.label_8.setText(_translate("MainWindow", "Ensemble memory limit"))
        self.label_9.setText(_translate("MainWindow", "Resampling strategy"))
        self.label_10.setText(_translate("MainWindow", "Metric"))
        self.checkBox_16.setText(_translate("MainWindow", "Enable Feature Preprocessing"))
        self.label_12.setText(_translate("MainWindow", "Holdout Train Size"))
        self.label_11.setText(_translate("MainWindow", "CV folds"))
        self.run_Button.setText(_translate("MainWindow", "Run"))
        self.backButton2.setText(_translate("MainWindow", "Back"))
        self.nextButton2.setText(_translate("MainWindow", "Next"))

