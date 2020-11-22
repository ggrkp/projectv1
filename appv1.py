import csv
import os
import sys
from io import StringIO
import sqlite3

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

# *><><><><><<><><><><><><><><><><><<><><><><><><><><><><><<><><><>
    # ! 1. IMPORT SCREEN -------------------------

# REFRESH

    def refreshAll(self):
        self.pathLine.setText(self.functions.getFileName())

# BROWSE BUTTON
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

# IMPORT BUTTON
    def importSlot(self):  # Slot gia to import button
        global fileName
        fileName = self.pathLine.text()
        if self.functions.isValid(fileName):
            # todo: na kanw akoma enan elegxo gia to an einai empty to file!
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

# CLEAR BUTTON
    def cancelSlot(self):
        # TODO: Na allaksw to clear button k na kanei clear - twra bazei to iris gia eukolia.
        self.pathLine.setText("/home/ggeorg/Desktop/DataSets/iris.csv")

# NEXT BUTTON POU KANEI TO PREVIEW
    def nextSlot(self):  # Slot gia to next button
        global preview_num
        preview_num = 45
        self.stackedWidget.setCurrentIndex(1)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)

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

# *^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    # *><><><><><<><><><><><><><><><><><<><><><><><><><><><><><<><><><><><><
    # ! 2. TARGET FEATURE - PREVIEW SCREEN ------------

# TARGET FEATURE DROPDOWN KAI PREVIEW
    def featureSlot(self):  # Slot gia to drop down box
        global learning_type
        item_index = self.comboBox.currentIndex()
        print(f"Ok. Column {item_index} is your Target Feature! ")
        global X
        global y
        y = self.functions.pickTarget(item_index, data)
        #! edw apofasizetai an einai regression i classification
        if y.dtype.name == 'category' or y.dtype.name == 'object':
            learning_type = 'Classification'
        else:
            learning_type = 'Regression'

        X = self.functions.pickPredictors(item_index, data)
        # Otan ginei to import me valid file energopoieitai to next button
        self.nextButton1.setEnabled(True)
        self.load_DB_btn.setEnabled(True)

        for i in range(preview_num):
            for j in range(self.functions.colCount(data)):
                self.tableWidget.item(i, j).setBackground(
                    QtGui.QColor('white'))
            self.tableWidget.item(i, item_index).setBackground(
                QtGui.QColor('springgreen'))

# NEXT BUTTON - BACK BUTTON > DHLWNONTAI DEFAULTS GIA TO EPOMENO SCREEN ( MDOELING SCREEN - PARAMETERS )
    def backSlot(self):  # Slot gia to back button
        self.stackedWidget.setCurrentIndex(0)  # Pame ena screen pisw
        self.comboBox.clear()  # Katharizoyme to Combo box gia na mpoun nea features sto drop down
        # Otan ginei to import me valid file energopoieitai to next button
        self.nextButton.setEnabled(False)

    def nextSlot_1(self):  # Next pou pigainei stis parametrous tou modeling
        # Pame ena screen mprosta sto next screen me preprocessing / modeling k parameter tuning
        global t_left, t_per_run, mem_limit, inc_est, disable_prepro, resample, resample_args, metric
        self.stackedWidget.setCurrentIndex(3)

        #! ARXIKOPOIHSEIS ANALOGA ME REGRESSION CLASSIFICATION
        if learning_type == "Classification":
            self.label_13.setText("Select Classification Parameters")

            metric_list = ["accuracy", "balanced_accuracy", "roc_auc", "average_precision", "log_loss",
                           "precision", "precision_macro", "precision_micro", "precision_samples", "precision_weighted",
                           "recall", "recall_macro", "recall_micro", "recall_samples", "recall_weighted",
                           "f1", "f1_macro", "f1_micro", "f1_samples", "f1_weighted"]

            self.metricCombo.addItems(metric_list)
            metric = None
            self.ardBox.hide()
            self.linearsvr_Box.hide()
            self.libsvrBox.hide()
            self.gausianPro_Box.hide()

            self.bernoulliBox.show()
            self.liblinearBox.show()
            self.libsvmBox.show()
            self.qdaBox.show()
            self.pasagrBox.show()
            self.multinbBox.show()
            self.gaussianBox.show()
            self.ldaBox.show()
            self.bernoulliBox.show()
            self.bernoulliBox.show()

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

        elif learning_type == "Regression":
            self.label_13.setText("Select Regression Parameters")

            self.ardBox.show()
            self.linearsvr_Box.show()
            self.libsvrBox.show()
            self.gausianPro_Box.show()

            self.bernoulliBox.hide()
            self.liblinearBox.hide()
            self.libsvmBox.hide()
            self.qdaBox.hide()
            self.pasagrBox.hide()
            self.multinbBox.hide()
            self.gaussianBox.hide()
            self.ldaBox.hide()
            self.bernoulliBox.hide()
            self.bernoulliBox.hide()

            metric_list = ["mean_absolute_error",
                           "mean_squared_error",
                           "root_mean_squared_error",
                           "mean_squared_log_error",
                           "median_absolute_error",
                           "r2"]

            self.metricCombo.addItems(metric_list)
            metric = None
            inc_est = ["adaboost",
                       "ard_regression",
                       "decision_tree",
                       "extra_trees",
                       "gaussian_process",
                       "gradient_boosting",
                       "k_nearest_neighbors",
                       "liblinear_svr",
                       "libsvm_svr",
                       "random_forest",
                       "sgd"]

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

        # TODO: Na dialeksw poies metrikes tha xrisimopoiw kai na emfanizontai sto teliko model.

        resample_list = ["Default", "Cross Validation", "Holdout"]
        self.ressampleCombo.addItems(resample_list)

        resample_args = {'train_size': 0.67}
        resample = "holdout"

        disable_prepro = None

        self.holdout_box.setEnabled(False)
        self.cvfoldsBox.setEnabled(False)

