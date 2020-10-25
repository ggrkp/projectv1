import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


class Ui_MainWindow(QObject):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(818, 591)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(30, 10, 731, 551))
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
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 520, 261, 25))
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
        self.layoutWidget2.setGeometry(QtCore.QRect(590, 460, 82, 54))
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
        self.widget = QtWidgets.QWidget(self.page_2)
        self.widget.setGeometry(QtCore.QRect(11, 41, 571, 471))
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_3.addWidget(self.tableWidget, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_13 = QtWidgets.QLabel(self.page_3)
        self.label_13.setGeometry(QtCore.QRect(50, 30, 501, 51))
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
        self.groupBox.setGeometry(QtCore.QRect(50, 100, 174, 421))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.extratreeBox = QtWidgets.QCheckBox(self.groupBox)
        self.extratreeBox.setObjectName("extratreeBox")
        self.gridLayout_2.addWidget(self.extratreeBox, 3, 0, 1, 1)
        self.rforoestBox = QtWidgets.QCheckBox(self.groupBox)
        self.rforoestBox.setObjectName("rforoestBox")
        self.gridLayout_2.addWidget(self.rforoestBox, 12, 0, 1, 1)
        self.qdaBox = QtWidgets.QCheckBox(self.groupBox)
        self.qdaBox.setObjectName("qdaBox")
        self.gridLayout_2.addWidget(self.qdaBox, 14, 0, 1, 1)
        self.pasagrBox = QtWidgets.QCheckBox(self.groupBox)
        self.pasagrBox.setObjectName("pasagrBox")
        self.gridLayout_2.addWidget(self.pasagrBox, 11, 0, 1, 1)
        self.bernoulliBox = QtWidgets.QCheckBox(self.groupBox)
        self.bernoulliBox.setObjectName("bernoulliBox")
        self.gridLayout_2.addWidget(self.bernoulliBox, 1, 0, 1, 1)
        self.multinbBox = QtWidgets.QCheckBox(self.groupBox)
        self.multinbBox.setObjectName("multinbBox")
        self.gridLayout_2.addWidget(self.multinbBox, 10, 0, 1, 1)
        self.ldaBox = QtWidgets.QCheckBox(self.groupBox)
        self.ldaBox.setObjectName("ldaBox")
        self.gridLayout_2.addWidget(self.ldaBox, 7, 0, 1, 1)
        self.gaussianBox = QtWidgets.QCheckBox(self.groupBox)
        self.gaussianBox.setObjectName("gaussianBox")
        self.gridLayout_2.addWidget(self.gaussianBox, 4, 0, 1, 1)
        self.adaBox = QtWidgets.QCheckBox(self.groupBox)
        self.adaBox.setObjectName("adaBox")
        self.gridLayout_2.addWidget(self.adaBox, 0, 0, 1, 1)
        self.liblinearBox = QtWidgets.QCheckBox(self.groupBox)
        self.liblinearBox.setObjectName("liblinearBox")
        self.gridLayout_2.addWidget(self.liblinearBox, 8, 0, 1, 1)
        self.libsvmBox = QtWidgets.QCheckBox(self.groupBox)
        self.libsvmBox.setObjectName("libsvmBox")
        self.gridLayout_2.addWidget(self.libsvmBox, 9, 0, 1, 1)
        self.knnBox = QtWidgets.QCheckBox(self.groupBox)
        self.knnBox.setObjectName("knnBox")
        self.gridLayout_2.addWidget(self.knnBox, 6, 0, 1, 1)
        self.gradientBox = QtWidgets.QCheckBox(self.groupBox)
        self.gradientBox.setObjectName("gradientBox")
        self.gridLayout_2.addWidget(self.gradientBox, 5, 0, 1, 1)
        self.sgdBox = QtWidgets.QCheckBox(self.groupBox)
        self.sgdBox.setObjectName("sgdBox")
        self.gridLayout_2.addWidget(self.sgdBox, 13, 0, 1, 1)
        self.dtreeBox = QtWidgets.QCheckBox(self.groupBox)
        self.dtreeBox.setObjectName("dtreeBox")
        self.gridLayout_2.addWidget(self.dtreeBox, 2, 0, 1, 1)
        self.layoutWidget3 = QtWidgets.QWidget(self.page_3)
        self.layoutWidget3.setGeometry(QtCore.QRect(240, 120, 314, 221))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        spacerItem2 = QtWidgets.QSpacerItem(118, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.timeLeft_box = QtWidgets.QSpinBox(self.layoutWidget3)
        self.timeLeft_box.setObjectName("timeLeft_box")
        self.verticalLayout_5.addWidget(self.timeLeft_box)
        self.perRun_box = QtWidgets.QSpinBox(self.layoutWidget3)
        self.perRun_box.setObjectName("perRun_box")
        self.verticalLayout_5.addWidget(self.perRun_box)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        spacerItem3 = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.memory_box = QtWidgets.QSpinBox(self.layoutWidget3)
        self.memory_box.setObjectName("memory_box")
        self.horizontalLayout_6.addWidget(self.memory_box)
        self.verticalLayout_9.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.ressampleCombo = QtWidgets.QComboBox(self.layoutWidget3)
        self.ressampleCombo.setObjectName("ressampleCombo")
        self.horizontalLayout_7.addWidget(self.ressampleCombo)
        self.verticalLayout_9.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.metricCombo = QtWidgets.QComboBox(self.layoutWidget3)
        self.metricCombo.setObjectName("metricCombo")
        self.horizontalLayout_8.addWidget(self.metricCombo)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        self.checkBox_16 = QtWidgets.QCheckBox(self.layoutWidget3)
        self.checkBox_16.setObjectName("checkBox_16")
        self.verticalLayout_9.addWidget(self.checkBox_16)
        self.layoutWidget4 = QtWidgets.QWidget(self.page_3)
        self.layoutWidget4.setGeometry(QtCore.QRect(600, 440, 82, 83))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.run_Button = QtWidgets.QPushButton(self.layoutWidget4)
        self.run_Button.setObjectName("run_Button")
        self.verticalLayout_10.addWidget(self.run_Button)
        self.backButton2 = QtWidgets.QPushButton(self.layoutWidget4)
        self.backButton2.setObjectName("backButton2")
        self.verticalLayout_10.addWidget(self.backButton2)
        self.nextButton2 = QtWidgets.QPushButton(self.layoutWidget4)
        self.nextButton2.setObjectName("nextButton2")
        self.verticalLayout_10.addWidget(self.nextButton2)
        self.widget1 = QtWidgets.QWidget(self.page_3)
        self.widget1.setGeometry(QtCore.QRect(241, 440, 280, 60))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_12 = QtWidgets.QLabel(self.widget1)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_10.addWidget(self.label_12)
        spacerItem4 = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        self.holdout_box = QtWidgets.QDoubleSpinBox(self.widget1)
        self.holdout_box.setObjectName("holdout_box")
        self.horizontalLayout_10.addWidget(self.holdout_box)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_11 = QtWidgets.QLabel(self.widget1)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)
        spacerItem5 = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.cvfoldsBox = QtWidgets.QSpinBox(self.widget1)
        self.cvfoldsBox.setObjectName("cvfoldsBox")
        self.horizontalLayout_9.addWidget(self.cvfoldsBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.stackedWidget.addWidget(self.page_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
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
        self.checkBox_16.stateChanged['int'].connect(self.prepro_Checked)
        self.adaBox.stateChanged['int'].connect(self.adaChecked)
        self.groupBox.toggled['bool'].connect(self.select_all_Estimators)
        self.bernoulliBox.stateChanged['int'].connect(self.bernoulliChecked)
        self.dtreeBox.stateChanged['int'].connect(self.dectreeChecked)
        self.extratreeBox.stateChanged['int'].connect(self.extraTreeChecked)
        self.gaussianBox.stateChanged['int'].connect(self.gausianChecked)
        self.gradientBox.stateChanged['int'].connect(self.gradient_checked)
        self.knnBox.stateChanged['int'].connect(self.knnChecked)
        self.ldaBox.stateChanged['int'].connect(self.ldaChecked)
        self.liblinearBox.stateChanged['int'].connect(self.liblinearChecked)
        self.libsvmBox.stateChanged['int'].connect(self.libsvmChecked)
        self.multinbBox.stateChanged['int'].connect(self.multnbChecked)
        self.pasagrBox.stateChanged['int'].connect(self.pasagrChecked)
        self.rforoestBox.stateChanged['int'].connect(self.rforestChecked)
        self.sgdBox.stateChanged['int'].connect(self.sgdChecked)
        self.qdaBox.stateChanged['int'].connect(self.qdaChecked)
        self.holdout_box.valueChanged['QString'].connect(self.holdout_Size)
        self.cvfoldsBox.valueChanged['QString'].connect(self.cv_Folds)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
# extra: 
        self.stackedWidget.setCurrentIndex(0) # Na ksekinaei apo 1h othoni
        self.nextButton.setEnabled(False) # Otan ginei to import me valid file energopoieitai to next button
        self.nextButton1.setEnabled(False) # Otan ginei to import me valid file energopoieitai to next button

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Auto-ML Tool for IoT Applications"))
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
        self.groupBox.setTitle(_translate("MainWindow", "Select Estimators: "))
        self.extratreeBox.setText(_translate("MainWindow", "extra_trees"))
        self.rforoestBox.setText(_translate("MainWindow", "random_forest"))
        self.qdaBox.setText(_translate("MainWindow", "qda"))
        self.pasagrBox.setText(_translate("MainWindow", "passive_aggressive"))
        self.bernoulliBox.setText(_translate("MainWindow", "bernoulli_nb"))
        self.multinbBox.setText(_translate("MainWindow", "multinomial_nb"))
        self.ldaBox.setText(_translate("MainWindow", "lda"))
        self.gaussianBox.setText(_translate("MainWindow", "gaussian_nb"))
        self.adaBox.setText(_translate("MainWindow", "adaboost"))
        self.liblinearBox.setText(_translate("MainWindow", "liblinear_svc"))
        self.libsvmBox.setText(_translate("MainWindow", "libsvm_svc"))
        self.knnBox.setText(_translate("MainWindow", "k_nearest_neighbors"))
        self.gradientBox.setText(_translate("MainWindow", "gradient_boosting"))
        self.sgdBox.setText(_translate("MainWindow", "sgd"))
        self.dtreeBox.setText(_translate("MainWindow", "decision_tree"))
        self.label_4.setText(_translate("MainWindow", "Time left for this task"))
        self.label_7.setText(_translate("MainWindow", "Per run time limit"))
        self.label_8.setText(_translate("MainWindow", "Ensemble memory limit"))
        self.label_9.setText(_translate("MainWindow", "Resampling strategy"))
        self.label_10.setText(_translate("MainWindow", "Metric"))
        self.checkBox_16.setText(_translate("MainWindow", "Enable Feature Preprocessing"))
        self.run_Button.setText(_translate("MainWindow", "Run"))
        self.backButton2.setText(_translate("MainWindow", "Back"))
        self.nextButton2.setText(_translate("MainWindow", "Next"))
        self.label_12.setText(_translate("MainWindow", "Holdout Train Size"))
        self.label_11.setText(_translate("MainWindow", "CV folds"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

