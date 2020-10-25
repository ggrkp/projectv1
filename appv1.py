#
import csv
import os
import sys
from io import StringIO

import featuretools
import pandas as pd
import sklearn
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

from functions import Func
from guiv1 import Ui_MainWindow


class MainWindowUIClass(Ui_MainWindow):
    def __init__(self):
        global t_left
        super().__init__()
        self.functions = Func()

    def setupUi(self, MW):

        super().setupUi(MW)

    # ><><><><><<><><><><><><><><><><><<><><><><><><><><><><><<><><><><><><
    # --------------------- PRWTO SCREEN ME IMPORT ------------------------
    # ><><><><><<><><><><><><><><><><><<><><><><><><><><><><><<><><><><><><
    def refreshAll(self):
        self.pathLine.setText(self.functions.getFileName())

    def browseSlot(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "QFileDialog.getOpenFileName()",
            "",
            "CSV Files (*.csv)",
            options=options)
        if fileName:
            self.functions.setFileName(fileName)
            self.refreshAll()

    def importSlot(self):  # Slot gia to import button
        global fileName
        fileName = self.pathLine.text()
        if self.functions.isValid(fileName):
            global data
            data = self.functions.readFile(fileName)
            self.functions.setFileName(self.pathLine.text())
            self.refreshAll()
            popup = QtWidgets.QMessageBox()
            popup.setText("Your file is successfully imported!")
            popup.setWindowTitle(" Success ")
            popup.setIcon(QtWidgets.QMessageBox.Information)
            popup.setStandardButtons(QtWidgets.QMessageBox.Close)
            popup.setDefaultButton(QtWidgets.QMessageBox.Close)
            popup.exec_()
            self.refreshAll()
            # Otan ginei to import me valid file energopoieitai to next button
            self.nextButton.setEnabled(True)
        else:
            popup = QtWidgets.QMessageBox()
            popup.setWindowTitle(" Error ")
            popup.setText("Please, choose a valid file to import!")
            popup.setStandardButtons(QtWidgets.QMessageBox.Retry)
            popup.setIcon(QtWidgets.QMessageBox.Warning)
            popup.setDefaultButton(QtWidgets.QMessageBox.Retry)
            popup.exec_()
            self.refreshAll()

    # Slot gia to cancel button --> KANONIKA KANEI CLEAR ALLA TO EXW ETSI GIA EUKOLIA
    def cancelSlot(self):
        self.pathLine.setText("/home/ggeorg/Desktop/DataSets/iris.csv")

    def nextSlot(self):  # Slot gia to next button
        global preview_num
        preview_num = 100
        self.stackedWidget.setCurrentIndex(1)
        # Molis pataw next tha kanei load to combo Box kai tha periexei ta features.
        # iterating the columns
        for col in data.columns:
            self.comboBox.addItem(col)
        # dimiourgia table me ta dedomena tou dataset gia preview
        self.tableWidget.setRowCount(preview_num)  # set row Count
        self.tableWidget.setColumnCount(
            self.functions.colCount(data))  # set column count
        for i in range(preview_num):
            for j in range(self.functions.colCount(data)):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(f"{ data.iloc[i][j] }"))
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    # ><><><><><<><><><><><><><><><><><<><><><><><><><><><><><<><><><><><><
    # --------------------- SCREEN ME TARGET KAI PREDICTOR FEATURES -------
    # ><><><><><<><><><><><><><><><><><<><><><><><><><><><><><<><><><><><><
    def featureSlot(self):  # Slot gia to drop down box
        item_index = self.comboBox.currentIndex()
        print(f"Ok. Column {item_index} is your Target Feature! ")
        global X
        global y
        y = self.functions.pickTarget(item_index, data)
        X = self.functions.pickPredictors(item_index, data)
        # Otan ginei to import me valid file energopoieitai to next button
        self.nextButton1.setEnabled(True)
        for i in range(preview_num):
            for j in range(self.functions.colCount(data)):
                self.tableWidget.item(i, j).setBackground(
                    QtGui.QColor('white'))
            self.tableWidget.item(i, item_index).setBackground(
                QtGui.QColor('springgreen'))

    def backSlot(self):  # Slot gia to back button
        self.stackedWidget.setCurrentIndex(0)  # Pame ena screen pisw
        self.comboBox.clear()  # Katharizoyme to Combo box gia na mpoun nea features sto drop down
        # Otan ginei to import me valid file energopoieitai to next button
        self.nextButton.setEnabled(False)

    def nextSlot_1(self):  # Next pou pigainei stis parametrous tou modeling
        # Pame ena screen mprosta sto next screen me preprocessing / modeling k parameter tuning
        self.stackedWidget.setCurrentIndex(2)

        global t_left, t_per_run, mem_limit, inc_est, disable_prepro, resample, resample_args, metric

        # MODELING DEFAULTS
        self.groupBox.setCheckable(True)
        self.groupBox.setChecked(False)

        self.timeLeft_box.setMinimum(30)
        self.timeLeft_box.setMaximum(30000)

        self.perRun_box.setMinimum(3)
        self.perRun_box.setMaximum(int(t_left/2))

        meminfo = dict((i.split()[0].rstrip(':'), int(i.split()[1])) for i in open(
            '/proc/meminfo').readlines())  # analoga me ta specs tou pc
        mem_Mb = int(meminfo['MemTotal']/1024)
        self.memory_box.setMinimum(1024)
        self.memory_box.setMaximum(mem_Mb)

        metric_list = ["accuracy", "balanced_accuracy", "roc_auc", "average_precision", "log_loss",
                       "precision", "precision_macro", "precision_micro", "precision_samples", "precision_weighted",
                       "recall", "recall_macro", "recall_micro", "recall_samples", "recall_weighted",
                       "f1", "f1_macro", "f1_micro", "f1_samples", "f1_weighted"]

        self.metricCombo.addItems(metric_list)

        metric = None
        resample_args = None
        resample_list = ["None", "Cross Validation", "Holdout"]
        self.ressampleCombo.addItems(resample_list)
        resample = 'holdout'

        inc_est = ["adaboost",
                   "bernoulli_nb",
                   "decision_tree",
                   "extra_trees",
                   "gaussian_nb",
                   "gradient_boosting",
                   "k_nearest_neighbors",
                   "lda",
                   "liblinear_svc",
                   "libsvm_svc",
                   "multinomial_nb",
                   "passive_aggressive",
                   "random_forest",
                   "sgd",
                   "qda"]

        disable_prepro = None
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    # ><><><><><<><><><><><><><><><><><<><><><><><><><><><><><<><><><><><><
    # --------------------- MODELING SCREEN -------------------------------
    # ><><><><><<><><><><><><><><><><><<><><><><><><><><><><><<><><><><><><
    # Time Left For This Task
    def timeleft_Slot(self):
        global t_left
        t_left = self.timeLeft_box.value()
        self.perRun_box.setMaximum(int(t_left/2))
        print(t_left)

    # Per Run Time Limit
    def perrun_Slot(self):
        global t_per_run
        t_per_run = self.perRun_box.value()
        print(t_per_run)

    # Ensemble Memory Limit
    def ensmemory_Slot(self):
        global mem_limit
        mem_limit = self.memory_box.value()

    # Metric
    def metricBox(self):
        global metric
        combo_idx_metric = self.metricCombo.currentIndex()
        metric = self.metricCombo.itemText(combo_idx_metric)

    # Resample
    def resampleBox(self):
        global resample
        combo_idx_resample = self.ressampleCombo.currentIndex()
        resample_str = self.ressampleCombo.itemText(combo_idx_resample)
        if resample_str == "Cross Validation":
            resample = 'cv'
        elif resample_str == "None":
            resample = None
        else:
            resample = 'holdout'

    def nextSlot_2(self):
        print(f"Included:   {inc_est}")

    def backSlot_1(self):
        pass

    # DEFAULT THA EINAI EILEGMENOI OLOI. AN PATHSEIS TO CHECK THA KSEKINAS NA VAZEIS MONOS SOU .
    def select_all_Estimators(self):
        global inc_est
        if self.groupBox.isChecked():
            inc_est = []

        else:
            self.extratreeBox.setChecked(False)
            self.adaBox.setChecked(False)
            self.gaussianBox.setChecked(False)
            self.bernoulliBox.setChecked(False)
            self.rforoestBox.setChecked(False)
            self.qdaBox.setChecked(False)
            self.multinbBox.setChecked(False)
            self.ldaBox.setChecked(False)
            self.libsvmBox.setChecked(False)
            self.liblinearBox.setChecked(False)
            self.dtreeBox.setChecked(False)
            self.sgdBox.setChecked(False)
            self.gradientBox.setChecked(False)
            self.knnBox.setChecked(False)
            self.pasagrBox.setChecked(False)
            inc_est = ["adaboost",
                       "bernoulli_nb",
                       "decision_tree",
                       "extra_trees",
                       "gaussian_nb",
                       "gradient_boosting",
                       "k_nearest_neighbors",
                       "lda",
                       "liblinear_svc",
                       "libsvm_svc",
                       "multinomial_nb",
                       "passive_aggressive",
                       "random_forest",
                       "sgd",
                       "qda"]

    # ALGORITHMOI CHECKED :
    def adaChecked(self):
        global inc_est
        box_state = self.adaBox.isChecked()
        est_name = self.adaBox.text()
        inc_est = self.functions.app_Estimator(inc_est, box_state, est_name)

    def bernoulliChecked(self):
        global inc_est
        box_state = self.bernoulliBox.isChecked()
        est_name = self.bernoulliBox.text()
        inc_est = self.functions.app_Estimator(inc_est, box_state, est_name)

    def dectreeChecked(self):
        global inc_est
        box_state = self.dtreeBox.isChecked()
        est_name = self.dtreeBox.text()
        inc_est = self.functions.app_Estimator(inc_est, box_state, est_name)

    def extraTreeChecked(self):
        global inc_est
        box_state = self.extratreeBox.isChecked()
        est_name = self.extratreeBox.text()
        inc_est = self.functions.app_Estimator(inc_est, box_state, est_name)

    def gausianChecked(self):
        global inc_est
        box_state = self.gaussianBox.isChecked()
        est_name = self.gaussianBox.text()
        inc_est = self.functions.app_Estimator(inc_est, box_state, est_name)

    def gradient_checked(self):
        global inc_est
        box_state = self.gradientBox.isChecked()
        est_name = self.gradientBox.text()
        inc_est = self.functions.app_Estimator(inc_est, box_state, est_name)

    def knnChecked(self):
        global inc_est
        box_state = self.knnBox.isChecked()
        est_name = self.knnBox.text()
        inc_est = self.functions.app_Estimator(inc_est, box_state, est_name)

    def ldaChecked(self):
        global inc_est
        box_state = self.ldaBox.isChecked()
        est_name = self.ldaBox.text()
        inc_est = self.functions.app_Estimator(inc_est, box_state, est_name)

    def liblinearChecked(self):
        global inc_est
        box_state = self.liblinearBox.isChecked()
        est_name = self.liblinearBox.text()
        inc_est = self.functions.app_Estimator(inc_est, box_state, est_name)

    def libsvmChecked(self):
        global inc_est
        box_state = self.libsvmBox.isChecked()
        est_name = self.bernoulliBox.text()
        inc_est = self.functions.app_Estimator(inc_est, box_state, est_name)

    def multnbChecked(self):
        global inc_est
        box_state = self.multinbBox.isChecked()
        est_name = self.multinbBox.text()
        inc_est = self.functions.app_Estimator(inc_est, box_state, est_name)

    def pasagrChecked(self):
        global inc_est
        box_state = self.pasagrBox.isChecked()
        est_name = self.pasagrBox.text()
        inc_est = self.functions.app_Estimator(inc_est, box_state, est_name)

    def rforestChecked(self):
        global inc_est
        box_state = self.bernoulliBox.isChecked()
        est_name = self.bernoulliBox.text()
        inc_est = self.functions.app_Estimator(inc_est, box_state, est_name)

    def sgdChecked(self):
        global inc_est
        box_state = self.sgdBox.isChecked()
        est_name = self.sgdBox.text()
        inc_est = self.functions.app_Estimator(inc_est, box_state, est_name)

    def qdaChecked(self):
        global inc_est
        box_state = self.qdaBox.isChecked()
        est_name = self.qdaBox.text()
        inc_est = self.functions.app_Estimator(inc_est, box_state, est_name)

    # DISABLE PREPROCESSING
    def prepro_Checked(self):  # Disable Feature Preprocessing
        global disable_prepro
        if self.checkBox_16.isChecked():
            disable_prepro = []
            disable_prepro.append("no_preprocessing")
        else:
            disable_prepro = None

    def modelSlot(self):
        global model, inc_est
        if not inc_est:
            popup = QtWidgets.QMessageBox()
            popup.setWindowTitle(" Error ")
            popup.setText("No Estimators Were Selected!")
            popup.setInformativeText(
                "Please select at least one Estimator from the list.")
            popup.setStandardButtons(QtWidgets.QMessageBox.Retry)
            popup.setIcon(QtWidgets.QMessageBox.Warning)
            popup.exec_()
        else:
            minutes = t_left/60
            seconds = t_left
            self.stackedWidget.setEnabled(False)
            popup = QtWidgets.QMessageBox()
            popup.setWindowTitle(" Running ")
            popup.setText("Please, wait. An ensemble is being created...     ")
            if minutes < 1:
                popup.setInformativeText(
                    f"This process will take about {seconds} seconds.")
            elif minutes == 1:
                popup.setInformativeText(
                    f"This process will take about 1 minute"
                )
            else:
                popup.setInformativeText(
                    f"This process will take about {minutes} minutes.")
            popup.setStandardButtons(QtWidgets.QMessageBox.Close)
            popup.setIcon(QtWidgets.QMessageBox.Information)
            popup.exec_()

            X_train, X_test, y_train, y_test = self.functions.splitData(X, y)
            base = os.path.basename(fileName)
            dataset_name = os.path.splitext(base)[0]

            model = self.functions.callClassifier(
                t_left, t_per_run, mem_limit, inc_est, disable_prepro, resample, resample_args, metric)
            self.functions.fitModel(X_train, y_train, model, dataset_name)
            print(model.sprint_statistics())

            pred = model.predict(X_test)
            print("Accuracy score", sklearn.metrics.accuracy_score(y_test, pred))
            print(model.show_models())
            popup = QtWidgets.QMessageBox()
            popup.setWindowTitle(" Done ")
            popup.setText("An ensemble is created successfully!")
            popup.setStandardButtons(QtWidgets.QMessageBox.Close)
            popup.setIcon(QtWidgets.QMessageBox.Information)
            popup.exec_()
            self.stackedWidget.setEnabled(True)

# Main
def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = MainWindowUIClass()
    MainWindow = QtWidgets.QMainWindow()
    ex.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    app.setStyle("cleanlooks")

main()