# *^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    # *><><><><><<><><><><><><><><><><><<><><><><><><><><><><><<><><><><><><
    # ! 3. MAKE MODEL SCREEN --------------------------

# TIME LEFT FOR THIS TASK SPINBOX
    def timeleft_Slot(self):
        global t_left
        t_left = self.timeLeft_box.value()
        self.perRun_box.setMaximum(int(t_left/2))
        print(t_left)

# PER RUN TIME LIMIT SPINBOX
    def perrun_Slot(self):
        global t_per_run
        t_per_run = self.perRun_box.value()
        print(t_per_run)

# ENSEMBLE MEMORY LIMIT SPINBOX
    def ensmemory_Slot(self):
        global mem_limit
        mem_limit = self.memory_box.value()

# METRIC SELECTION DROPDOWN
    def metricBox(self):
        global metric
        combo_idx_metric = self.metricCombo.currentIndex()
        metric = self.metricCombo.itemText(combo_idx_metric)

# RESAMPLING STRATEGY DROPDOWN
    def resampleBox(self):
        global resample, resample_args
        combo_idx_resample = self.ressampleCombo.currentIndex()
        resample_str = self.ressampleCombo.itemText(combo_idx_resample)

        if resample_str == "Cross Validation":
            self.cvfoldsBox.setEnabled(True)
            self.holdout_box.setEnabled(False)
            self.cvfoldsBox.setRange(2, 10)
            resample_args = {'folds': 2}
            resample = "cv"

        elif resample_str == "Default":
            self.holdout_box.setEnabled(False)
            self.cvfoldsBox.setEnabled(False)
            resample_args = {'train_size': 0.67}
            resample = "holdout"

        else:
            self.holdout_box.setEnabled(True)
            self.cvfoldsBox.setEnabled(False)
            self.holdout_box.setRange(0.1, 1.0)
            self.holdout_box.setSingleStep(0.01)
            self.holdout_box.setDecimals(2)
            self.holdout_box.setValue(0.67)
            resample_args = {'train_size': 0.67}
            resample = "holdout"

# CV FOLDS - HOLDOUT TRAIN SIZE SPINBOXES
    def cv_Folds(self):
        global resample_args
        folds = self.cvfoldsBox.value()
        resample_args = {'folds': folds}

    def holdout_Size(self):
        global resample_args
        h_size = self.holdout_box.value()
        resample_args = {'train_size': h_size}

# NEXT BUTTON - BACK BUTTON
    # TODO: To next button na se pigainei sto epomeno screen kai na pernaei oti arguments kai data xreiazontai gi auto :

    def nextSlot_2(self):
        print(f"Included:   {inc_est}")
        print("Metric:", metric)
        print("Resampling_Technique:", resample)
        print("Args:", resample_args)
        print(t_left)
        print("Yoleleison")

    def backSlot_1(self):
        self.checkBox_16.setChecked(False)
        self.stackedWidget.setCurrentIndex(1)  # Pame ena screen pisw
        self.metricCombo.clear()
        self.ressampleCombo.clear()

#! Estimators - Preprocessing
# BUTTON GIA MANUALL SELCECTION ESTIMATORS

    def select_all_Estimators(self):
        global inc_est
        if self.groupBox.isChecked():
            inc_est = []
        else:
            if learning_type == "Classification":

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
            else:
                self.extratreeBox.setChecked(False)
                self.adaBox.setChecked(False)
                self.ardBox.setChecked(False)
                self.gausianPro_Box.setChecked(False)
                self.rforoestBox.setChecked(False)
                self.multinbBox.setChecked(False)
                self.libsvrBox.setChecked(False)
                self.linearsvr_Box.setChecked(False)
                self.dtreeBox.setChecked(False)
                self.sgdBox.setChecked(False)
                self.gradientBox.setChecked(False)
                self.knnBox.setChecked(False)

                inc_est = ["adaboost",
                           "ard_regression",
                           "decision_tree",
                           "extra_trees",
                           "gaussian_process",
                           "gradient_boosting",
                           "k_nearest_neighbors",
                           "liblinear_svr",
                           "libsvm_svr",
                           "random_forest",
                           "sgd"]

# ESTIMATORS CHECK BOXES (MPAINOUN SE LISTA) :
    def ard_Checked(self):
        global inc_est
        box = self.ardBox
        box_state = box.isChecked()
        est_name = box.text()
        inc_est = self.functions.app_Estimator(inc_est, box_state, est_name)

    def gausianPro_Checked(self):
        global inc_est
        box = self.gausianPro_Box
        box_state = box.isChecked()
        est_name = box.text()
        inc_est = self.functions.app_Estimator(inc_est, box_state, est_name)

    def liblinearsvr_Checked(self):
        global inc_est
        box = self.linearsvr_Box
        box_state = box.isChecked()
        est_name = box.text()
        inc_est = self.functions.app_Estimator(inc_est, box_state, est_name)

    def libsvr_Checked(self):
        global inc_est
        box = self.libsvrBox
        box_state = box.isChecked()
        est_name = box.text()
        inc_est = self.functions.app_Estimator(inc_est, box_state, est_name)

    def adaChecked(self):
        global inc_est
        box = self.adaBox
        box_state = box.isChecked()
        est_name = box.text()
        inc_est = self.functions.app_Estimator(inc_est, box_state, est_name)

    def bernoulliChecked(self):
        global inc_est
        box = self.bernoulliBox
        box_state = box.isChecked()
        est_name = box.text()
        inc_est = self.functions.app_Estimator(inc_est, box_state, est_name)

    def dectreeChecked(self):
        global inc_est
        box = self.dtreeBox
        box_state = box.isChecked()
        est_name = box.text()
        inc_est = self.functions.app_Estimator(inc_est, box_state, est_name)

    def extraTreeChecked(self):
        global inc_est
        box = self.extratreeBox
        box_state = box.isChecked()
        est_name = box.text()
        inc_est = self.functions.app_Estimator(inc_est, box_state, est_name)

    def gausianChecked(self):
        global inc_est
        box = self.gaussianBox
        box_state = box.isChecked()
        est_name = box.text()
        inc_est = self.functions.app_Estimator(inc_est, box_state, est_name)

    def gradient_checked(self):
        global inc_est
        box = self.gradientBox
        box_state = box.isChecked()
        est_name = box.text()
        inc_est = self.functions.app_Estimator(inc_est, box_state, est_name)

    def knnChecked(self):
        global inc_est
        box = self.knnBox
        box_state = box.isChecked()
        est_name = box.text()
        inc_est = self.functions.app_Estimator(inc_est, box_state, est_name)

    def ldaChecked(self):
        global inc_est
        box = self.ldaBox
        box_state = box.isChecked()
        est_name = box.text()
        inc_est = self.functions.app_Estimator(inc_est, box_state, est_name)

    def liblinearChecked(self):
        global inc_est
        box = self.liblinearBox
        box_state = box.isChecked()
        est_name = box.text()
        inc_est = self.functions.app_Estimator(inc_est, box_state, est_name)

    def libsvmChecked(self):
        global inc_est
        box = self.libsvmBox
        box_state = box.isChecked()
        est_name = box.text()
        inc_est = self.functions.app_Estimator(inc_est, box_state, est_name)

    def multnbChecked(self):
        global inc_est
        box = self.multinbBox
        box_state = box.isChecked()
        est_name = box.text()
        inc_est = self.functions.app_Estimator(inc_est, box_state, est_name)

    def pasagrChecked(self):
        global inc_est
        box = self.pasagrBox
        box_state = box.isChecked()
        est_name = box.text()
        inc_est = self.functions.app_Estimator(inc_est, box_state, est_name)

    def rforestChecked(self):
        global inc_est
        box = self.rforoestBox
        box_state = box.isChecked()
        est_name = box.text()
        inc_est = self.functions.app_Estimator(inc_est, box_state, est_name)

    def sgdChecked(self):
        global inc_est
        box = self.sgdBox
        box_state = box.isChecked()
        est_name = box.text()
        inc_est = self.functions.app_Estimator(inc_est, box_state, est_name)

    def qdaChecked(self):
        global inc_est
        box = self.qdaBox
        box_state = box.isChecked()
        est_name = box.text()
        inc_est = self.functions.app_Estimator(inc_est, box_state, est_name)

# DISABLE PREPROCESSING CHECKBOX
    def prepro_Checked(self):  # Disable Feature Preprocessing
        global disable_prepro
        if self.checkBox_16.isChecked():
            disable_prepro = []
            disable_prepro.append("no_preprocessing")
        else:
            disable_prepro = None

#! Modeling
# RUN BUTTON => START CREATING ENSEMBLES
    # TODO: Gia to run button prepei na apothikeuw to teliko model / ensemble se ena file
    # TODO: Na vrw tropo na to anaktw kai na to xrismopoiw h na to porbalw sthn othoni se History tab (PX)

    def modelSlot(self):
        global model, inc_est, resample
        #! ELEGXOS AN EXOUN EPILEXTHEI ESTIMATORS:
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
                    f"This process will take about {minutes} minutes. Press OK to continue...")
            popup.setStandardButtons(QtWidgets.QMessageBox.Ok)
            popup.setIcon(QtWidgets.QMessageBox.Information)
            popup.exec_()

            #! Data Splitting:
            X_train, X_test, y_train, y_test = self.functions.splitData(X, y)
            base = os.path.basename(fileName)
            dataset_name = os.path.splitext(base)[0]

            #! Check learning problem Type:
            if learning_type == "Classification":  # classifier call
                model = self.functions.callClassifier(
                    t_left, t_per_run, mem_limit, inc_est, disable_prepro, resample, resample_args, metric)
            elif learning_type == "Regression":  # regressor call
                model = self.functions.callRegressor(
                    t_left, t_per_run, mem_limit, inc_est, disable_prepro, resample, resample_args, metric)
            #! Model Fit:
            model = self.functions.fitModel(
                X_train, y_train, model, dataset_name)
            pred = model.predict(X_test)

            #! Metric results:
            if learning_type == 'Regression':
                print("Max error", sklearn.metrics.max_error(y_test, pred))
            elif learning_type == "Classification":
                print("Accuracy score", sklearn.metrics.accuracy_score(y_test, pred))

            # print(model.get_models_with_weights())

            # print(model.show_models())
            popup = QtWidgets.QMessageBox()
            popup.setWindowTitle(" Done ")
            popup.setText("An ensemble is created successfully!")
            popup.setStandardButtons(QtWidgets.QMessageBox.Close)
            popup.setIcon(QtWidgets.QMessageBox.Information)
            popup.exec_()
            self.stackedWidget.setEnabled(True)

            if self.savemodel_Box.isChecked():
                self.functions.store_model(model, "model")

# *^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    # *><><><><><<><><><><><><><><><><><<><><><><><><><><><><><<><><><><><><
    # ! 4. LOAD DATABASE SCREEN ---------------------
    def load_DB(self):  # tha kanei connect meta tha kanei load kai tha petaei mesa ta records!
        self.stackedWidget.setCurrentIndex(2)
        db_name = 'modelsDB.db'

        conn = sqlite3.connect(db_name)

        # QUERIES
        cursor = conn.execute("select name, timestamp from models")
        curs1 = conn.execute("select count(*) from models")
        tbl_rowcount = curs1.fetchone()
        self.dbTable.setRowCount(tbl_rowcount[0])
        self.dbTable.setColumnCount(2)
        self.dbTable.setSelectionBehavior(QTableWidget.SelectRows)
        # DATABASE VIEW
        row = 0
        while True:
            form = cursor.fetchone()
            if form == None:
                break
            for column, item in enumerate(form):
                self.dbTable.setItem(
                    row, column, QTableWidgetItem(f'{item}'))
            row += 1


    def fetch_model(self):
        global ft_model
        currow = self.dbTable.currentRow()
        tstamp = self.dbTable.item(currow, 1)

        if tstamp == None:
            popup = QtWidgets.QMessageBox()
            popup.setWindowTitle(" Error ")
            popup.setText("No Models Were Selected!")
            popup.setInformativeText(
                "Please select a model form the list.")
            popup.setStandardButtons(QtWidgets.QMessageBox.Retry)
            popup.setIcon(QtWidgets.QMessageBox.Warning)
            popup.exec_()
        else:
            tstamp = self.dbTable.item(currow, 1).text()
            ft_model = self.functions.load_model(tstamp)
            self.showen_btn.setEnabled(True)
            self.predict_btn.setEnabled(True)

    def show_ensembles(self):
        global ft_model
        print(ft_model.show_models())

    def predict_y(self):
        global X,y,ft_model
        score = ft_model.score(X, y)
        print("Test Score with pickle model: {0:.2f} %". format(100 * score))
        y_predict = ft_model.predict(X)
        print(y_predict)

    def save_Checked(self):
        pass

# *^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = MainWindowUIClass()
    MainWindow = QtWidgets.QMainWindow()
    ex.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


main()
